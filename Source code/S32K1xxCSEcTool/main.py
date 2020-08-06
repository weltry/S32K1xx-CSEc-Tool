'''
@Author: yunchuan.wang@nxp.com
@Github: https://github.com/weltry/S32K1xx-CSEc-Tool.git
@LastEditors: yunchuan.wang@nxp.com
@LastEditTime: 2020-07-03 11:50:22
'''


# -*- coding: UTF-8 -*-
import wx
import uiCbk
import ctypes, sys


'''
@description: Entrance
@param {type} 
@return: 
'''
if __name__ == '__main__':
    wxapp = wx.App()
    sub_win  = uiCbk.UI_CfgKeyFrame(None)
    main_win = uiCbk.UI_MainFrame(None, sub_win)
    main_win.Show()
    wxapp.MainLoop()