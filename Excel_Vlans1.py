import pandas as pd

def From_eExcel():
  path = input("please Enter the Excel Datei Path like   D:\Online Courses\VLANs.xlsx     ")
  data = pd.read_excel(path.strip())
  VLANs= data['VLAN'].tolist()
  Value= data['Value'].tolist()
  print(VLANs)
  print(Value)
  return Vlans,Value