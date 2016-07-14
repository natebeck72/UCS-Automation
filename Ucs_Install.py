import xlrd
import ucsmsdk

file_location = "./UCS.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(1)

