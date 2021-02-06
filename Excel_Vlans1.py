import pandas as pd

#df = pd.read_excel('VLANs.xlsx', index_col=0)
data = pd.read_excel('VLANs.xlsx')
VLANs= pd.DataFrame(data, columns= ['VLAN'])
Value= pd.DataFrame(data, columns= ['Value'])
print (Value)