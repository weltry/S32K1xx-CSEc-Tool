/* ###################################################################
**     Filename    : main.c
**     Processor   : S32K11x
**     Abstract    :
**         Main module.
**         This module contains user's application code.
**     Settings    :
**     Contents    :
**         No public methods
**
** ###################################################################*/
/*!
** @file main.c
** @version 01.00
** @brief
**         Main module.
**         This module contains user's application code.
*/
/*!
**  @addtogroup main_module main module documentation
**  @{
*/
/* MODULE main */


/* Including necessary module. Cpu.h contains other modules needed for compiling.*/
#include "Cpu.h"

  volatile int exit_code = 0;

/* User includes (#include below this line is not maintained by Processor Expert) */
#include "Flash1.h"
#include "Csec1.h"
#include "CSEc_functions.h"
#include "CSEc_Keys.h"

#define CSEC_KEYS_MEM __attribute__((section (".CSEcKeys")))

#define RESET 1
#define INIT  0

flash_ssd_config_t  flashSSDConfig;

typedef struct
{
	uint32_t   KeyID:8;
	uint32_t   Enable:8;
	uint32_t   Flags:8;
	uint32_t   Reserved:8;
	uint32_t   Counter;
	uint8_t    Buffer[8];
	uint8_t    Key[16];
}CSEcKeys_t;

uint8_t    CSEC_KEYS_MEM PartitionCode[16]={/*default setting*/
											0x00,  //0:MCU partnumber
											0x02, //1:EEP size,          0x02:4k eeprom
											0x04, //2:DEflash partition, 0x04:64K EFlash:0K DFlash
											0x03, //3:total key number,  0x03:24Key
											0x1,  //4:USFE,              0x1: Enable
											0x01, //5:Flex ram auto load eep data 0x1:Enable must be 0x1 when use csec
											0x03, //6:secure boot mode   0x03: CSEC_BOOT_NOT_DEFINED
											0x00,0x00,0x00,0x00, //7~10:boot size Low byte frist
											0x1,  //11:0-Init 1-reset,   0x1: reset CSEc
											0x00,0x00,0x00,0x00 //unused
											};

