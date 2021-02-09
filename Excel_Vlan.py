
import pandas as pd

data = pd.read_excel('VLANs.xlsx')
VLANs= data['VLAN'].tolist()
Value= data['Value'].tolist()
#Value= data["Value"].fillna(2, inplace = True) )
print(Value)
for i in Value :
    if str(i) == '1.0':
        print(i)
    else:
        print('Empty')