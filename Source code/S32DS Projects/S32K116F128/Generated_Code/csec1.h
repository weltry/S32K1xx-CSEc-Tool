/* ###################################################################
**     This component module is generated by Processor Expert. Do not modify it.
**     Filename    : csec1.h
**     Project     : S32K116F128
**     Processor   : S32K116_48
**     Component   : csec
**     Version     : Component SDK_S32K14x_12, Driver 01.00, CPU db: 3.00.000
**     Repository  : SDK_S32K14x_12
**     Compiler    : GNU C Compiler
**     Date/Time   : 2020-06-29, 23:47, # CodeGen: 1
**     Contents    :
**         CSEC_DRV_Init                - void CSEC_DRV_Init(csec_state_t * state);
**         CSEC_DRV_Deinit              - void CSEC_DRV_Deinit(void);
**         CSEC_DRV_EncryptECB          - status_t CSEC_DRV_EncryptECB(csec_key_id_t keyId,const uint8_t *...
**         CSEC_DRV_DecryptECB          - status_t CSEC_DRV_DecryptECB(csec_key_id_t keyId,const uint8_t *...
**         CSEC_DRV_EncryptCBC          - status_t CSEC_DRV_EncryptCBC(csec_key_id_t keyId,const uint8_t *...
**         CSEC_DRV_DecryptCBC          - status_t CSEC_DRV_DecryptCBC(csec_key_id_t keyId,const uint8_t *...
**         CSEC_DRV_GenerateMAC         - status_t CSEC_DRV_GenerateMAC(csec_key_id_t keyId,const uint8_t *...
**         CSEC_DRV_GenerateMACAddrMode - status_t CSEC_DRV_GenerateMACAddrMode(csec_key_id_t keyId,const uint8_t *...
**         CSEC_DRV_VerifyMAC           - status_t CSEC_DRV_VerifyMAC(csec_key_id_t keyId,const uint8_t * msg,uint32_t...
**         CSEC_DRV_VerifyMACAddrMode   - status_t CSEC_DRV_VerifyMACAddrMode(csec_key_id_t keyId,const uint8_t *...
**         CSEC_DRV_LoadKey             - status_t CSEC_DRV_LoadKey(csec_key_id_t keyId,const uint8_t * m1,const...
**         CSEC_DRV_LoadPlainKey        - status_t CSEC_DRV_LoadPlainKey(const uint8_t * plainKey);
**         CSEC_DRV_ExportRAMKey        - status_t CSEC_DRV_ExportRAMKey(uint8_t * m1,uint8_t * m2,uint8_t * m3,uint8_t...
**         CSEC_DRV_InitRNG             - status_t CSEC_DRV_InitRNG(void);
**         CSEC_DRV_ExtendSeed          - status_t CSEC_DRV_ExtendSeed(const uint8_t * entropy);
**         CSEC_DRV_GenerateRND         - status_t CSEC_DRV_GenerateRND(uint8_t * rnd);
**         CSEC_DRV_BootFailure         - status_t CSEC_DRV_BootFailure(void);
**         CSEC_DRV_BootOK              - status_t CSEC_DRV_BootOK(void);
**         CSEC_DRV_BootDefine          - status_t CSEC_DRV_BootDefine(uint32_t bootSize,csec_boot_flavor_t bootFlavor);
**         CSEC_DRV_GetStatus           - static inline csec_status_t CSEC_DRV_GetStatus(void);
**         CSEC_DRV_GetID               - status_t CSEC_DRV_GetID(const uint8_t * challenge,uint8_t * uid,uint8_t *...
**         CSEC_DRV_DbgChal             - status_t CSEC_DRV_DbgChal(uint8_t * challenge);
**         CSEC_DRV_DbgAuth             - status_t CSEC_DRV_DbgAuth(const uint8_t * authorization);
**         CSEC_DRV_MPCompress          - status_t CSEC_DRV_MPCompress(const uint8_t * msg,uint16_t msgLen,uint8_t *...
**         CSEC_DRV_EncryptECBAsync     - status_t CSEC_DRV_EncryptECBAsync(csec_key_id_t keyId,const uint8_t *...
**         CSEC_DRV_DecryptECBAsync     - status_t CSEC_DRV_DecryptECBAsync(csec_key_id_t keyId,const uint8_t *...
**         CSEC_DRV_EncryptCBCAsync     - status_t CSEC_DRV_EncryptCBCAsync(csec_key_id_t keyId,const uint8_t *...
**         CSEC_DRV_DecryptCBCAsync     - status_t CSEC_DRV_DecryptCBCAsync(csec_key_id_t keyId,const uint8_t *...
**         CSEC_DRV_GenerateMACAsync    - status_t CSEC_DRV_GenerateMACAsync(csec_key_id_t keyId,const uint8_t *...
**         CSEC_DRV_VerifyMACAsync      - status_t CSEC_DRV_VerifyMACAsync(csec_key_id_t keyId,const uint8_t *...
**         CSEC_DRV_GetAsyncCmdStatus   - status_t CSEC_DRV_GetAsyncCmdStatus(void);
**         CSEC_DRV_InstallCallback     - void CSEC_DRV_InstallCallback(security_callback_t callbackFunc,void *...
**         CSEC_DRV_CancelCommand       - void CSEC_DRV_CancelCommand(void);
**
**     Copyright 1997 - 2015 Freescale Semiconductor, Inc.
**     Copyright 2016-2017 NXP
**     All Rights Reserved.
**     
**     THIS SOFTWARE IS PROVIDED BY NXP "AS IS" AND ANY EXPRESSED OR
**     IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
**     OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
**     IN NO EVENT SHALL NXP OR ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
**     INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
**     (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
**     SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
**     HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
**     STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
**     IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
**     THE POSSIBILITY OF SUCH DAMAGE.
** ###################################################################*/
/*!
** @file csec1.h
** @version 01.00
*/
/*!
**  @addtogroup csec1_module csec1 module documentation
**  @{
*/
#ifndef csec1_H
#define csec1_H
/* MODULE csec1. */

/* Include inherited beans */
#include "Cpu.h"

/*! @brief Driver state structure which holds driver runtime data */
extern csec_state_t csec1_State;

#endif
/* ifndef csec1_H */

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
