import pandas as pd
import time

dataf=pd.read_excel("data_wea.xlsx",header=0,index_col=0)
data=dataf.values

data1=[]
timenow=0
for i in range(0,len(data)):
    for j in range(0,288):
        data1.append(data[i][1])
print(len(data1))

dataf1 = pd.DataFrame(data1)
dataf1.to_csv("data_wea.csv")