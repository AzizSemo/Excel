'''import pandas as pd

#df = pd.read_excel('VLANs.xlsx', index_col=0)
data = pd.read_excel('VLANs.xlsx')
df = pd.DataFrame(data, columns= ['VLAN','Value'])
print (df)'''
import xlrd
 
loc = ("VLANs.xlsx")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
# For row 0 and column 0
sheet.cell_value(0, 0)
 
for i in range(sheet.ncols):
    print(sheet.cell_value(0, i))
for i in range(1,sheet.nrows):
    print(int(sheet.cell_value(i, 0)))