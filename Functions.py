import pandas as pd
import csv   


def From_eExcel():
  try:
      #data =
      data = pd.read_excel('OEDIV-DC-VLANs.xlsx') 
      VLANs= data['vlan'].tolist()
      Value= data['LAN_UCS_Power_TR_NK_aka usr'].tolist()
      return VLANs,Value
  except IOError:
    print("Could not Find EXCEL file: ")
    return "Error"


def Compare_Vlan():
   try:
      Vlans= open("VLAN.txt", "r")
      VLANS = []
      Vlan_Ohne_comma = []
      minus = '-'
      #comma = ','
      '''
      try:
    f = open('somefile.txt', 'r')
    print(f.read())
    f.close()
except IOError:
    print('file not found')
      '''
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
   except IOError:
    print("Could not Find TXT file: ")
    return "Error"
def Create_File(Result_v):
       f = open("Result.txt", "w")
       for i in Result_v:
          f.write(str(i).rstrip())
          f.write('\n')
       print("File is Cteated")
       f.close()


