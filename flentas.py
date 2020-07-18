# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 13:36:42 2020

@author: HP
"""
from itertools import permutations
a=int(input(''))
output=[]
while a>0:
    pattern=input('')
    text=input('')
    permList=permutations(pattern)
    flag=0
    for i in list(permList):
        if ''.join(i) in text:
            flag=1
    if flag==1:
        output.append("YES")
    else:
        output.append("NO")
    a=a-1
for i in output:
    print(i)