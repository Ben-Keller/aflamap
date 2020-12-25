import pandas

import os.path
from os import path

import subprocess as cmd

codes={
"Crops in early stages":"e",
"Pre-harvest: no drought conditions":"r",
"Around harvest: no aboundant rain":"h",
"Crops not present/active":"n",
"Pre-harvest: drought conditions":"d",
"Around harvest: aboundant rain":"w"}


dfFull = pandas.DataFrame() 

def dateSimp(date):
    year=int(date[:4])
    month=int(date[5:7])
    dek=int(date[8:10])
    return(int((year-2003)*36+(month-1)*3+(dek+9)/10))

for year in range(2003,2021):
    for month in range(12):
        for dek in ("01","11","21"):
            date=str(year)+"-"+str(month+1).zfill(2)+"-"+dek

            fil="C:/Users/bench/Documents/APHLISdata/"+date+'.csv'
            if path.exists(fil):
                df=pandas.read_csv(fil)[['asap1_id','reference_date','class_code']]
                df['reference_date'] = df['reference_date'].map(lambda dat: dateSimp(dat))
                df['class_code']=df['class_code'].map(lambda code: codes[code])
                dfFull=pandas.concat([dfFull,df])


print(dfFull.head())
dfFull.to_csv('aflaWarningsNew.csv',index = False)

cp = cmd.run("git add .", check=True, shell=True)
cp = cmd.run("git commit -m Test", check=True, shell=True)
cp = cmd.run("git push -u origin master -f", check=True, shell=True)