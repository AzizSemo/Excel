import Functions

f = open("My_Vlans.txt", "r")
Vlans = f
VLAN = []
char = '-'
for id in Vlans:
     if char in id:
       range1 = id.split('-')
       first =int(range1[0]) 
       last = int(range1[1])
       for i in range(first, last+1):
           print(i)
       print('**********')

f.close()
      # print(last)
       #VLAN.append(id.strip())
#print(VLAN)

