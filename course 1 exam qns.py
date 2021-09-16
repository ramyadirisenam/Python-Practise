# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 10:41:47 2021

@author: RAMYA
"""

# print(" this is a single line")

# print("Hello world")

# a = 2**45

# print(a)



# you are given two inputs

a= 7 #int(input())
b= [2,3,1,4,6,5,5]#[int(i) for i in input().split()]


count = 0
for i in range(2,len(b)-1):
    print(i, ":",b[i-2], b[i-1],b[i],b[i+1])
    if b[i-2]+b[i-1]==b[i]+b[i+1]:
        count+=1

print(count)


# count =0
# for i in range(3,len(b)):
#     print(i, ":",b[i-3], b[i-2],b[i-1],b[i])
#     if b[i-3]+b[i-2]==b[i-1]+b[i]:
#         count+=1

# print(count)
final = ""
for i in range(len(b)):
    if i%3==0:
        final= final+" "+str(b[i])

print(final)



final = []
for i in range(len(b)):
    if i%3==0:
        final.append(str(b[i]))

output = " ".join(final)
print(output)


import numpy as np
mat =np.zeros((5,5))

for i in range(5):
    mat[i][i]=1
    
for i in range(5):
    for j in range(5):
        if i==j:
            mat[i][j]=3



for i in range(5):
    mat[i][4-i]=-100


for i in range(5):
    for j in range(5):
        if j==4-i:
            mat[i][j]=300000
