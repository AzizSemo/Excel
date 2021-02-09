import Functions

Vlans_exist,Vlans_Value = Functions.From_eExcel()
Vlan_new  = Functions.Compare_Vlan()
Result = []
print(Vlans_exist)
print(Vlans_Value)
print(Vlan_new)
for vlan_Id in Vlan_new:
    index = 0
    for ID in Vlans_exist :
        if int(vlan_Id) == int(ID) :
            if str(Vlans_Value[index]) != '1.0':
              Result.append(vlan_Id)
        index +=1
print(Result)

