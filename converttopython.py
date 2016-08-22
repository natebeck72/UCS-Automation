# This is the file that I use to connect to UCS and then run the converttopython part of the UCSMSDK
import xlrd

file_location = "./UCS.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(1)

from ucsmsdk.utils.ucsguilaunch import ucs_gui_launch
from ucsmsdk.ucshandle import UcsHandle

#login to the server
handle = UcsHandle( (sheet.cell_value(3,1)),(sheet.cell_value(4,1)),(sheet.cell_value(5,1)))
handle.login()

#launch the UCSM GUI
ucs_gui_launch(handle)

#convert_to_ucs portion

from ucsmsdk.utils.converttopython import convert_to_ucs_python

convert_to_ucs_python()