CSEcKeys_t CSEC_KEYS_MEM CSEc_Keys_Buffer[20]=
{
	//      ID        Enable   Flags   reserved  Counter  reserved buffer       Key
	{CSEC_MASTER_ECU,   1,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_BOOT_MAC_KEY, 0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_BOOT_MAC,     0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_1,        0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_2,        0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_3,        0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_4,        0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_5,        0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_6,        0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_7,        0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_8,        0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_9,        0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_10,       0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_11,       0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_12,       0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_13,       0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_14,       0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_15,       0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_16,       0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
	{CSEC_KEY_17,       0,      0,     0,        0x1,     RESERVED_8,  BLANK_KEY},
};

/*!
  \brief The main function for the project.
  \details The startup initialization sequence is the following:
 * - startup asm routine
 * - main()
*/
int main(void)
{
  /* Write your local variable definition here */
	uint16_t Res=0u;
	uint8_t  i;
	uint8_t  M1[16u], M2[32u], M3[16u], M4[32u], M5[16u], M4_out[32u], M5_out[16u];
	uint8_t  EEEDataSizeCode;
	uint8_t  DEPartitionCode;
	uint8_t  CSEcKeySize;
	bool     SFE;
	bool     LoadEEEData;
	uint8_t  SecureBootMode=0u;
	uint32_t BootSize=0u; //byte
	uint8_t  InitOrReset=0u;
	uint8_t  BlankKey[16u] = BLANK_KEY;
	uint8_t *AuthKey=NULL;
	uint8_t  Challenge[16u]={0x00u};
	uint8_t  DbgAuth[16u] = {0x00u};
  /*** Processor Expert internal initialization. DON'T REMOVE THIS CODE!!! ***/
  #ifdef PEX_RTOS_INIT
    PEX_RTOS_INIT();                   /* Initialization of the selected RTOS. Macro is defined by the RTOS component. */
  #endif
  /*** End of Processor Expert internal initialization.                    ***/

  /* Write your code here */
  /* For example: for(;;) { } */
	EEEDataSizeCode = PartitionCode[1u];
	DEPartitionCode = PartitionCode[2u];
	CSEcKeySize     = PartitionCode[3u];
	SFE             = PartitionCode[4u];
	LoadEEEData     = PartitionCode[5u];
	SecureBootMode  = PartitionCode[6u];
	BootSize        = ((PartitionCode[7u]<<24u)|(PartitionCode[8u]<<16u)|(PartitionCode[9u]<<8u)|PartitionCode[10u]);
	InitOrReset     = PartitionCode[11u];

    /*initialize Flash*/
    FLASH_DRV_Init(&Flash1_InitConfig0,&flashSSDConfig);
    if ((flashSSDConfig.EEESize == 0)&&(INIT == InitOrReset))
    {
    	FLASH_DRV_DEFlashPartition(&flashSSDConfig,EEEDataSizeCode,DEPartitionCode,CSEcKeySize,SFE,LoadEEEData);
    }
	else if ((flashSSDConfig.EEESize == 0)&&(RESET == InitOrReset))
	{
		return exit_code;
	}
	else
	{

	}
    /*initialize CSEc*/
	CSEC_DRV_Init(&csec1_State);
	/*initialize RNG*/
	CSEC_DRV_InitRNG();
	if(RESET == InitOrReset)
	{
		Res |= CSEC_DRV_DbgChal(Challenge);
		Res |= CalculateDbgAuth(CSEc_Keys_Buffer[0].Key,Challenge,DbgAuth);
		Res |= CSEC_DRV_DbgAuth(DbgAuth);
		if(Res != STATUS_SUCCESS)
		{
			//error
		}
	}
	else if(INIT == InitOrReset)
	{
		for(i=0u;i<20u;i++)
		{
			if(CSEc_Keys_Buffer[i].Enable == true)
			{
				if(CSEc_Keys_Buffer[i].KeyID == CSEC_MASTER_ECU)
				{
					AuthKey = BlankKey;
				}
				else
				{
					AuthKey = CSEc_Keys_Buffer[0].Key;//master Ecu key
				}
				Res = 0;
				/* Calculate M1 to M5 in Software */
				Res |= CalculateM1ToM5( AuthKey,  /*Auth Key value*/
										CSEc_Keys_Buffer[i].Key,   /*Update new key value*/
										CSEC_MASTER_ECU,           /*Auth Key  ID*/
										CSEc_Keys_Buffer[i].KeyID, /*update new key ID*/
										CSEc_Keys_Buffer[i].Counter, /*counter*/
										CSEc_Keys_Buffer[i].Flags,   /*Flags*/
										M1, M2, M3, M4, M5);         /*M1~M5 value*/
				Res |= CSEC_DRV_LoadKey(CSEc_Keys_Buffer[i].KeyID,M1, M2, M3,M4_out,M5_out);
				if(Res != STATUS_SUCCESS)
				{
					//error
				}
			}
		}
		//secure boot
		if(SecureBootMode != CSEC_BOOT_NOT_DEFINED)
		{
			Res = CSEC_DRV_BootDefine(BootSize*8,SecureBootMode);
			if(Res != STATUS_SUCCESS)
			{
				//error
			}
		}
	}

  /*** Don't write any code pass this line, or it will be deleted during code generation. ***/
  /*** RTOS startup code. Macro PEX_RTOS_START is defined by the RTOS component. DON'T MODIFY THIS CODE!!! ***/
  #ifdef PEX_RTOS_START
    PEX_RTOS_START();                  /* Startup of the selected RTOS. Macro is defined by the RTOS component. */
  #endif
  /*** End of RTOS startup code.  ***/
  /*** Processor Expert end of main routine. DON'T MODIFY THIS CODE!!! ***/
  for(;;) {
    if(exit_code != 0) {
      break;
    }
  }
  return exit_code;
  /*** Processor Expert end of main routine. DON'T WRITE CODE BELOW!!! ***/
} /*** End of main routine. DO NOT MODIFY THIS TEXT!!! ***/

/* END main */
/*!
** @}
*/
/*
** ###################################################################
**
**     This file was created by Processor Expert 10.1 [05.21]
**     for the Freescale S32K series of microcontrollers.
**
** ###################################################################
*/
