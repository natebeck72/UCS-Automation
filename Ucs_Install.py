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

# Compute Chassis Link Aggregation Policy

from ucsmsdk.mometa.compute.ComputeChassisDiscPolicy import ComputeChassisDiscPolicy

mo = ComputeChassisDiscPolicy(parent_mo_or_dn="org-root", rebalance="user-acknowledged", action=(sheet.cell.value(8.1)), descr="", name="", policy_owner="local", link_aggregation_pref="none")
handle.add_mo(mo, True)

handle.commit()


#logout

handle.logout()





