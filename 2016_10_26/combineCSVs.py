# coding: utf-8
import os
import pandas as pd

flist=[]
for filename in os.listdir('.'):
    if (filename.endswith(".csv") & (filename!="allDept.csv")): 
        flist=flist+[filename]

dfl=[]
for fn in flist:
    dfl.append(pd.read_csv(fn,sep='\t',encoding='utf-16',parse_dates=True,index_col=[0,1],usecols=[0,1,3]))
    dfl[-1]=dfl[-1].rename(columns = {'Nouveaux Cas':fn[:-4]})

df=pd.concat(dfl,axis=1)

df=df.reindex_axis(sorted(df.columns), axis=1)

df.to_pickle('dataframeCombined.pickle')
df.to_csv('allDept.csv')

ax=df.plot(x=df.index.levels[0])
ax.get_figure().savefig('output.png')
