'''
@Author: yunchuan.wang@nxp.com
@Github: https://github.com/weltry/S32K1xx-CSEc-Tool.git
@LastEditors: yunchuan.wang@nxp.com
@LastEditTime: 2020-07-02 20:14:46
'''

# -*- coding: UTF-8 -*-
import wx
import datetime
import os
import ui
import string

import app
import csec
import utility
import binascii

#config
TotalKeyNum = 20

Warning1 = "Once have been set,will never to be changed !\n Please be very careful to set this option !\n"
Warning2 = "Do you really want to set it ?"

# -----------------------common funcations-------------------------------
'''
@description: 
@param {type} 
@return: 
'''
def UpdateInputLen(Instance, InputTextCtrl, TextCtrlLen,TotalLen=32):
    Textlen = len(getattr(getattr(Instance, InputTextCtrl), "GetValue")())
    if TotalLen == None:
        getattr(getattr(Instance, TextCtrlLen), "SetValue")("{:0>2d}".format(Textlen))
    else:
        getattr(getattr(Instance, TextCtrlLen), "SetValue")("{:0>2d}".format(Textlen)+"/" + str(TotalLen))
    if getattr(getattr(Instance, TextCtrlLen), "BackgroundColour") == "Red":
        setattr(getattr(Instance, TextCtrlLen), "BackgroundColour", "Window")
        getattr(Instance, "Refresh")()

'''
@description: 
@param {type} 
@return: 
'''
def CheckInputLen(Instance, InputTextCtrl,TextCtrlLen,ExpectLen):
    if len(getattr(getattr(Instance, InputTextCtrl), "GetValue")()) != ExpectLen:
        #set the background with red to show error
        setattr(getattr(Instance, TextCtrlLen), "BackgroundColour", "Red") 
        getattr(Instance, "Refresh")()
        return True #Error
    else:
        return False

'''
@description: 
@param {type} 
@return: 
'''
def Validator(Instance,CtrlName,CbkName,Style="Number"):
    Text = getattr(getattr(Instance,CtrlName), "GetValue")()
    Valid = ""
    for ch in Text:
        if Style == "Number":
            if ch.isdigit():
                Valid += ch
        if Style == "HexString":
            if ("0123456789ABCDEFabcdef".find(ch)) != -1:
                Valid += ch
    #disconnect callback avoid multiple call callback function when set the control value .
    getattr(getattr(Instance,CtrlName), "Bind")(wx.EVT_TEXT, None)
    getattr(getattr(Instance,CtrlName), "SetValue")(Valid)
    getattr(getattr(Instance,CtrlName), "Bind")(wx.EVT_TEXT, getattr(Instance,CbkName))

'''
@description: 
@param {type} 
@return: 
'''
def WarningMessageDialog(Text):
    Res = False
    dlg = wx.MessageDialog(None, Text, u"Waring!", wx.YES_NO|wx.ICON_QUESTION)
    if dlg.ShowModal() == wx.ID_YES:
        Res = True
    dlg.Destroy()
    return Res
# -----------------------end of common funcations-------------------------

