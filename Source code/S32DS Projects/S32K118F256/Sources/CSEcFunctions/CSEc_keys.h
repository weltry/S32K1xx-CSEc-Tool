/*
 * @Author: your name
 * @Date: 2020-04-16 14:33:06
 * @LastEditTime: 2020-05-27 10:31:38
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \S32K144F512\Sources\CSEcFunctions\CSEc_keys.h
 */ 


#ifndef CSEC_KEYS_H_
#define CSEC_KEYS_H_

#define RESERVED_8      {0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u}
#define BLANK_KEY       {0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu}
#define MASTER_ECU_KEY  {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define BOOT_MAC_KEY    {0x12u,0x34u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x00u,0x56u,0x78u}
#define BOOT_MAC        {0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu,0xFFu}
#define USER_KEY01      {0xAFu,0x12u,0x56u,0xFDu,0xBEu,0x89u,0x56u,0x5Cu,0xF1u,0x28u,0xEDu,0x6Au,0XAAu,0x55u,0x44u,0xFFu}
#define USER_KEY02      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY03      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY04      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY05      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY06      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY07      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY08      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY09      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY10      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY11      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY12      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY13      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY14      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY15      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY16      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}
#define USER_KEY17      {0x00u,0x01u,0x02u,0x03u,0x04u,0x05u,0x06u,0x07u,0x08u,0x09u,0x0au,0x0bu,0x0cu,0x0du,0x0eu,0x0fu}

#endif /* CSEC_KEYS_H_ */
