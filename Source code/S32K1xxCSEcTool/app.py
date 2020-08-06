'''
@Author: yunchuan.wang@nxp.com
@Github: https://github.com/weltry/S32K1xx-CSEc-Tool.git
@LastEditors: yunchuan.wang@nxp.com
@LastEditTime: 2020-07-03 12:47:09
'''

# -*- coding: utf-8 -*-
import string
import utility
import hashlib 

#Avoid file read permission issues
import Firmware.S32K116F128 as FW_S32K116F128
import Firmware.S32K118F256 as FW_S32K118F256
import Firmware.S32K142F256 as FW_S32K142F256
import Firmware.S32K144F512 as FW_S32K144F512
import Firmware.S32K146F1M  as FW_S32K146F1M
import Firmware.S32K148F2M  as FW_S32K148F2M

FW_Bin_DIC = {\
"S32K116F128":FW_S32K116F128.Bin,\
"S32K118F256":FW_S32K118F256.Bin,\
"S32K142F256":FW_S32K142F256.Bin,\
"S32K144F512":FW_S32K144F512.Bin,\
"S32K146F1M":FW_S32K146F1M.Bin,\
"S32K148F2M":FW_S32K148F2M.Bin }

__KeyInfList__ = None

'''
@description: 
@param {type} 
@return: 
'''
def ImportKey(KeyInfList):
    global __KeyInfList__
    __KeyInfList__ = KeyInfList


