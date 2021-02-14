import Functions
from tqdm import tqdm

if Functions.From_eExcel() == "Error" or Functions.Compare_Vlan() == "Error":#check if an error in the Openning
   print("ERROR in File Opening")
else :
   Vlans_exist,Vlans_Value = Functions.From_eExcel()# store the Result in tow Lists
   Vlan_new  = Functions.Compare_Vlan()
   Result = []
   for vlan_Id in tqdm(Vlan_new):
        index = 0
        for ID in tqdm(Vlans_exist) :
         if int(vlan_Id) == int(ID) :#
            if str(Vlans_Value[index]) != '1.0': #here will be checkt if the Value does not equal to 1.0
              Result.append(vlan_Id)
         index +=1
   print(Result)
   Functions.Create_File(Result)


