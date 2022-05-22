'''
@Author: yunchuan.wang@nxp.com
@Github: https://github.com/weltry/S32K1xx-CSEc-Tool.git
@LastEditors: yunchuan.wang@nxp.com
@LastEditTime: 2022-05-22 13:15:05
'''


 
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import binascii
import csec

'''
@description: 
@param {type} 
@return: 
'''
def KDF(AuthKey, Constant):
    Concat = AuthKey + Constant
    IV = "00"*16
    K_out = csec.CSEC_MPCompress(Concat,IV)
    return K_out

'''
@description: 
@param {type} all input is hex string
@return: 
'''
def CalculateM1ToM5(AuthKey, NewKey, AuthKeyID, NewKeyID, Counter, Flags, UID, CSEC_UID):
    MOut = {}
    KEY_UPDATE_ENC_C = "010153484500800000000000000000B0"
    KEY_UPDATE_MAC_C = "010253484500800000000000000000B0"
    #M1
    MOut["M1"] = (UID[:30] + NewKeyID[1:2] + AuthKeyID[1:2])
    #M2
    #Tmp_Text[0]~Tmp_Text[2]:Counter Bit24~Bit4 
    Tmp_Text = Counter[1:] + Flags + "0" + "00"*11 + NewKey 
    Key = KDF(AuthKey,KEY_UPDATE_ENC_C)
    MOut["M2"] = csec.CSEC_EncryptCBC(Key,str(Tmp_Text),IV="00"*16)
    #M3
    Key = KDF(AuthKey,KEY_UPDATE_MAC_C)
    M1M2 = MOut["M1"] + MOut["M2"]
    MOut["M3"]  = csec.CSEC_GenerateMAC(Key,M1M2)
    #M4
    Key = KDF(NewKey,KEY_UPDATE_ENC_C)
    #calculate K4* = ENCECB(K3(CID’(28 bits) | “1”(1bit) | “0…0”(99 bits)))
    Tmp_Text = Counter[1:] + "8"
    M4_Star = csec.CSEC_EncryptCBC(Key,str(Tmp_Text),IV="00"*16)
    MOut["M4"] = CSEC_UID  + NewKeyID[1:] + AuthKeyID[1:] + M4_Star
    #M5
    Key = KDF(NewKey,KEY_UPDATE_MAC_C)
    MOut["M5"]  = csec.CSEC_GenerateMAC(Key,MOut["M4"])
    return MOut

'''
@description: 
@param {type} 
@return: 
'''
def CheckSum(HexString):
    binary = binascii.unhexlify(HexString)
    checksum = 0
    for ch in binary:
        checksum += ch
        checksum &= 0xff
    checksum = checksum ^ 0xff
    return ("{:0>2x}".format(checksum)).upper()
