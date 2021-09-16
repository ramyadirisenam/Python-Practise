# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
#input_str = sys.stdin.read()
#input_list = ast.literal_eval(input_str)
list1=[1,2,3,4,5,6,7]
list2=[1,3,7]
series1=pd.Series(list1)
series2=pd.Series(list2)
out_list= series1.isin(series2)
out_list=out_list[out_list].index

import ast,sys
import pandas as pd
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
series1=pd.Series(input_list[0])
series2=pd.Series(input_list[1])
out_list=[pd.Index(series1).get_loc(num) for num in series2]
print(list(map(int,out_list)))


print(list(map(int,out_list)))#do not alter this step, list must be int type for evaluation purposes


import pandas as pd 
df=pd.read_csv("https://media-doselect.s3.amazonaws.com/generic/8NMooe4G0ENEe8z9q5ZvaZA7/googleplaystore.csv")
#add your cleaning code here
#data = data.loc[data["cases"] != 0]
#df = df[df["Installs"] !="Free"]
df1= df.drop(df.index[(df["Installs"] == "Free")],axis=0)
#df1['Avg_Annual'] = df1['Avg_Annual'].str.replace(',', '').str.replace('$', '').astype(int)
df1["Installs"] = df1["Installs"].str.replace(",","").str.replace("+","").astype(int)
#df1["Installs"] = df1["Installs"].str.replace("+","")
#df1["Installs"] = df1["Installs"].astype(int)

print(df1.corr())