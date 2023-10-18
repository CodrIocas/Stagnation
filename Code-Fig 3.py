#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Fig3
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("D:/papers/Dataset.csv",encoding='gbk',low_memory=False)
df1 = df.loc[:, ['AGE','SIO2','MGO','Nb_Ta', 'Dy_Yb']]
df1.columns=['AGE', 'SIO2 ', 'MGO ', 'Nb/Ta', 'Dy/Yb']
sampleN=len(df1['AGE'])
print(df1.columns)
OutlierH = (df1['Dy/Yb'].quantile(.99))
Outlierl = (df1['Dy/Yb'].quantile(.01))

df1 = df1[(((df1['Dy/Yb'])<OutlierH)&(df1['Dy/Yb']>Outlierl))]
df1 = df1[((df1['Dy/Yb'])>=1)]

X1= 21;
X2 = 23;
binsize =1;
movestep = (X1+X2)/2/binsize
low = X1
high = X2

df1 = df1[((df1['MGO ']<18)|(df1['MGO '].isnull()))]
df1 = df1[((df1['SIO2 '] >= 45) & (df1['SIO2 '] <= 52))]
df1_Pha = df1[(df1['AGE']<=541)]
df1_Arc = df1[((df1['AGE'] >= 2500) & (df1['AGE'] <= 3200))]
df2 = pd.DataFrame(columns=['1AGE','2meanH', '3standard errorsH', '4valueH','5AGE','6meanH', '7standard errorsH', '8valueH'])

a = []
n = ()
m = ()
for j in range(1, int(movestep), 1):
    a.append(j)
    df1_PhaBinAA = df1_Pha[(((df1_Pha['Nb/Ta']) <= high) & (df1_Pha['Nb/Ta'] >= low))];
    PhaOutlierHDy= (df1_PhaBinAA['Dy/Yb'].quantile(.9))
    PhaOutlierlDy= (df1_PhaBinAA['Dy/Yb'].quantile(.1))
    df1_PhaBinAADy = df1_PhaBinAA[(((df1_PhaBinAA['Dy/Yb'])<PhaOutlierHDy)&(df1_PhaBinAA['Dy/Yb']>PhaOutlierlDy))]
    df1_PhaBinAADy.dropna(subset=['Dy/Yb'], inplace=True)
    n=len(df1_PhaBinAADy['Dy/Yb'])
    if 6 <= (low+high)/2 <= 22:
        df2.loc[j, '1AGE'] = (low+high)/2
    df2.loc[j, '2meanH'] = df1_PhaBinAADy['Dy/Yb'].mean()
    df2.loc[j, '3standard errorsH'] = ((df1_PhaBinAADy['Dy/Yb'].sem())*2)
    df2.loc[j, '4valueH'] = n
    
    df1_ArcBinAA = df1_Arc[(((df1_Arc['Nb/Ta']) <= high) & (df1_Arc['Nb/Ta'] >= low))];
    ArcOutlierHDy= (df1_ArcBinAA['Dy/Yb'].quantile(.9))
    ArcOutlierlDy= (df1_ArcBinAA['Dy/Yb'].quantile(.1))
    df1_ArcBinAADy = df1_ArcBinAA[(((df1_ArcBinAA['Dy/Yb'])<ArcOutlierHDy)&(df1_ArcBinAA['Dy/Yb']>ArcOutlierlDy))]
    df1_ArcBinAADy.dropna(subset=['Dy/Yb'], inplace=True)
    n=len(df1_ArcBinAADy['Dy/Yb'])
    if 6 <= (low+high)/2 <= 22:
        df2.loc[j, '5AGE'] = (low+high)/2
    df2.loc[j, '6meanH'] = df1_ArcBinAADy['Dy/Yb'].mean()
    df2.loc[j, '7standard errorsH'] = ((df1_ArcBinAADy['Dy/Yb'].sem())*2)
    df2.loc[j, '8valueH'] = n
    
    low = low-binsize;      
    high = high-binsize;    
df2.to_csv("D:/papers/Fig3.csv")
figure = plt.figure(figsize=(10,10))
plt.errorbar(df2['1AGE'],df2['2meanH'],yerr=df2['3standard errorsH'],fmt='o', ecolor='Black', capsize=5,markersize=10, markerfacecolor='#FFFF00',color='black')
plt.errorbar(df2['5AGE'],df2['6meanH'],yerr=df2['7standard errorsH'],fmt='o', ecolor='Black', capsize=5,markersize=10, markerfacecolor='#FF0000',color='black')

plt.scatter([], [], s=100, marker='o', color='#FFFF00', edgecolors='black')
plt.scatter([], [], s=100, marker='o', color='#FF0000')
custom_legend = {'Phanerozic': 'ko','Archean': 'ko'}
plt.legend(custom_legend)
plt.title('Comparison of Dy/Yb vs. Nb/Ta trends between Archean and Phanerozoic basalts')

yticks_major = np.arange(0.8, 2.2, 0.2)    
xticks_major = np.arange(6, 23, 4)
plt.yticks(yticks_major)   
plt.xlabel('Nb/Ta')
plt.ylabel('Dy/Yb')
plt.show()


# In[ ]:





# In[ ]:




