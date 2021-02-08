import Functions

Vlans_exist,Vlans_Value = Functions.From_eExcel()
Vlan_new = [3,34,24,7,5]
Result = []
print(Vlans_exist)
print(Vlans_Value)
 #wiedr = []
for vlan_Id in Vlan_new:
    index = 0
    for ID in Vlans_exist :
        index +=1
        if vlan_Id == ID :
            if Vlans_Value != 1:
                Result.append(ID)
print(Result)

