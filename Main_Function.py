import Functions
from tqdm import tqdm

if Functions.From_eExcel() == "Error" or Functions.Compare_Vlan() == "Error":
   print("ERROR in File Opening")
else :
   Vlans_exist,Vlans_Value = Functions.From_eExcel()
   Vlan_new  = Functions.Compare_Vlan()
   Result = []
    #print(Vlans_exist)
    #print(Vlans_Value)
    #print(Vlan_new)
    #if Vlans_exist=='' | Vlans_Value=='' | Vlans_Value == '' :
     # print("Problem with File Openning")
    #else:
   for vlan_Id in tqdm(Vlan_new):
        index = 0
        for ID in tqdm(Vlans_exist) :
         if int(vlan_Id) == int(ID) :
            if str(Vlans_Value[index]) != '1.0':
              Result.append(vlan_Id)
         index +=1
   print(Result)
   Functions.Create_File(Result)


