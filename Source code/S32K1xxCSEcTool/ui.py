# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Dec  4 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"S32K1xx CSEC Tool", pos = wx.DefaultPosition, size = wx.Size( 1079,543 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		MainSizer = wx.BoxSizer( wx.HORIZONTAL )

		CSECInitSizer = wx.BoxSizer( wx.VERTICAL )

		self.CSECInitTitleText = wx.StaticText( self, wx.ID_ANY, u"CSEC Init", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.CSECInitTitleText.Wrap( -1 )

		self.CSECInitTitleText.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.CSECInitTitleText.SetBackgroundColour( wx.Colour( 255, 173, 0 ) )

		CSECInitSizer.Add( self.CSECInitTitleText, 0, wx.BOTTOM|wx.EXPAND, 5 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		CI_MCU_choiceChoices = [ u"S32K116F128", u"S32K118F256", u"S32K142F256", u"S32K144F512", u"S32K146F1M", u"S32K148F2M" ]
		self.CI_MCU_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), CI_MCU_choiceChoices, 0, wx.DefaultValidator, u"PartNum" )
		self.CI_MCU_choice.SetSelection( 3 )
		gSizer2.Add( self.CI_MCU_choice, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.CI_CSEc_checkBox = wx.CheckBox( self, wx.ID_ANY, u"CSEC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CI_CSEc_checkBox.SetValue(True)
		bSizer3.Add( self.CI_CSEc_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.CI_SecureBoot_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Secure Boot", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.CI_SecureBoot_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )


		gSizer2.Add( bSizer3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		CI_SecureBootMode_choiceChoices = [ u"Sequential Boot Mode", u"Strict Sequential Boot Mode", u"Parallel Boot Mode" ]
		self.CI_SecureBootMode_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), CI_SecureBootMode_choiceChoices, 0 )
		self.CI_SecureBootMode_choice.SetSelection( 0 )
		self.CI_SecureBootMode_choice.Enable( False )
		self.CI_SecureBootMode_choice.SetToolTip( u"Secuse boot mode" )

		gSizer2.Add( self.CI_SecureBootMode_choice, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.CI_BootSize_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"16384", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.CI_BootSize_textCtrl.SetMaxLength( 6 )
		self.CI_BootSize_textCtrl.Enable( False )
		self.CI_BootSize_textCtrl.SetToolTip( u"Boot size(byte)" )

		bSizer4.Add( self.CI_BootSize_textCtrl, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Byte Boot Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer4.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		gSizer2.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		CI_Partit_choiceChoices = [ u"0KB DFlash/64KB EFlash", u"32KB DFlash/32KB EFlash", u"16KB DFlash/48KB EFlash" ]
		self.CI_Partit_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), CI_Partit_choiceChoices, 0 )
		self.CI_Partit_choice.SetSelection( 0 )
		self.CI_Partit_choice.SetToolTip( u"DFlash/EFlash partition" )

		gSizer2.Add( self.CI_Partit_choice, 1, wx.ALL|wx.FIXED_MINSIZE|wx.RESERVE_SPACE_EVEN_IF_HIDDEN|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		CI_EEPSize_choiceChoices = [ u"0KB EEPROM", u"4KB EEPROM" ]
		self.CI_EEPSize_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), CI_EEPSize_choiceChoices, 0 )
		self.CI_EEPSize_choice.SetSelection( 1 )
		self.CI_EEPSize_choice.SetToolTip( u"EEPROM size" )

		gSizer2.Add( self.CI_EEPSize_choice, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		CI_KeyNum_choiceChoices = [ u"0 Key", u"6 Keys", u"12 Keys", u"24 Keys" ]
		self.CI_KeyNum_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 140,-1 ), CI_KeyNum_choiceChoices, 0 )
		self.CI_KeyNum_choice.SetSelection( 3 )
		self.CI_KeyNum_choice.SetToolTip( u"Maximum number of keys" )

		gSizer2.Add( self.CI_KeyNum_choice, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.CI_AutoLoad_checkBox = wx.CheckBox( self, wx.ID_ANY, u"Auto load", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CI_AutoLoad_checkBox.SetValue(True)
		self.CI_AutoLoad_checkBox.SetToolTip( u"Auto load EFlash date to FlexRAM" )

		bSizer5.Add( self.CI_AutoLoad_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.CI_USFE_checkBox = wx.CheckBox( self, wx.ID_ANY, u"USFE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CI_USFE_checkBox.SetValue(True)
		self.CI_USFE_checkBox.SetToolTip( u"uSFE Security Flag Extension" )

		bSizer5.Add( self.CI_USFE_checkBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		gSizer2.Add( bSizer5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CI_CfgKey_button = wx.Button( self, wx.ID_ANY, u"Config Keys", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gSizer2.Add( self.CI_CfgKey_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.CI_CreateInitFW_button = wx.Button( self, wx.ID_ANY, u"Create Initial Firmware", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gSizer2.Add( self.CI_CreateInitFW_button, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.CI_CreatPartitCode_button = wx.Button( self, wx.ID_ANY, u"Create Partition Code", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gSizer2.Add( self.CI_CreatPartitCode_button, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.CI_CreateResetFW_button = wx.Button( self, wx.ID_ANY, u"Create Reset Firmware", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		gSizer2.Add( self.CI_CreateResetFW_button, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )


		CSECInitSizer.Add( bSizer1, 1, wx.EXPAND, 5 )

		self.CI_Output_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,180 ), wx.TE_MULTILINE|wx.VSCROLL )
		CSECInitSizer.Add( self.CI_Output_textCtrl, 0, wx.ALL|wx.EXPAND, 5 )


		MainSizer.Add( CSECInitSizer, 1, wx.EXPAND, 5 )

		AESToolSizer = wx.BoxSizer( wx.VERTICAL )

		self.AESToolTitleText = wx.StaticText( self, wx.ID_ANY, u"AES Tool", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.AESToolTitleText.Wrap( -1 )

		self.AESToolTitleText.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.AESToolTitleText.SetBackgroundColour( wx.Colour( 125, 178, 219 ) )

		AESToolSizer.Add( self.AESToolTitleText, 0, wx.EXPAND|wx.BOTTOM, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Input", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer6.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.AT_Input_text = wx.TextCtrl( self, wx.ID_ANY, u"000102030405060708090A0B0C0D0E0F", wx.DefaultPosition, wx.Size( 245,-1 ), 0 )
		bSizer6.Add( self.AT_Input_text, 1, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.AT_InputLen_text = wx.TextCtrl( self, wx.ID_ANY, u"32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		bSizer6.Add( self.AT_InputLen_text, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		AESToolSizer.Add( bSizer6, 1, wx.EXPAND, 5 )

		self.AT_LoadBin_button = wx.Button( self, wx.ID_ANY, u"Load Bin File", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.AT_LoadBin_button.SetToolTip( u"Only support Bin file" )

		AESToolSizer.Add( self.AT_LoadBin_button, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.AT_Key_staticText = wx.StaticText( self, wx.ID_ANY, u" Key ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AT_Key_staticText.Wrap( -1 )

		bSizer7.Add( self.AT_Key_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.AT_Key_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"000102030405060708090A0B0C0D0E0F", wx.DefaultPosition, wx.Size( 245,-1 ), 0 )
		self.AT_Key_textCtrl.SetMaxLength( 32 )
		bSizer7.Add( self.AT_Key_textCtrl, 1, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.AT_KeyLen_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"32/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		bSizer7.Add( self.AT_KeyLen_textCtrl, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		AESToolSizer.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.AT_IV_staticText = wx.StaticText( self, wx.ID_ANY, u"  IV  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AT_IV_staticText.Wrap( -1 )

		bSizer8.Add( self.AT_IV_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.AT_IV_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"00000000000000000000000000000000", wx.DefaultPosition, wx.Size( 245,-1 ), 0 )
		self.AT_IV_textCtrl.SetMaxLength( 32 )
		bSizer8.Add( self.AT_IV_textCtrl, 1, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.AT_IVLen_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"32/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		bSizer8.Add( self.AT_IVLen_textCtrl, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		AESToolSizer.Add( bSizer8, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		AT_Mode_choiceChoices = [ u"ECB", u"CBC", u"CMAC", u"MPCompress", u"BootMAC" ]
		self.AT_Mode_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), AT_Mode_choiceChoices, 0 )
		self.AT_Mode_choice.SetSelection( 0 )
		bSizer9.Add( self.AT_Mode_choice, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		AT_Action_choiceChoices = [ u"Crypto", u"Decrypto" ]
		self.AT_Action_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, AT_Action_choiceChoices, 0 )
		self.AT_Action_choice.SetSelection( 0 )
		bSizer9.Add( self.AT_Action_choice, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.AT_Compute_button = wx.Button( self, wx.ID_ANY, u"Calculate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.AT_Compute_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		AESToolSizer.Add( bSizer9, 1, wx.EXPAND, 5 )

		self.AT_Output_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,180 ), wx.TE_MULTILINE|wx.VSCROLL )
		AESToolSizer.Add( self.AT_Output_textCtrl, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )


		MainSizer.Add( AESToolSizer, 1, wx.EXPAND, 5 )

		CalMSizer = wx.BoxSizer( wx.VERTICAL )

		self.CalMTitle_staticText = wx.StaticText( self, wx.ID_ANY, u"Calculate M", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.CalMTitle_staticText.Wrap( -1 )

		self.CalMTitle_staticText.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.CalMTitle_staticText.SetBackgroundColour( wx.Colour( 199, 210, 45 ) )

		CalMSizer.Add( self.CalMTitle_staticText, 0, wx.EXPAND|wx.BOTTOM, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.CM_AuthKey_staticText = wx.StaticText( self, wx.ID_ANY, u"AuthKey", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CM_AuthKey_staticText.Wrap( -1 )

		bSizer10.Add( self.CM_AuthKey_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CM_AuthKey_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", wx.DefaultPosition, wx.Size( 245,-1 ), 0 )
		self.CM_AuthKey_textCtrl.SetMaxLength( 32 )
		bSizer10.Add( self.CM_AuthKey_textCtrl, 1, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CM_AuthKeyLen_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"32/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		bSizer10.Add( self.CM_AuthKeyLen_textCtrl, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		CalMSizer.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.CM_NewKey_staticText = wx.StaticText( self, wx.ID_ANY, u" NewKey", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CM_NewKey_staticText.Wrap( -1 )

		bSizer11.Add( self.CM_NewKey_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CM_NewKey_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"000102030405060708090A0B0C0D0E0F", wx.DefaultPosition, wx.Size( 245,-1 ), 0 )
		self.CM_NewKey_textCtrl.SetMaxLength( 32 )
		bSizer11.Add( self.CM_NewKey_textCtrl, 1, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CM_NewKeyLen_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"32/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		bSizer11.Add( self.CM_NewKeyLen_textCtrl, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		CalMSizer.Add( bSizer11, 1, wx.EXPAND, 5 )

		gSizer12 = wx.GridSizer( 2, 3, 0, 0 )

		self.CM_WRITE_PROT_checkBox = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.CM_WRITE_PROT_checkBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CM_BOOT_PROT_checkBox = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.CM_BOOT_PROT_checkBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CM_DEBUG_PROT_checkBox = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.CM_DEBUG_PROT_checkBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CM_KEY_USAGE_checkBox = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.CM_KEY_USAGE_checkBox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.CM_WILD_CARD_checkBox = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.CM_WILD_CARD_checkBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CM_VERFIY_ONLY_checkBox87 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.CM_VERFIY_ONLY_checkBox87, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		CalMSizer.Add( gSizer12, 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.CM_UID_staticText = wx.StaticText( self, wx.ID_ANY, u"      UID   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CM_UID_staticText.Wrap( -1 )

		bSizer13.Add( self.CM_UID_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CM_UID_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"000000000000000000000000000000", wx.DefaultPosition, wx.Size( 245,-1 ), 0 )
		self.CM_UID_textCtrl.SetMaxLength( 30 )
		bSizer13.Add( self.CM_UID_textCtrl, 1, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CM_UIDLen_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"30/30", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		self.CM_UIDLen_textCtrl.SetMaxLength( 5 )
		bSizer13.Add( self.CM_UIDLen_textCtrl, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


		CalMSizer.Add( bSizer13, 1, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.CM_AuthKeyID_staticText = wx.StaticText( self, wx.ID_ANY, u"AuthKeyID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CM_AuthKeyID_staticText.Wrap( -1 )

		bSizer14.Add( self.CM_AuthKeyID_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		CM_AuthKeyID_choiceChoices = [ u"MASTER_ECU_KEY", u"BOOT_MAC_KEY", u"BOOT_MAC", u"USER_KEY_01", u"USER_KEY_02", u"USER_KEY_03", u"USER_KEY_04", u"USER_KEY_05", u"USER_KEY_06", u"USER_KEY_07", u"USER_KEY_08", u"USER_KEY_08", u"USER_KEY_10", u"USER_KEY_11", u"USER_KEY_12", u"USER_KEY_13", u"USER_KEY_14", u"USER_KEY_15", u"USER_KEY_16", u"USER_KEY_17", u"USER_KEY_16", u"USER_KEY_09", u"USER_KEY_10" ]
		self.CM_AuthKeyID_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, CM_AuthKeyID_choiceChoices, 0 )
		self.CM_AuthKeyID_choice.SetSelection( 0 )
		bSizer14.Add( self.CM_AuthKeyID_choice, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.CM_Counter_staticText = wx.StaticText( self, wx.ID_ANY, u"Counter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CM_Counter_staticText.Wrap( -1 )

		bSizer14.Add( self.CM_Counter_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.CM_Counter_textCtrl = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 65,-1 ), 0 )
		self.CM_Counter_textCtrl.SetMaxLength( 8 )
		bSizer14.Add( self.CM_Counter_textCtrl, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )


		CalMSizer.Add( bSizer14, 1, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.CM_NewKeyID_staticText = wx.StaticText( self, wx.ID_ANY, u"NewKeyID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CM_NewKeyID_staticText.Wrap( -1 )

		bSizer15.Add( self.CM_NewKeyID_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		CM_NewKeyID_choiceChoices = [ u"MASTER_ECU_KEY", u"BOOT_MAC_KEY", u"BOOT_MAC", u"USER_KEY_01", u"USER_KEY_02", u"USER_KEY_03", u"USER_KEY_04", u"USER_KEY_05", u"USER_KEY_06", u"USER_KEY_07", u"USER_KEY_08", u"USER_KEY_08", u"USER_KEY_10", u"USER_KEY_11", u"USER_KEY_12", u"USER_KEY_13", u"USER_KEY_14", u"USER_KEY_15", u"USER_KEY_16", u"USER_KEY_17", u"USER_KEY_16", u"USER_KEY_09", u"USER_KEY_10" ]
		self.CM_NewKeyID_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, CM_NewKeyID_choiceChoices, 0 )
		self.CM_NewKeyID_choice.SetSelection( 0 )
		bSizer15.Add( self.CM_NewKeyID_choice, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.CM_Cal_button = wx.Button( self, wx.ID_ANY, u"Calculate", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer15.Add( self.CM_Cal_button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		CalMSizer.Add( bSizer15, 1, wx.EXPAND, 5 )

		self.CM_Output_textCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,180 ), wx.TE_MULTILINE|wx.VSCROLL )
		CalMSizer.Add( self.CM_Output_textCtrl, 0, wx.ALL|wx.EXPAND, 5 )


		MainSizer.Add( CalMSizer, 1, wx.EXPAND, 5 )


		self.SetSizer( MainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose_Cbk )
		self.Bind( wx.EVT_MOVE_END, self.OnMoveEnd_Cbk )
		self.Bind( wx.EVT_SET_FOCUS, self.OnSetFocus_Cbk )
		self.CI_MCU_choice.Bind( wx.EVT_CHOICE, self.CI_MCU_choice_Cbk )
		self.CI_CSEc_checkBox.Bind( wx.EVT_CHECKBOX, self.CI_CSEc_checkBox_Cbk )
		self.CI_SecureBoot_checkBox.Bind( wx.EVT_CHECKBOX, self.CI_SecureBoot_checkBox_Cbk )
		self.CI_SecureBootMode_choice.Bind( wx.EVT_CHOICE, self.CI_SecureBootMode_choice_Cbk )
		self.CI_BootSize_textCtrl.Bind( wx.EVT_TEXT, self.CI_BootSize_textCtrl_Cbk )
		self.CI_Partit_choice.Bind( wx.EVT_CHOICE, self.CI_Partit_choice_Cbk )
		self.CI_EEPSize_choice.Bind( wx.EVT_CHOICE, self.CI_EEPSize_choice_Cbk )
		self.CI_USFE_checkBox.Bind( wx.EVT_CHECKBOX, self.CI_USFE_checkBox_Cbk )
		self.CI_CfgKey_button.Bind( wx.EVT_BUTTON, self.CI_CfgKey_button_Cbk )
		self.CI_CreateInitFW_button.Bind( wx.EVT_BUTTON, self.CI_CreateInitFW_button_Cbk )
		self.CI_CreatPartitCode_button.Bind( wx.EVT_BUTTON, self.CI_CreatPartitCode_button_Cbk )
		self.CI_CreateResetFW_button.Bind( wx.EVT_BUTTON, self.CI_CreateResetFW_button_Cbk )
		self.AT_Input_text.Bind( wx.EVT_TEXT, self.AT_Input_text_Cbk )
		self.AT_LoadBin_button.Bind( wx.EVT_BUTTON, self.AT_LoadBin_button_Cbk )
		self.AT_Key_textCtrl.Bind( wx.EVT_TEXT, self.AT_Key_textCtrl_Cbk )
		self.AT_IV_textCtrl.Bind( wx.EVT_TEXT, self.AT_IV_textCtrl_Cbk )
		self.AT_Mode_choice.Bind( wx.EVT_CHOICE, self.AT_Mode_choice_Cbk )
		self.AT_Compute_button.Bind( wx.EVT_BUTTON, self.AT_Compute_button_Cbk )
		self.CM_AuthKey_textCtrl.Bind( wx.EVT_TEXT, self.CM_AuthKey_textCtrl_Cbk )
		self.CM_NewKey_textCtrl.Bind( wx.EVT_TEXT, self.CM_NewKey_textCtrl_Cbk )
		self.CM_WRITE_PROT_checkBox.Bind( wx.EVT_CHECKBOX, self.CM_WRITE_PROT_checkBox_Cbk )
		self.CM_UID_textCtrl.Bind( wx.EVT_TEXT, self.CM_UID_textCtrl_Cbk )
		self.CM_Counter_textCtrl.Bind( wx.EVT_TEXT, self.CM_Counter_textCtrl_Cbk )
		self.CM_Cal_button.Bind( wx.EVT_BUTTON, self.CM_Cal_button_Cbk )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClose_Cbk( self, event ):
		event.Skip()

	def OnMoveEnd_Cbk( self, event ):
		event.Skip()

	def OnSetFocus_Cbk( self, event ):
		event.Skip()

	def CI_MCU_choice_Cbk( self, event ):
		event.Skip()

	def CI_CSEc_checkBox_Cbk( self, event ):
		event.Skip()

	def CI_SecureBoot_checkBox_Cbk( self, event ):
		event.Skip()

	def CI_SecureBootMode_choice_Cbk( self, event ):
		event.Skip()

	def CI_BootSize_textCtrl_Cbk( self, event ):
		event.Skip()

	def CI_Partit_choice_Cbk( self, event ):
		event.Skip()

	def CI_EEPSize_choice_Cbk( self, event ):
		event.Skip()

	def CI_USFE_checkBox_Cbk( self, event ):
		event.Skip()

	def CI_CfgKey_button_Cbk( self, event ):
		event.Skip()

	def CI_CreateInitFW_button_Cbk( self, event ):
		event.Skip()

	def CI_CreatPartitCode_button_Cbk( self, event ):
		event.Skip()

	def CI_CreateResetFW_button_Cbk( self, event ):
		event.Skip()

	def AT_Input_text_Cbk( self, event ):
		event.Skip()

	def AT_LoadBin_button_Cbk( self, event ):
		event.Skip()

	def AT_Key_textCtrl_Cbk( self, event ):
		event.Skip()

	def AT_IV_textCtrl_Cbk( self, event ):
		event.Skip()

	def AT_Mode_choice_Cbk( self, event ):
		event.Skip()

	def AT_Compute_button_Cbk( self, event ):
		event.Skip()

	def CM_AuthKey_textCtrl_Cbk( self, event ):
		event.Skip()

	def CM_NewKey_textCtrl_Cbk( self, event ):
		event.Skip()

	def CM_WRITE_PROT_checkBox_Cbk( self, event ):
		event.Skip()

	def CM_UID_textCtrl_Cbk( self, event ):
		event.Skip()

	def CM_Counter_textCtrl_Cbk( self, event ):
		event.Skip()

	def CM_Cal_button_Cbk( self, event ):
		event.Skip()


###########################################################################
## Class CfgKeyFrame
###########################################################################

class CfgKeyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Config Keys", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL, name = u"CSEC Tool" )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		gSizer = wx.GridSizer( 7, 3, 1, 1 )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_01 = wx.StaticText( self, wx.ID_ANY, u"Master ECU Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_01.Wrap( -1 )

		self.staticText_01.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_01.SetForegroundColour( wx.Colour( 255, 173, 0 ) )

		gbSizer1.Add( self.staticText_01, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyValue_01 = wx.TextCtrl( self, wx.ID_ANY, u"000102030405060708090A0B0C0D0E0F", wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_01.SetMaxLength( 32 )
		self.KeyValue_01.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gbSizer1.Add( self.KeyValue_01, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_01 = wx.TextCtrl( self, wx.ID_ANY, u"32/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer1.Add( self.KeyValueLen_01, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_01 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Enable_01.SetValue(True)
		self.Enable_01.Enable( False )

		gbSizer1.Add( self.Enable_01, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_01 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.WriteProt_01, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_01 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.BootProt_01, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_01 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.DebugProt_01, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_01 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.KeyUsage_01, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_01 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.WildCard_01, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_01 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.VerfiyOnly_01.Enable( False )

		gbSizer1.Add( self.VerfiyOnly_01, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer1.AddGrowableCol( 0 )
		gbSizer1.AddGrowableRow( 0 )

		gSizer.Add( gbSizer1, 1, wx.EXPAND, 5 )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_02 = wx.StaticText( self, wx.ID_ANY, u"Boot MAC Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_02.Wrap( -1 )

		self.staticText_02.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_02.SetForegroundColour( wx.Colour( 125, 178, 219 ) )

		gbSizer2.Add( self.staticText_02, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_02 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_02.SetMaxLength( 32 )
		gbSizer2.Add( self.KeyValue_02, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValueLen_02 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer2.Add( self.KeyValueLen_02, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_02 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Enable_02.Enable( False )

		gbSizer2.Add( self.Enable_02, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_02 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WriteProt_02.Enable( False )

		gbSizer2.Add( self.WriteProt_02, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_02 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BootProt_02.Enable( False )

		gbSizer2.Add( self.BootProt_02, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_02 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DebugProt_02.Enable( False )

		gbSizer2.Add( self.DebugProt_02, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_02 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KeyUsage_02.Enable( False )

		gbSizer2.Add( self.KeyUsage_02, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_02 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WildCard_02.Enable( False )

		gbSizer2.Add( self.WildCard_02, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_02 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.VerfiyOnly_02.Enable( False )

		gbSizer2.Add( self.VerfiyOnly_02, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer2.AddGrowableCol( 0 )
		gbSizer2.AddGrowableRow( 0 )

		gSizer.Add( gbSizer2, 1, wx.EXPAND, 5 )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_03 = wx.StaticText( self, wx.ID_ANY, u"Boot MAC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_03.Wrap( -1 )

		self.staticText_03.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_03.SetForegroundColour( wx.Colour( 199, 210, 45 ) )

		gbSizer3.Add( self.staticText_03, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_03 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_03.SetMaxLength( 32 )
		gbSizer3.Add( self.KeyValue_03, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValueLen_03 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer3.Add( self.KeyValueLen_03, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_03 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Enable_03.Enable( False )

		gbSizer3.Add( self.Enable_03, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_03 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WriteProt_03.Enable( False )

		gbSizer3.Add( self.WriteProt_03, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_03 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BootProt_03.Enable( False )

		gbSizer3.Add( self.BootProt_03, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_03 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DebugProt_03.Enable( False )

		gbSizer3.Add( self.DebugProt_03, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_03 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KeyUsage_03.Enable( False )

		gbSizer3.Add( self.KeyUsage_03, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_03 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WildCard_03.Enable( False )

		gbSizer3.Add( self.WildCard_03, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_03 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.VerfiyOnly_03.Enable( False )

		gbSizer3.Add( self.VerfiyOnly_03, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer3.AddGrowableCol( 0 )
		gbSizer3.AddGrowableRow( 0 )

		gSizer.Add( gbSizer3, 1, wx.EXPAND, 5 )

		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_04 = wx.StaticText( self, wx.ID_ANY, u"User Key 01", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_04.Wrap( -1 )

		self.staticText_04.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_04.SetForegroundColour( wx.Colour( 255, 173, 0 ) )

		gbSizer4.Add( self.staticText_04, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_04 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_04.SetMaxLength( 32 )
		gbSizer4.Add( self.KeyValue_04, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_04 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer4.Add( self.KeyValueLen_04, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_04 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.Enable_04, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_04 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.WriteProt_04, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_04 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.BootProt_04, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_04 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.DebugProt_04, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_04 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.KeyUsage_04, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_04 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.WildCard_04, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_04 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.VerfiyOnly_04, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer4.AddGrowableCol( 0 )
		gbSizer4.AddGrowableRow( 0 )

		gSizer.Add( gbSizer4, 1, wx.EXPAND, 5 )

		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_05 = wx.StaticText( self, wx.ID_ANY, u"User Key 02", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_05.Wrap( -1 )

		self.staticText_05.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_05.SetForegroundColour( wx.Colour( 125, 178, 219 ) )

		gbSizer5.Add( self.staticText_05, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_05 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_05.SetMaxLength( 32 )
		gbSizer5.Add( self.KeyValue_05, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_05 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer5.Add( self.KeyValueLen_05, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_05 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.Enable_05, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_05 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.WriteProt_05, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_05 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.BootProt_05, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_05 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.DebugProt_05, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_05 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.KeyUsage_05, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_05 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.WildCard_05, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_05 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.VerfiyOnly_05, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer5.AddGrowableCol( 0 )
		gbSizer5.AddGrowableRow( 0 )

		gSizer.Add( gbSizer5, 1, wx.EXPAND, 5 )

		gbSizer6 = wx.GridBagSizer( 0, 0 )
		gbSizer6.SetFlexibleDirection( wx.BOTH )
		gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_06 = wx.StaticText( self, wx.ID_ANY, u"User Key 03", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_06.Wrap( -1 )

		self.staticText_06.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_06.SetForegroundColour( wx.Colour( 199, 210, 45 ) )

		gbSizer6.Add( self.staticText_06, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_06 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_06.SetMaxLength( 32 )
		gbSizer6.Add( self.KeyValue_06, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_06 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer6.Add( self.KeyValueLen_06, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_06 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.Enable_06, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_06 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.WriteProt_06, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_06 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.BootProt_06, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_06 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.DebugProt_06, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_06 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.KeyUsage_06, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_06 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.WildCard_06, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_06 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.VerfiyOnly_06, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer6.AddGrowableCol( 0 )
		gbSizer6.AddGrowableRow( 0 )

		gSizer.Add( gbSizer6, 1, wx.EXPAND, 5 )

		gbSizer7 = wx.GridBagSizer( 0, 0 )
		gbSizer7.SetFlexibleDirection( wx.BOTH )
		gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_07 = wx.StaticText( self, wx.ID_ANY, u"User Key 04", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_07.Wrap( -1 )

		self.staticText_07.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_07.SetForegroundColour( wx.Colour( 255, 173, 0 ) )

		gbSizer7.Add( self.staticText_07, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_07 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_07.SetMaxLength( 32 )
		gbSizer7.Add( self.KeyValue_07, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_07 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer7.Add( self.KeyValueLen_07, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_07 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.Enable_07, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_07 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.WriteProt_07, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_07 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.BootProt_07, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_07 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.DebugProt_07, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_07 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.KeyUsage_07, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_07 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.WildCard_07, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_07 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.VerfiyOnly_07, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer7.AddGrowableCol( 0 )
		gbSizer7.AddGrowableRow( 0 )

		gSizer.Add( gbSizer7, 1, wx.EXPAND, 5 )

		gbSizer8 = wx.GridBagSizer( 0, 0 )
		gbSizer8.SetFlexibleDirection( wx.BOTH )
		gbSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_08 = wx.StaticText( self, wx.ID_ANY, u"User Key 05", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_08.Wrap( -1 )

		self.staticText_08.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_08.SetForegroundColour( wx.Colour( 125, 178, 219 ) )

		gbSizer8.Add( self.staticText_08, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_08 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_08.SetMaxLength( 32 )
		gbSizer8.Add( self.KeyValue_08, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_08 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer8.Add( self.KeyValueLen_08, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_08 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.Enable_08, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_08 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.WriteProt_08, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_08 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.BootProt_08, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_08 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.DebugProt_08, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_08 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.KeyUsage_08, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_08 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.WildCard_08, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_08 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.VerfiyOnly_08, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer8.AddGrowableCol( 0 )
		gbSizer8.AddGrowableRow( 0 )

		gSizer.Add( gbSizer8, 1, wx.EXPAND, 5 )

		gbSizer9 = wx.GridBagSizer( 0, 0 )
		gbSizer9.SetFlexibleDirection( wx.BOTH )
		gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_09 = wx.StaticText( self, wx.ID_ANY, u"User Key 06", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_09.Wrap( -1 )

		self.staticText_09.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_09.SetForegroundColour( wx.Colour( 199, 210, 45 ) )

		gbSizer9.Add( self.staticText_09, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_09 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_09.SetMaxLength( 32 )
		gbSizer9.Add( self.KeyValue_09, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_09 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer9.Add( self.KeyValueLen_09, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_09 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.Enable_09, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_09 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.WriteProt_09, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_09 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.BootProt_09, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_09 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.DebugProt_09, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_09 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.KeyUsage_09, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_09 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.WildCard_09, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_09 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.VerfiyOnly_09, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer9.AddGrowableCol( 0 )
		gbSizer9.AddGrowableRow( 0 )

		gSizer.Add( gbSizer9, 1, wx.EXPAND, 5 )

		gbSizer10 = wx.GridBagSizer( 0, 0 )
		gbSizer10.SetFlexibleDirection( wx.BOTH )
		gbSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_10 = wx.StaticText( self, wx.ID_ANY, u"User Key 07", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_10.Wrap( -1 )

		self.staticText_10.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_10.SetForegroundColour( wx.Colour( 255, 173, 0 ) )

		gbSizer10.Add( self.staticText_10, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_10.SetMaxLength( 32 )
		gbSizer10.Add( self.KeyValue_10, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_10 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer10.Add( self.KeyValueLen_10, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_10 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer10.Add( self.Enable_10, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_10 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer10.Add( self.WriteProt_10, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_10 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer10.Add( self.BootProt_10, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_10 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer10.Add( self.DebugProt_10, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_10 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer10.Add( self.KeyUsage_10, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_10 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer10.Add( self.WildCard_10, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_10 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer10.Add( self.VerfiyOnly_10, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer10.AddGrowableCol( 0 )
		gbSizer10.AddGrowableRow( 0 )

		gSizer.Add( gbSizer10, 1, wx.EXPAND, 5 )

		gbSizer11 = wx.GridBagSizer( 0, 0 )
		gbSizer11.SetFlexibleDirection( wx.BOTH )
		gbSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_11 = wx.StaticText( self, wx.ID_ANY, u"User Key 08", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_11.Wrap( -1 )

		self.staticText_11.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_11.SetForegroundColour( wx.Colour( 125, 178, 219 ) )

		gbSizer11.Add( self.staticText_11, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_11.SetMaxLength( 32 )
		gbSizer11.Add( self.KeyValue_11, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_11 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer11.Add( self.KeyValueLen_11, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_11 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.Enable_11, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_11 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.WriteProt_11, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_11 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.BootProt_11, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_11 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.DebugProt_11, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_11 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.KeyUsage_11, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_11 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.WildCard_11, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_11 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.VerfiyOnly_11, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer11.AddGrowableCol( 0 )
		gbSizer11.AddGrowableRow( 0 )

		gSizer.Add( gbSizer11, 1, wx.EXPAND, 5 )

		gbSizer12 = wx.GridBagSizer( 0, 0 )
		gbSizer12.SetFlexibleDirection( wx.BOTH )
		gbSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_12 = wx.StaticText( self, wx.ID_ANY, u"User Key 09", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_12.Wrap( -1 )

		self.staticText_12.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_12.SetForegroundColour( wx.Colour( 199, 210, 45 ) )

		gbSizer12.Add( self.staticText_12, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_12.SetMaxLength( 32 )
		gbSizer12.Add( self.KeyValue_12, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_12 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer12.Add( self.KeyValueLen_12, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_12 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer12.Add( self.Enable_12, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_12 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer12.Add( self.WriteProt_12, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_12 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer12.Add( self.BootProt_12, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_12 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer12.Add( self.DebugProt_12, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_12 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer12.Add( self.KeyUsage_12, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_12 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer12.Add( self.WildCard_12, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_12 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer12.Add( self.VerfiyOnly_12, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer12.AddGrowableCol( 0 )
		gbSizer12.AddGrowableRow( 0 )

		gSizer.Add( gbSizer12, 1, wx.EXPAND, 5 )

		gbSizer13 = wx.GridBagSizer( 0, 0 )
		gbSizer13.SetFlexibleDirection( wx.BOTH )
		gbSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_13 = wx.StaticText( self, wx.ID_ANY, u"User Key 10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_13.Wrap( -1 )

		self.staticText_13.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_13.SetForegroundColour( wx.Colour( 255, 173, 0 ) )

		gbSizer13.Add( self.staticText_13, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_13.SetMaxLength( 32 )
		gbSizer13.Add( self.KeyValue_13, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_13 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer13.Add( self.KeyValueLen_13, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_13 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer13.Add( self.Enable_13, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_13 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer13.Add( self.WriteProt_13, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_13 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer13.Add( self.BootProt_13, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_13 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer13.Add( self.DebugProt_13, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_13 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer13.Add( self.KeyUsage_13, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_13 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer13.Add( self.WildCard_13, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_13 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer13.Add( self.VerfiyOnly_13, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer13.AddGrowableCol( 0 )
		gbSizer13.AddGrowableRow( 0 )

		gSizer.Add( gbSizer13, 1, wx.EXPAND, 5 )

		gbSizer14 = wx.GridBagSizer( 0, 0 )
		gbSizer14.SetFlexibleDirection( wx.BOTH )
		gbSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_14 = wx.StaticText( self, wx.ID_ANY, u"User Key 11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_14.Wrap( -1 )

		self.staticText_14.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_14.SetForegroundColour( wx.Colour( 128, 178, 219 ) )

		gbSizer14.Add( self.staticText_14, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_14.SetMaxLength( 32 )
		gbSizer14.Add( self.KeyValue_14, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_14 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer14.Add( self.KeyValueLen_14, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_14 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer14.Add( self.Enable_14, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_14 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer14.Add( self.WriteProt_14, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_14 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer14.Add( self.BootProt_14, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_14 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer14.Add( self.DebugProt_14, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_14 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer14.Add( self.KeyUsage_14, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_14 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer14.Add( self.WildCard_14, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_14 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer14.Add( self.VerfiyOnly_14, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer14.AddGrowableCol( 0 )
		gbSizer14.AddGrowableRow( 0 )

		gSizer.Add( gbSizer14, 1, wx.EXPAND, 5 )

		gbSizer15 = wx.GridBagSizer( 0, 0 )
		gbSizer15.SetFlexibleDirection( wx.BOTH )
		gbSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_15 = wx.StaticText( self, wx.ID_ANY, u"User Key 12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_15.Wrap( -1 )

		self.staticText_15.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_15.SetForegroundColour( wx.Colour( 199, 210, 45 ) )

		gbSizer15.Add( self.staticText_15, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_15.SetMaxLength( 32 )
		gbSizer15.Add( self.KeyValue_15, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_15 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer15.Add( self.KeyValueLen_15, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_15 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.Enable_15, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_15 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.WriteProt_15, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_15 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.BootProt_15, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_15 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.DebugProt_15, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_15 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.KeyUsage_15, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_15 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.WildCard_15, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_15 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.VerfiyOnly_15, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer15.AddGrowableCol( 0 )
		gbSizer15.AddGrowableRow( 0 )

		gSizer.Add( gbSizer15, 1, wx.EXPAND, 5 )

		gbSizer16 = wx.GridBagSizer( 0, 0 )
		gbSizer16.SetFlexibleDirection( wx.BOTH )
		gbSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_16 = wx.StaticText( self, wx.ID_ANY, u"User Key 13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_16.Wrap( -1 )

		self.staticText_16.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_16.SetForegroundColour( wx.Colour( 255, 173, 0 ) )

		gbSizer16.Add( self.staticText_16, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_16.SetMaxLength( 32 )
		gbSizer16.Add( self.KeyValue_16, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_16 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer16.Add( self.KeyValueLen_16, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_16 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer16.Add( self.Enable_16, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_16 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer16.Add( self.WriteProt_16, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_16 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer16.Add( self.BootProt_16, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_16 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer16.Add( self.DebugProt_16, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_16 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer16.Add( self.KeyUsage_16, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_16 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer16.Add( self.WildCard_16, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_16 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer16.Add( self.VerfiyOnly_16, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer16.AddGrowableCol( 0 )
		gbSizer16.AddGrowableRow( 0 )

		gSizer.Add( gbSizer16, 1, wx.EXPAND, 5 )

		gbSizer17 = wx.GridBagSizer( 0, 0 )
		gbSizer17.SetFlexibleDirection( wx.BOTH )
		gbSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_17 = wx.StaticText( self, wx.ID_ANY, u"User Key 14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_17.Wrap( -1 )

		self.staticText_17.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_17.SetForegroundColour( wx.Colour( 125, 178, 219 ) )

		gbSizer17.Add( self.staticText_17, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_17 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_17.SetMaxLength( 32 )
		gbSizer17.Add( self.KeyValue_17, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_17 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer17.Add( self.KeyValueLen_17, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_17 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer17.Add( self.Enable_17, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_17 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer17.Add( self.WriteProt_17, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_17 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer17.Add( self.BootProt_17, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_17 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer17.Add( self.DebugProt_17, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_17 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer17.Add( self.KeyUsage_17, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_17 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer17.Add( self.WildCard_17, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_17 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer17.Add( self.VerfiyOnly_17, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer17.AddGrowableCol( 0 )
		gbSizer17.AddGrowableRow( 0 )

		gSizer.Add( gbSizer17, 1, wx.EXPAND, 5 )

		gbSizer18 = wx.GridBagSizer( 0, 0 )
		gbSizer18.SetFlexibleDirection( wx.BOTH )
		gbSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_18 = wx.StaticText( self, wx.ID_ANY, u"User Key 15", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_18.Wrap( -1 )

		self.staticText_18.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_18.SetForegroundColour( wx.Colour( 199, 210, 45 ) )

		gbSizer18.Add( self.staticText_18, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_18.SetMaxLength( 32 )
		gbSizer18.Add( self.KeyValue_18, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_18 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer18.Add( self.KeyValueLen_18, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_18 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer18.Add( self.Enable_18, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_18 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer18.Add( self.WriteProt_18, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_18 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer18.Add( self.BootProt_18, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_18 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer18.Add( self.DebugProt_18, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_18 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer18.Add( self.KeyUsage_18, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_18 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer18.Add( self.WildCard_18, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_18 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer18.Add( self.VerfiyOnly_18, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer18.AddGrowableCol( 0 )
		gbSizer18.AddGrowableRow( 0 )

		gSizer.Add( gbSizer18, 1, wx.EXPAND, 5 )

		gbSizer19 = wx.GridBagSizer( 0, 0 )
		gbSizer19.SetFlexibleDirection( wx.BOTH )
		gbSizer19.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_19 = wx.StaticText( self, wx.ID_ANY, u"User Key 16", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_19.Wrap( -1 )

		self.staticText_19.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_19.SetForegroundColour( wx.Colour( 255, 173, 0 ) )

		gbSizer19.Add( self.staticText_19, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_19.SetMaxLength( 32 )
		gbSizer19.Add( self.KeyValue_19, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_19 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer19.Add( self.KeyValueLen_19, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_19 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer19.Add( self.Enable_19, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_19 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer19.Add( self.WriteProt_19, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_19 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer19.Add( self.BootProt_19, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_19 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer19.Add( self.DebugProt_19, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_19 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer19.Add( self.KeyUsage_19, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_19 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer19.Add( self.WildCard_19, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_19 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer19.Add( self.VerfiyOnly_19, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer19.AddGrowableCol( 0 )
		gbSizer19.AddGrowableRow( 0 )

		gSizer.Add( gbSizer19, 1, wx.EXPAND, 5 )

		gbSizer20 = wx.GridBagSizer( 0, 0 )
		gbSizer20.SetFlexibleDirection( wx.BOTH )
		gbSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.staticText_20 = wx.StaticText( self, wx.ID_ANY, u"User Key 17", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.staticText_20.Wrap( -1 )

		self.staticText_20.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.staticText_20.SetForegroundColour( wx.Colour( 125, 178, 219 ) )

		gbSizer20.Add( self.staticText_20, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.KeyValue_20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 245,-1 ), 0 )
		self.KeyValue_20.SetMaxLength( 32 )
		gbSizer20.Add( self.KeyValue_20, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 5 ), wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM, 5 )

		self.KeyValueLen_20 = wx.TextCtrl( self, wx.ID_ANY, u"0/32", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
		gbSizer20.Add( self.KeyValueLen_20, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Enable_20 = wx.CheckBox( self, wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer20.Add( self.Enable_20, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WriteProt_20 = wx.CheckBox( self, wx.ID_ANY, u"WRITE_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer20.Add( self.WriteProt_20, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.BootProt_20 = wx.CheckBox( self, wx.ID_ANY, u"BOOT_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer20.Add( self.BootProt_20, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.DebugProt_20 = wx.CheckBox( self, wx.ID_ANY, u"DEBUG_PROT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer20.Add( self.DebugProt_20, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.KeyUsage_20 = wx.CheckBox( self, wx.ID_ANY, u"KEY_USAGE", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer20.Add( self.KeyUsage_20, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.WildCard_20 = wx.CheckBox( self, wx.ID_ANY, u"WILD_CARD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer20.Add( self.WildCard_20, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )

		self.VerfiyOnly_20 = wx.CheckBox( self, wx.ID_ANY, u"VERFIY_ONLY", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer20.Add( self.VerfiyOnly_20, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.BOTTOM|wx.RIGHT, 5 )


		gbSizer20.AddGrowableCol( 0 )
		gbSizer20.AddGrowableRow( 0 )

		gSizer.Add( gbSizer20, 1, wx.EXPAND, 5 )

		self.ImportKey_Button = wx.Button( self, wx.ID_ANY, u"Import Key", wx.Point( -1,-1 ), wx.Size( 180,50 ), 0 )
		self.ImportKey_Button.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.ImportKey_Button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		gSizer.Add( self.ImportKey_Button, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )


		self.SetSizer( gSizer )
		self.Layout()
		gSizer.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose_Cbk )
		self.Bind( wx.EVT_MOVE_END, self.OnMoveEnd_Cbk )
		self.KeyValue_01.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.KeyValue_02.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_02.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_03.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_03.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_04.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_04.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_05.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_05.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_06.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_06.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_07.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_07.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_08.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_08.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_09.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_09.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_10.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_10.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_11.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_11.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_12.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_12.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_13.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_13.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_14.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_14.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_15.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_15.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_16.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_16.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_17.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_17.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_18.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_18.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_19.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_19.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.KeyValue_20.Bind( wx.EVT_TEXT, self.KeyValue_xx_Cbk )
		self.Enable_20.Bind( wx.EVT_CHECKBOX, self.Enable_xx_Cbk )
		self.ImportKey_Button.Bind( wx.EVT_BUTTON, self.ImportKey_Cbk )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClose_Cbk( self, event ):
		event.Skip()

	def OnMoveEnd_Cbk( self, event ):
		event.Skip()

	def KeyValue_xx_Cbk( self, event ):
		event.Skip()


	def Enable_xx_Cbk( self, event ):
		event.Skip()





































	def ImportKey_Cbk( self, event ):
		event.Skip()


