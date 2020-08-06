'''
@Author: yunchuan.wang@nxp.com
@Github: https://github.com/weltry/S32K1xx-CSEc-Tool.git
@LastEditors: yunchuan.wang@nxp.com
@LastEditTime: 2020-07-02 20:14:06
'''

# -*- coding: UTF-8 -*-
from Crypto.Hash import CMAC
from Crypto.Cipher import AES
import binascii

BLOCK_SIZE = 16

def _PaddingZero(Msg,Length):
    tmp = Msg + bytes([0 for i in range(Length)])
    return tmp[0:Length]
    
def _bxor(a,b):
    return bytes([x ^ y for x, y in zip(a, b)])

'''
@description: Generate MAC
@param {type}: input and output are, such as:"000102030405060708090A0B0C0D"
@return: Msg MAC(hexstring)
'''
def CSEC_GenerateMAC(Key,Msg):
    KeyBin = binascii.unhexlify(Key)
    MsgBin = binascii.unhexlify(Msg)
    Cipher = CMAC.new(KeyBin,MsgBin,ciphermod=AES)
    return Cipher.hexdigest().upper()

'''
@description: S32K1xx Generate BootMAC
@param {type} 
@return: BootMAC
'''
def CSEC_GenerateBootMAC(Key,BootMsg,BootSize):
    #96bits"0" + 32bits "bootsize" + BootMsg 
    if BootSize%4 != 0:
        return "Input length error !,Must be 4 bytes aligned !\n"
    Msg=""
    #Little endian mode to big endian mode
    for i in range(0,len(BootMsg),8):
        Msg = Msg + BootMsg[i+6:i+8] + BootMsg[i+4:i+6] + BootMsg[i+2:i+4] + BootMsg[i:i+2] 
    tmp = "0"*24 + "{:0>8x}".format(BootSize*8) + Msg
    KeyBin = binascii.unhexlify(Key)
    MsgBin = binascii.unhexlify(tmp)
    Cipher = CMAC.new(KeyBin,MsgBin,ciphermod=AES)
    return Cipher.hexdigest().upper()

'''
@description: S32K1xx CSEc MPCompress. 
@param {type}: input and output are hexstring, such as:"000102030405060708090A0B0C0D"
@return: the result 
'''
def CSEC_MPCompress(Msg,IV):
    global BLOCK_SIZE
    MsgBin = binascii.unhexlify(Msg)
    IVBin  = binascii.unhexlify(IV)
    Length = len(MsgBin)
    TotalBlk = (BLOCK_SIZE + Length - 1) // BLOCK_SIZE
    CurKey = IVBin
    for i in range(0,TotalBlk):
        Blk = MsgBin[i*BLOCK_SIZE : (i+1)*BLOCK_SIZE]
        if len(Blk) < BLOCK_SIZE:
            Blk = _PaddingZero(Blk,BLOCK_SIZE)
        Cipher  = AES.new(CurKey, AES.MODE_ECB)
        CurRes = Cipher.encrypt(Blk)
        CurKey = _bxor(_bxor(bytes(CurRes), bytes(Blk)), CurKey)
    Res = str((binascii.hexlify(CurKey)))[2:-1].upper()
    return Res

'''
@description: AES128 ECB encrypto. 
@param {type}: input and output are hexstring, such as:"000102030405060708090A0B0C0D"
@return: the result 
'''
def CSEC_EncryptECB(Key,PlainMsg):
    KeyBin = binascii.unhexlify(Key)
    MsgBin = binascii.unhexlify(PlainMsg)
    Length = len(MsgBin)
    TotalBlk = (BLOCK_SIZE + Length - 1) // BLOCK_SIZE
    Cipher  = AES.new(KeyBin, AES.MODE_ECB)
    Res =''
    for i in range(0,TotalBlk):
        Blk = MsgBin[i*BLOCK_SIZE : (i+1)*BLOCK_SIZE]
        if len(Blk) < BLOCK_SIZE:
            Blk = _PaddingZero(Blk,BLOCK_SIZE)
        Tmp = Cipher.encrypt(Blk)
        Res += str((binascii.hexlify(Tmp)))[2:-1].upper()
    return Res

'''
@description: AES128 ECB decrypto. 
@param {type} 
@return: 
'''
def CSEC_DecryptECB(Key,CiperMsg):
    KeyBin = binascii.unhexlify(Key)
    MsgBin = binascii.unhexlify(CiperMsg)
    Cipher  = AES.new(KeyBin, AES.MODE_ECB)
    PlaintText = Cipher.decrypt(MsgBin)
    return str((binascii.hexlify(PlaintText)))[2:-1].upper()

'''
@description: AES128 CBC encrypto. 
@param {type} 
@return: 
'''
def CSEC_EncryptCBC(Key,PlainMsg,IV):
    KeyBin = binascii.unhexlify(Key)
    MsgBin = binascii.unhexlify(PlainMsg)
    IVBin  = binascii.unhexlify(IV)
    Cipher = AES.new(KeyBin, AES.MODE_CBC,IVBin)
    x = (len(MsgBin) % BLOCK_SIZE)
    if x != 0:
        MsgBin = MsgBin + bytes([0 for i in range(BLOCK_SIZE - x)])
    Res = Cipher.encrypt(MsgBin)
    return str((binascii.hexlify(Res)))[2:-1].upper()
    
'''
@description: AES128 CBC decrypto. 
@param {type} 
@return: 
'''
def CSEC_DecryptCBC(Key,CipherText,IV):
    if len(CipherText)%BLOCK_SIZE != 0:
        return "Error:Input must be multiple 16"
    KeyBin = binascii.unhexlify(Key)
    MsgBin = binascii.unhexlify(CipherText)
    IVBin  = binascii.unhexlify(IV)
    Cipher = AES.new(KeyBin, AES.MODE_CBC, IVBin)
    Res = Cipher.decrypt(MsgBin)
    return str((binascii.hexlify(Res)))[2:-1].upper()

