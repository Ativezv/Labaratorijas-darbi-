import pandas as pd
get_info=input("Ievadi reģionu: ")  #input information from terminal

fails = pd.read_excel("description.xlsx", sheet_name="LookupAREA") # if no pages are specified, then the last one saved is open
info_list = fails.values.tolist()
csv=open('data.csv')


geo_count=[]
rinda=[]
area=0
# write your program code here
for row in info_list:
    if row[1] == get_info:
        area=row[0]
        break
cleanData=[]
csv=open('data.csv','r')
for line in csv:
    cleanData.append(line.rstrip().split(','))
for line in cleanData:
    if line[1]==area:
        geo_count.append(int(line[3]))
print(sum(geo_count))