'''
@description: main frame class
@param {type} 
@return: 
'''
class UI_MainFrame(ui.MainFrame):
    __sub_win__ = None
    def __init__(self, parent, SubWin):
        ui.MainFrame.__init__(self, parent)
        self.icon = wx.Icon('ico.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        self.__sub_win__ = SubWin

#Show key config frame
    def ShowSubWin(self, win):
        self.__sub_win__.Hide()
        self.__sub_win__.Centre()
        self.__sub_win__.Show()
#Hide key config frame
    def OnSetFocus_Cbk(self, win):
        self.__sub_win__.Hide()
#exit system
    def OnClose_Cbk(self, event):
        self.Destroy()
        self.__sub_win__.Destroy()

    def OnMoveEnd_Cbk(self, event):
        self.Refresh()
        
# -----------------------CSEc Init CallBack-------------------------------
# change the choice selection depend on partnum and CSEC enable
    def SetDEFlashChoiceList(self):
        MCU = self.CI_MCU_choice.GetString(self.CI_MCU_choice.GetCurrentSelection())
        CSEC = self.CI_CSEc_checkBox.GetValue()
        self.CI_Partit_choice.Clear()
        self.CI_EEPSize_choice.Clear()
        Choices2 = []
        if (MCU == "S32K116F128") or (MCU == "S32K118F256"):
            Choices1 = [u"0KB DFlash/32KB EFlash", u"8KB DFlash/24KB EFlash"]
            if CSEC == False:
                Choices1 += [u"32KB DFlash/0KB EFlash"]
                Choices2 = [u"0KB EEPROM"]
            Choices2 += [u"2KB EEPROM"]
        if (MCU == "S32K142F256") or (MCU == "S32K144F512") or (MCU == "S32K146F1M"):
            Choices1 = [u"0KB DFlash/64KB EFlash",
                        u"16KB DFlash/48KB EFlash", u"32KB DFlash/32KB EFlash"]
            if CSEC == False:
                Choices1 += [u"64KB DFlash/0KB EFlash"]
                Choices2 = [u"0KB EEPROM"]
            Choices2 += [u"4KB EEPROM"]
        if (MCU == "S32K148F2M"):
            Choices1 = [u"448KB DFlash/64KB EFlash"]
            if CSEC == False:
                Choices1 += [u"512KB DFlash/0KB EFlash"]
                Choices2 = [u"0KB EEPROM"]
            Choices2 += [u"4KB EEPROM"]
        self.CI_AutoLoad_checkBox.Set3StateValue(CSEC)
        self.CI_AutoLoad_checkBox.Enable(not CSEC)
        self.CI_SecureBoot_checkBox.Enable(CSEC)
        self.CI_USFE_checkBox.Enable(CSEC)
        self.CI_CfgKey_button.Enable(CSEC)
        self.CI_CreateInitFW_button.Enable(CSEC)
        self.CI_CreateResetFW_button.Enable(CSEC)
        self.CI_KeyNum_choice.Enable(CSEC)
        self.CI_Partit_choice.SetItems(Choices1)
        self.CI_Partit_choice.SetSelection(0)
        self.CI_EEPSize_choice.SetItems(Choices2)
        self.CI_EEPSize_choice.SetSelection(0)

# MCU choice callback
    def CI_MCU_choice_Cbk(self, event):
        self.SetDEFlashChoiceList()

# CSEc checkbox callback   
    def CI_CSEc_checkBox_Cbk(self, event):
        self.SetDEFlashChoiceList()
        self.CI_SecureBoot_checkBox.SetValue(False)
        self.CI_SecureBoot_checkBox_Cbk(event)

# CSEc checkbos callback
    def CI_SecureBoot_checkBox_Cbk(self, event):
        Enable = self.CI_SecureBoot_checkBox.GetValue()
        self.CI_BootSize_textCtrl.Enable(Enable)
        self.CI_SecureBootMode_choice.Enable(Enable)
        getattr(getattr(getattr(self, "__sub_win__"),"Enable_02"), "SetValue")(Enable)
        getattr(getattr(getattr(self, "__sub_win__"),"Enable_03"), "SetValue")(Enable)
        if Enable:
            self.CI_SecureBootMode_choice_Cbk(event)


    def CI_SecureBootMode_choice_Cbk(self, event):
        if self.CI_SecureBootMode_choice.GetString(self.CI_SecureBootMode_choice.GetCurrentSelection()) \
            == "Strict Sequential Boot Mode":
            if WarningMessageDialog("\"Strict Sequential Boot Mode\"" + Warning1) !=True:
                self.CI_SecureBootMode_choice.SetSelection(0)

    def CI_BootSize_textCtrl_Cbk(self, event):
        Validator(self,"CI_BootSize_textCtrl","CI_BootSize_textCtrl_Cbk")
        if 512000 < (int(self.CI_BootSize_textCtrl.GetValue())):
            self.CI_BootSize_textCtrl.SetValue("512000")

    def CI_Partit_choice_Cbk(self, event):
        Pattit = self.CI_Partit_choice.GetString(self.CI_Partit_choice.GetCurrentSelection())
        if(Pattit == "512KB DFlash:0KB EFlash") or \
          (Pattit == "64KB DFlash:0KB  EFlash") or \
          (Pattit == "32KB DFlash:0KB EFlash"):
            self.CI_EEPSize_choice.SetSelection(0)

    def CI_EEPSize_choice_Cbk(self, event):
        self.CI_Partit_choice_Cbk(event)

    def CI_USFE_checkBox_Cbk(self, event):
        USFE = self.CI_USFE_checkBox.GetValue()
        for ID in range(4, TotalKeyNum+1): #User key01 ~ User Key17
            getattr(getattr(getattr(self, "__sub_win__"),"VerfiyOnly_"+"{:0>2d}".format(ID)), "Enable")(USFE)

    # Config key buttons callback
    def CI_CfgKey_button_Cbk(self, event):
        self.ShowSubWin(self.__sub_win__)

    # output text
    def CI_OutputInf(self, text):
        Time = datetime.datetime.now().strftime("%T")
        self.CI_Output_textCtrl.write(Time+": \n"+text+"\n")

    # transfer to MCU API parameter
    __PartitionCodeDic__ = {"0KB DFlash/32KB EFlash":  0x3, "8KB DFlash/24KB EFlash":  0x9, "32KB DFlash/0KB EFlash": 0x0,
                            "0KB DFlash/64KB EFlash":  0x4, "16KB DFlash/48KB EFlash": 0xA, "32KB DFlash/32KB EFlash": 0x3, "64KB DFlash/0KB EFlash": 0x0,
                            "512KB DFlash/0KB EFlash": 0x0, "448KB DFlash/64KB EFlash": 0x4}
    __EepSizeCodeDic__ = {"0KB EEPROM": 0x0, "2KB EEPROM": 0x3, "4KB EEPROM": 0x2}
    __KeyNumCodeDic__  = {"0 Key": 0,     "6 Keys": 0x01,
                         "12 Keys": 0x02, "24 Keys": 0x03}
    __SecureBootMode__ = {"Strict Sequential Boot Mode":0x01,"Sequential Boot Mode":0x02,"Parallel Boot Mode":0x03}

    def CI_CreatPartitCode_button_Cbk(self, event):
        MCU = self.CI_MCU_choice.GetString(self.CI_MCU_choice.GetCurrentSelection())
        EepSizeCode   = self.__EepSizeCodeDic__[self.CI_EEPSize_choice.GetString(self.CI_EEPSize_choice.GetCurrentSelection())]
        PartitionCode = self.__PartitionCodeDic__[self.CI_Partit_choice.GetString(self.CI_Partit_choice.GetCurrentSelection())]
        KeyNumCode    = self.__KeyNumCodeDic__[self.CI_KeyNum_choice.GetString(self.CI_KeyNum_choice.GetCurrentSelection())]
        USFE     = "1" if (self.CI_USFE_checkBox.GetValue() == True)     else "0"
        AutoLoad = "1" if (self.CI_AutoLoad_checkBox.GetValue() == True) else "0"
        Text = "MCU: " + MCU + "\n" \
            "uEEEDataSizeCode: " + "0x{:0>2x}".format(EepSizeCode)   + "\n" + \
            "uDEPartitionCode: " + "0x{:0>2x}".format(PartitionCode) + "\n" + \
            "uCSEcKeySize: "     + "0x{:0>2x}".format(KeyNumCode)    + "\n" + \
            "uSFE: " + USFE + "\n" + \
            "flexRamEnableLoadEEEData: " + AutoLoad + "\n"
        self.CI_OutputInf(Text)

    def CI_CreateResetFW_button_Cbk(self, event):
        self.CreateFirmware("Reset")

    def CI_CreateInitFW_button_Cbk(self, event):
        self.CreateFirmware("Init")

    def CreateFirmware(self, InitOrReset):
        CSEcCfg = {}
        dlg = wx.DirDialog(self, u"Chose path", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath() 
            # get CSEc config
            CSEcCfg['MCU']           = self.CI_MCU_choice.GetString(self.CI_MCU_choice.GetCurrentSelection())
            CSEcCfg['EepSizeCode']   = self.__EepSizeCodeDic__[self.CI_EEPSize_choice.GetString(self.CI_EEPSize_choice.GetCurrentSelection())]
            CSEcCfg['PartitionCode'] = self.__PartitionCodeDic__[self.CI_Partit_choice.GetString(self.CI_Partit_choice.GetCurrentSelection())]
            CSEcCfg['KeyNumCode']    = self.__KeyNumCodeDic__[self.CI_KeyNum_choice.GetString(self.CI_KeyNum_choice.GetCurrentSelection())]
            CSEcCfg['USFE']          = self.CI_USFE_checkBox.GetValue()
            CSEcCfg['AutoLoad']      = self.CI_AutoLoad_checkBox.GetValue()
            CSEcCfg['SecureBoot']    = self.CI_SecureBoot_checkBox.GetValue()
            CSEcCfg['SecureBootMode']= self.__SecureBootMode__[self.CI_SecureBootMode_choice.GetString(self.CI_SecureBootMode_choice.GetCurrentSelection())]
            CSEcCfg['BootSize']      = int(self.CI_BootSize_textCtrl.GetValue())
            CSEcCfg['CSEc']          = self.CI_CSEc_checkBox.GetValue()
            CSEcCfg['InitOrReset']   = InitOrReset
            if (CSEcCfg['BootSize']%4 != 0) and (CSEcCfg['SecureBoot'] == True):
                self.CI_OutputInf("Error: Boot size must be 4 bytes aligned !\n")
            else:
                self.CI_OutputInf(app.CreatFirmware(path, CSEcCfg))
        else:
            self.CI_OutputInf("Canceled!\n")
        dlg.Destroy()
# -------------------End Of CSEc Init CallBack-------------------------------

# ----------------------------AES Tool CallBack-------------------------------
    def AT_OutputInf(self,text):
        Time = datetime.datetime.now().strftime("%T")
        self.AT_Output_textCtrl.write(Time+": \n"+text+"\n")

    # AES tool, AES mode choice
    def AT_Mode_choice_Cbk(self, event):
        mode = self.AT_Mode_choice.GetString(
            self.AT_Mode_choice.GetCurrentSelection())
        if(mode == "CBC") or (mode == "ECB"):
            self.AT_Action_choice.Enable(True)
        else:
            self.AT_Action_choice.Enable(False)
        if (mode == "MPCompress"):
            self.AT_Key_textCtrl.Enable(False)
            self.AT_KeyLen_textCtrl.Enable(False)
        else:
            self.AT_Key_textCtrl.Enable(True)
            self.AT_KeyLen_textCtrl.Enable(True)
        if (mode == "CBC") or (mode == "MPCompress"):
            self.AT_IV_textCtrl.Enable(True)
            self.AT_IVLen_textCtrl.Enable(True)
        else:
            self.AT_IV_textCtrl.Enable(False)
            self.AT_IVLen_textCtrl.Enable(False)

    def AT_Input_text_Cbk(self, event):
        Validator(self,"AT_Input_text","AT_Input_text_Cbk","HexString")
        UpdateInputLen(self, "AT_Input_text", "AT_InputLen_text",None)

    def AT_Key_textCtrl_Cbk(self, event):
        Validator(self,"AT_Key_textCtrl","AT_Key_textCtrl_Cbk","HexString")
        UpdateInputLen(self, "AT_Key_textCtrl", "AT_KeyLen_textCtrl",32)

    def AT_IV_textCtrl_Cbk(self, event):
        Validator(self,"AT_IV_textCtrl","AT_IV_textCtrl_Cbk","HexString")
        UpdateInputLen(self, "AT_IV_textCtrl", "AT_IVLen_textCtrl",32)

    def AT_LoadBin_button_Cbk(self, event):
        dlg = wx.FileDialog(self,message=u"Chose File",
                            wildcard = "(*.bin)|*.bin|" "All files (*.*)|*.*",
                            defaultDir=os.getcwd(),
                            defaultFile=".bin",
                            style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            File = dlg.GetPath()
            try:
                f = open(File,"rb")
                FileString = f.read()
                FileString = str(binascii.b2a_hex(FileString))[2:-1]
                FileString = FileString.strip().replace('\n', '').replace('\r', '').replace(' ', '').upper()
                Res = "Lode File Successed!\n"
                self.AT_Input_text.SetValue(FileString)
                self.AT_Input_text_Cbk(event)
                f.close()
            except IOError:
                Res = "Open File Failed!\n"
            self.AT_OutputInf(Res)
        dlg.Destroy()

    def AT_Compute_button_Cbk(self, event):
        Error = False
        Res = "Error"
        # Mode
        Mode = self.AT_Mode_choice.GetString(self.AT_Mode_choice.GetCurrentSelection())
        # Action
        Action = self.AT_Action_choice.GetString(self.AT_Action_choice.GetCurrentSelection())
        # input msg and length
        Msg = str(self.AT_Input_text.GetValue())
        InputLen = int(str(self.AT_InputLen_text.GetValue()))
        Error = Error or CheckInputLen(self, "AT_Input_text", "AT_InputLen_text",InputLen+InputLen % 2)
        # Input Key
        Key = str(self.AT_Key_textCtrl.GetValue())
        Error = Error or CheckInputLen(self, "AT_Key_textCtrl","AT_KeyLen_textCtrl",32)
        if Mode == "CBC" or (Mode == "MPCompress"):
            # input IV
            IV = str(self.AT_IV_textCtrl.GetValue())
            Error = Error or CheckInputLen(self, "AT_IV_textCtrl","AT_IVLen_textCtrl",32)
        if Error == True:
            Res = "Input Error"
        else:
            if (Mode == "ECB") and (Action == "Crypto"):
                Res = csec.CSEC_EncryptECB(Key,Msg)
            if (Mode == "ECB") and (Action == "Decrypto"):
                Res = csec.CSEC_DecryptECB(Key,Msg)
            if (Mode == "CBC") and (Action == "Crypto"):
                Res = csec.CSEC_EncryptCBC(Key,Msg,IV)
            if (Mode == "CBC") and (Action == "Decrypto"):
                Res = csec.CSEC_DecryptCBC(Key,Msg,IV)
            if Mode == "MPCompress":
                Res = csec.CSEC_MPCompress(Msg,IV)
            if Mode == "CMAC":
                Res = csec.CSEC_GenerateMAC(Key,Msg)
            if Mode == "BootMAC":
                Res = csec.CSEC_GenerateBootMAC(Key,Msg,int(InputLen/2))
        self.AT_OutputInf(Res)
# -----------------------End Of AES Tool CallBack-------------------------------

# -----------------------Calculate M1~M5 Toll CallBack-------------------------------
    def CM_OutputInf(self,text):
        Time = datetime.datetime.now().strftime("%T")
        self.CM_Output_textCtrl.write(Time+": \n"+text+"\n")

    def CM_AuthKey_textCtrl_Cbk(self, event):
        Validator(self,"CM_AuthKey_textCtrl","CM_AuthKey_textCtrl_Cbk","HexString")
        UpdateInputLen(self, "CM_AuthKey_textCtrl", "CM_AuthKeyLen_textCtrl",32)

    def CM_NewKey_textCtrl_Cbk(self, event):
        Validator(self,"CM_NewKey_textCtrl","CM_NewKey_textCtrl_Cbk","HexString")
        UpdateInputLen(self, "CM_NewKey_textCtrl", "CM_NewKeyLen_textCtrl",32)

    def CM_WRITE_PROT_checkBox_Cbk(self, event):
        Enable = self.CM_WRITE_PROT_checkBox.GetValue()
        if Enable:
            if WarningMessageDialog(" \"WRITE_PROT\"" + Warning1) == False:
                self.CM_WRITE_PROT_checkBox.SetValue(False)

    def CM_UID_textCtrl_Cbk(self, event):
        Validator(self,"CM_UID_textCtrl","CM_UID_textCtrl_Cbk","HexString")
        UpdateInputLen(self, "CM_UID_textCtrl", "CM_UIDLen_textCtrl",30)

    def CM_Counter_textCtrl_Cbk(self, event):
        Validator(self,"CM_Counter_textCtrl","CM_Counter_textCtrl_Cbk","Number")

    def CM_Cal_button_Cbk(self, event):
        KeyIdToKeyNameDic = {"MASTER_ECU_KEY":"01", "BOOT_MAC_KEY":"02", "BOOT_MAC":"03",     "USER_KEY_01":"04", "USER_KEY_02":"05",\
                             "USER_KEY_03":"06",    "USER_KEY_04":"07",  "USER_KEY_05":"08",  "USER_KEY_06":"09", "USER_KEY_07":"0A",\
                             "USER_KEY_08":"0B",    "USER_KEY_09":"0C",  "USER_KEY_10":"0D",  "USER_KEY_11":"14", "USER_KEY_12":"15",\
                             "USER_KEY_13":"16",    "USER_KEY_14":"17",  "USER_KEY_15":"18",  "USER_KEY_16":"19", "USER_KEY_17":"1A"}
        Error = False
        Res = "Error"
        #AuthKey
        AuthKey = str(self.CM_AuthKey_textCtrl.GetValue()).upper()
        Error   = Error or CheckInputLen(self, "CM_AuthKey_textCtrl", "AuthKeyLen_textCtrl",32)
        #NewKey
        NewKey = str(self.CM_NewKey_textCtrl.GetValue()).upper()
        Error  = Error or CheckInputLen(self, "CM_NewKey_textCtrl", "CM_NewKeyLen_textCtrl",32)
        #UID
        UID   = str(self.CM_UID_textCtrl.GetValue()).upper()
        Error = Error or CheckInputLen(self, "CM_UID_textCtrl","CM_UIDLen_textCtrl", 30)
        #counter
        Counter = int(self.CM_Counter_textCtrl.GetValue())
        Error   = Error or (not str(Counter).isdigit())
        Counter = "{:0>8x}".format((Counter))
        #AuthKey ID
        AuthKeyID = KeyIdToKeyNameDic[self.CM_AuthKeyID_choice.GetString(self.CM_AuthKeyID_choice.GetCurrentSelection())]
        #NewKeyID
        NewKeyID = KeyIdToKeyNameDic[self.CM_NewKeyID_choice.GetString(self.CM_NewKeyID_choice.GetCurrentSelection())]
        #Flags
        Flags = 0x00
        Flags = Flags | (int(self.CM_WRITE_PROT_checkBox.GetValue()) << 7)
        Flags = Flags | (int(self.CM_BOOT_PROT_checkBox.GetValue())  << 6)
        Flags = Flags | (int(self.CM_DEBUG_PROT_checkBox.GetValue()) << 5)
        Flags = Flags | (int(self.CM_KEY_USAGE_checkBox.GetValue())  << 4)
        Flags = Flags | (int(self.CM_WILD_CARD_checkBox.GetValue())  << 3)
        Flags = Flags | (int(self.CM_VERFIY_ONLY_checkBox87.GetValue()) << 2)
        Flags = "{:0>2x}".format(Flags)
        if Error == True:
            Res = "Input Error"
        else:
            Res = utility.CalculateM1ToM5(AuthKey, NewKey, AuthKeyID, NewKeyID, Counter, str(Flags), UID)
            Res = "M1: "  + Res["M1"] + "\nM2: " + Res["M2"] + "\nM3: " + Res["M3"] \
              + "\nM4: "  + Res["M4"] + "\nM5: " + Res["M5"] + "\n"
        self.CM_OutputInf(Res)
# -------------------End Of Calculate M1~M5 Toll CallBack----------------------------

'''
@description: Key configuration frame class(as sub-windows for main windows)
@param {type} 
@return: 
'''
class UI_CfgKeyFrame(ui.CfgKeyFrame):
    __CSEcInitCls__ = None
    __KeyInputTextNameAndID__ = {}
    def __init__(self, parent):
        ui.CfgKeyFrame.__init__(self, parent)
        self.icon = wx.Icon('ico.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)
        # get key input text id and connect to their name
        # there also can use lamanda when connect callback
        for i in range(1, TotalKeyNum+1):
            InstanceNum = "{:0>2d}".format(i)
            ID = str(getattr(getattr(self, "KeyValue_"+InstanceNum), "GetId")())
            self.__KeyInputTextNameAndID__[ID] = InstanceNum

    def OnClose_Cbk(self, event):
        self.Hide()

    def OnMoveEnd_Cbk(self, event):
        self.Refresh()

    def ImportKey_Cbk(self, event):
        # check input is legal
        for i in range(1, TotalKeyNum+1):
            Num = "{:0>2d}".format(i)
            if (getattr(getattr(self, "Enable_"+Num), "GetValue")() == True):
                Error = CheckInputLen(self, "KeyValue_"+Num,"KeyValueLen_"+Num,32)
        if(Error == True):
            return
        KeyInfList = []
        Warn = False
        for i in range(1, TotalKeyNum+1):
            TmpDic = {}
            Flags = 0x00
            Num = "{:0>2d}".format(i)
            ID = (i+6) if (i > 13) else (i)
            TmpDic["KeyID"] = ID  # key ID 1~13d 20~26d
            TmpDic["Enable"] = getattr(getattr(self, "Enable_"+Num), "GetValue")()
            if TmpDic["Enable"] == True:
                TmpDic["KeyValue"] = getattr(getattr(self, "KeyValue_"+Num), "GetValue")().upper()
                Flags = Flags | ((getattr(getattr(self, "WriteProt_"+Num), "GetValue")()) << 7)
                Flags = Flags | ((getattr(getattr(self, "BootProt_" +Num), "GetValue")()) << 6)
                Flags = Flags | ((getattr(getattr(self, "DebugProt_"+Num), "GetValue")()) << 5)
                Flags = Flags | ((getattr(getattr(self, "DebugProt_"+Num), "GetValue")()) << 4)
                Flags = Flags | ((getattr(getattr(self, "WildCard_" +Num), "GetValue")()) << 3)
                Flags = Flags | ((getattr(getattr(self, "VerfiyOnly_"+Num),"GetValue")()) << 2)
                if (Flags & 0x80) == 0x80:
                    Warn = True
            else:
                TmpDic["KeyValue"] = "FF"*16
            TmpDic["Flags"] = Flags
            TmpDic["Counter"] = "01"  # conter always 1 in init
            KeyInfList.append(TmpDic)
        if Warn == True:
            if WarningMessageDialog("\"WriteProt\" "+ Warning1+Warning2) == False:
                return
        app.ImportKey(KeyInfList)
        self.OnClose_Cbk(wx._core.CloseEvent)

    def KeyValue_xx_Cbk(self, event):
        Num = self.__KeyInputTextNameAndID__[str(event.GetId())]  # num:01~20
        Validator(self,"KeyValue_" + Num,"KeyValue_xx_Cbk","HexString")
        UpdateInputLen(self, "KeyValue_" + Num, "KeyValueLen_" + Num,32)
