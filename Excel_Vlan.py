import xlrd

loc = ("VLANs.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 # For row 0 and column 0
sheet.cell_value(0, 0)
Vlan_new = [2,25,34,24]
Vlans_exist = []
Vlans_Value = []
#for i in range(sheet.ncols):
 #   print(sheet.cell_value(0, i))
for i in range(1,sheet.nrows):
   Vlans_exist.append(int(sheet.cell_value(i, 0)))
   if sheet.cell_value(i, 1) == 1 :
     Vlans_Value.append(int(sheet.cell_value(i, 1)))
   else :
      Vlans_Value.append(sheet.cell_value(i, 1)) 
print(Vlans_exist)
print(Vlans_Value)