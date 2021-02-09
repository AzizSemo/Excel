import pandas as pd

def From_eExcel():
  data = pd.read_excel('VLANs.xlsx')
  VLANs= data['VLAN'].tolist()
  Value= data['Value'].tolist()
  #Value= data["Value"].fillna(2, inplace = True) 
  return VLANs,Value

def Compare_Vlan():
      Vlans= open("My_Vlans.txt", "r")
      VLANS = []
      Vlan_Ohne_comma = []
      minus = '-'
      #comma = ','
      '''for vl in Vlans:
        if comma in vl:
           vl =vl.replace(',','')
           Vlan_Ohne_comma.append(vl.split())
        else :
           Vlan_Ohne_comma.append(vl)
       print(Vlan_Ohne_comma) '''
      for id in Vlans:
         id
         #print(id + " it is a range")
         if minus in str(id):
            range1 = id.split('-')
            first =int(range1[0]) 
            last = int(range1[1])
            for i in range(first, last+1):
              VLANS.append(i)
         else :
            VLANS.append(id)   
      Vlans.close()
      return VLANS


