import Functions

f = open("My_Vlans.txt","r")
print(f)
Vlans = f
VLAN = []
Vlan_Ohne_comma = []
minus = '-'
comma = ','
for vl in Vlans:
      if comma in vl:
           Vlan_Ohne_comma.append(vl.split(','))
      else :
           Vlan_Ohne_comma.append(vl)
#print(Vlan_Ohne_comma) 
for id in Vlan_Ohne_comma:
     '''if minus in id:
       range1 = id.split('-')
       first =int(range1[0]) 
       last = int(range1[1])
       for i in range(first, last+1):
           print(i)
       print('**********')
      # print(last)
       #VLAN.append(id.strip())'''
     print(id)
f.close()
#print(VLAN)

