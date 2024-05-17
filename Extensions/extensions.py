import pandas as panda

extensionsDataFrame = panda.read_excel('extensions.xlsx','Sheet1') ; extensions = {}

extensionsDataFrame['Ext'] = extensionsDataFrame['Ext'].astype(int)

for row in range(len(extensionsDataFrame)):
    info = {
         'Dept.' :   ""
        ,'User'  :   ""
    }
    info['Dept.'] = extensionsDataFrame['Dept.'][row] ; info['User'] = extensionsDataFrame['User'][row]
    extensions[str(extensionsDataFrame['Ext'][row])] = info
    
row = input("Extension: ")

print(extensions[row])