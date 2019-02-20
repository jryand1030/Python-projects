import os, re


r= "^[a-zA-z]$"

f = open('supportingfiles/10000DirtyNames.csv','r')

clean= []

for name in f:
    if re.match(r,f,name) in none:
        print(name)

list = []

dirty_list.append(name)


f.close()
