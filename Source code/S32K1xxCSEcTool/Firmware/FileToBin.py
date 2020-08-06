'''
@Author: yunchuan.wang@nxp.com
@Github: https://github.com/weltry/S32K1xx-CSEc-Tool.git
@LastEditors: yunchuan.wang@nxp.com
@LastEditTime: 2020-07-03 11:10:04
'''
# -*- coding: utf-8 -*-
import string

Firmwares = ["S32K116F128.srec","S32K118F256.srec","S32K142F256.srec","S32K144F512.srec","S32K146F1M.srec","S32K148F2M.srec"]
'''
for fw in Firmwares:
    FwString = "Bin = b'\\\n"
    f = open(fw,"rb")
    for line in f.readlines():
        FwString = FwString + str(line)[2:-1]+"\\\n"
    FwString = FwString + "\'"
    f.close()
    f = open(fw[:-4]+"py","w")
    f.write(FwString)
    f.close()
'''
for fw in Firmwares:
    FwString = "Bin = \\\n'''"
    f = open(fw,"rb")
    for line in f.readlines():
        #print(str(line))
        #print(str(line)[2:-5])
        FwString = FwString + str(line)[2:-5]+"\n"

    FwString = FwString + "'''"
    f.close()
    f = open(fw[:-4]+"py","w")
    f.write(FwString)
    f.close()