'''
@description: 
@param {type} 
@return: 
'''
def CreatFirmware(Path,CSEcCfg):
    global __KeyInfList__
    KeyIdToKeyNameDic = {"01":"CSEC_MASTER_ECU", "02":"CSEC_BOOT_MAC_KEY", "03":"CSEC_BOOT_MAC", "04":"CSEC_KEY_1", "05":"CSEC_KEY_2",\
                         "06":"CSEC_KEY_3",      "07":"CSEC_KEY_4",        "08":"CSEC_KEY_5",    "09":"CSEC_KEY_6", "0A":"CSEC_KEY_7",\
                         "0B":"CSEC_KEY_8",      "0C":"CSEC_KEY_9",        "0D":"CSEC_KEY_10",   "14":"CSEC_KEY_11","15":"CSEC_KEY_12",\
                         "16":"CSEC_KEY_13",     "17":"CSEC_KEY_14",       "18":"CSEC_KEY_15",   "19":"CSEC_KEY_16","1A":"CSEC_KEY_17"}
    
    if (__KeyInfList__ == None):
        return "Failed! Please Config Key First!\n"
    FwString = str(FW_Bin_DIC[ CSEcCfg["MCU"] ])
    Index = FwString.find("S1130410", 0,len(FwString))
    if Index == -1:
        return "Error:The firmware error !"
    ConfigList= "MCU: " + str(CSEcCfg["MCU"]) + "\n" \
                "uEEEDataSizeCode: " + "0x{:0>2x}".format(CSEcCfg["EepSizeCode"]) + "\n" + \
                "uDEPartitionCode: " + "0x{:0>2x}".format(CSEcCfg["PartitionCode"]) + "\n" + \
                "uCSEcKeySize: "     + "0x{:0>2x}".format(CSEcCfg["KeyNumCode"]) + "\n" + \
                "uSFE: "+ str(CSEcCfg["USFE"]) + "\n" + \
                "flexRamEnableLoadEEEData: " + str(CSEcCfg["AutoLoad"]) + "\n\n"
    #modify string by chop it
    #byte 0: part number  
    FwString = FwString[:Index+8] + "{:0>2x}".format(int(CSEcCfg["MCU"][4:7])) + FwString[Index+10:]
    #byte 1: EepSize code 
    FwString = FwString[:Index+10] + "{:0>2x}".format(CSEcCfg["EepSizeCode"]).upper() + FwString[Index+12:]
    #byte 2: DEFlash partition code 
    FwString = FwString[:Index+12] + "{:0>2x}".format(CSEcCfg["PartitionCode"]).upper() + FwString[Index+14:]
    #byte 3: total key number code
    FwString = FwString[:Index+14] + "{:0>2x}".format(CSEcCfg["KeyNumCode"]).upper() + FwString[Index+16:]
    #byte 4: USFE 
    FwString = FwString[:Index+16] + "{:0>2x}".format(CSEcCfg["USFE"]).upper() + FwString[Index+18:]
    #byte 5: Flex ram auto load eep data
    FwString = FwString[:Index+18] + "{:0>2x}".format(CSEcCfg["AutoLoad"]).upper() + FwString[Index+20:]
    #byte 6: Secure boot mode
    #byte 7~10: Boot size Low byte frist
    if CSEcCfg["SecureBoot"] == True:
        FwString = FwString[:Index+20] + "{:0>2x}".format(CSEcCfg["SecureBootMode"]).upper() + FwString[Index+22:]
        FwString = FwString[:Index+22] + "{:0>8x}".format(CSEcCfg["BootSize"]).upper() + FwString[Index+30:]
    else:
        FwString = FwString[:Index+20] + "03"   + FwString[Index+22:] #03 means CSEC_BOOT_NOT_DEFINED refer S32DS project
        FwString = FwString[:Index+22] + "00"*4 + FwString[Index+30:]
    #byte 11:Init or reset
    if CSEcCfg["InitOrReset"] == "Init":
        FwString = FwString[:Index+30] + "00" + FwString[Index+32:]
    else:
        FwString = FwString[:Index+30] + "01" + FwString[Index+32:]
    #check sum
    FwString = FwString[:Index+40] + (utility.CheckSum(FwString[Index+2:Index+40])) + FwString[Index+42:]
    #key 
    for keyinf in __KeyInfList__:
        KeyID = "{:0>2x}".format(keyinf["KeyID"]).upper()
        #line 1
        Index = Index + 43
        #byte 0: Key Id
        FwString = FwString[:Index+8]  + KeyID + FwString[Index+10:]
        #byte 1: Enable
        FwString = FwString[:Index+10] + "{:0>2x}".format(keyinf["Enable"]) + FwString[Index+12:]
        #byte 2: Flags
        FwString = FwString[:Index+12] + "{:0>2x}".format(keyinf["Flags"]) + FwString[Index+14:]
        #byte 3: reserved 
        FwString = FwString[:Index+14] + "00" + FwString[Index+16:]
        #byte 4~7: Counter Low byte frist 
        FwString = FwString[:Index+16] + "01000000" + FwString[Index+24:] #counter always set 1
        #byte 8~16: reserved 
        FwString = FwString[:Index+24] + "00"*8 + FwString[Index+40:]
        #check sum
        FwString = FwString[:Index+40] + (utility.CheckSum(FwString[Index+2:Index+40])) + FwString[Index+42:]
        #line 2
        Index = Index + 43
        #byte 0~16: Key value
        FwString = FwString[:Index+8]  + keyinf["KeyValue"] + FwString[Index+40:]
        #check sum
        FwString = FwString[:Index+40] + (utility.CheckSum(FwString[Index+2:Index+40])) + FwString[Index+42:]
        #for generate config list text file
        if keyinf["Enable"] == True:
            ConfigList += "KeyName: " + KeyIdToKeyNameDic[KeyID] + "\n"\
                          "KeyID: 0x" + KeyID + "\n"\
                          "Key: "     + keyinf["KeyValue"] + "\n"\
                          "Flags: 0x" + "{:0>2x}".format(keyinf["Flags"]) + "\n"\
                          "Counter: " + "1" + "\n\n"
    ConfigList += "Soure code:https://github.com/weltry/S32K1xx-CSEc-Tool.git \n\n"
    FileName1 = "\\" + CSEcCfg["MCU"] + CSEcCfg["InitOrReset"] +"FW.srec"
    FileName2 = "\\" + CSEcCfg["MCU"] + "CSEcConfigList.txt"
    try:
        f = open(Path+FileName1,"w")
        f.write(FwString)
        f.close()
        f= open(Path+FileName2,"w")
        f.write(ConfigList)
        f.close()
        return Path + "\n" + FileName1 +"\n"+ FileName2 + "\n" + "Genreated Successful !\n"
    except:
        return Path + "\n" + FileName1 +"\n"+ FileName2 + "\n" + "Error:Open Files Error !\n"
    
