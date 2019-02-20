#Objective#
#To create a program that will open a file with a list of poorly formated and unaccepeted names,
#and sort those names into two seperate files - invalidNames.csv and CleanNames.csv

#steps to completing this assigment

#1-access filename DirtyNames.csv
#2-filter through list of names to determine invalid names and place name in a created invalidnamefile.(module for function to identify non letter)
#3-filter through list of names to determine valid names that do not need to be reformated and place in cleannamefile
#4-filter throughh list of names and refromat names in list to display capital letter first and all small cap latter.( build module with function to handle this)


import csv
f = open('supportingfiles/10000DirtyNames.csv')
csv_f = csv.reader(f)

for name in csv_f:
    print(len(name))

f.close()
