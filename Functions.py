import pandas as pd
import csv   


def From_eExcel():
  try:
      #data =
      data = pd.read_excel('OEDIV-DC-VLANs.xlsx') #read from Excel File
      VLANs= data['vlan'].tolist() #read contants of specefic columns and convert it to list
      Value= data['LAN_UCS_Power_TR_NK_aka'].tolist()#read contants of specefic columns and convert it to list
      return VLANs,Value #return tow values
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
def Create_File(Result_v):#create a Text File and put the  the Result in it
       f = open("Result.txt", "w")
       for i in Result_v:
          f.write(str(i).rstrip())
          f.write('\n')
       print("File is Cteated")
       f.close()


