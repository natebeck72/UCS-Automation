import xlrd

import ucsmsdk


file_location = "./UCS.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(1)

# Create Session
#


from ucsmsdk.ucshandle import UcsHandle

handle = UcsHandle( (sheet.cell_value(3,1)),(sheet.cell_value(4,1)),(sheet.cell_value(5,1)))

handle.login()

mo = handle.query_dn("org-root")
print (mo)


#logout
handle.logout()





