#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Fig4
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("D:/papers/Dataset.csv",encoding='gbk',low_memory=False)
df1 = df.loc[:, ['AGE','SIO2','MGO','Nb_Ta', 'Dy_Yb']]
df1.columns=['AGE', 'SIO2 ', 'MGO ', 'Nb/Ta', 'Dy/Yb']
df1['MGO '] = df1['MGO '].astype(float)
df1['AGE'] = df1['AGE'].astype(float)
SampleN = len(df1)

OutlierH = (df1['Dy/Yb'].quantile(.995))
Outlierl = (df1['Dy/Yb'].quantile(.005))
df1 = df1[(((df1['Dy/Yb'])<OutlierH)&(df1['Dy/Yb']>Outlierl))]
df1 = df1[((df1['Dy/Yb'])>=1)]
df1 = df1[((df1['MGO ']<18)|(df1['MGO '].isnull()))]
df1 = df1[((df1['SIO2 '] >= 45) & (df1['SIO2 '] <= 52))]
df2 = pd.DataFrame(columns=['AGE','2meanH', '3standard errorsH', '4valueH',
                            '5meanL','6standard errorsL','7valueL',
                            '8meanD','9stdD'])
dfH = df1
dfl = df1

dfH = dfH[((dfH['Nb/Ta'] >= 14) & (dfH['Nb/Ta'] <= 22))]
dfl = dfl[((dfl['Nb/Ta'] >= 8) & (dfl['Nb/Ta']<=14))]

X1=3000
X2=3400
movestep = 100
low = X1
high = X2

a = []
n = ()
m = ()
simuHSi = []
simuLSi = []

for j in range(1, (int((low / movestep + 2))), 1):  
    a.append(j);
    dfHA = dfH[(((dfH['AGE']) < high) & (dfH['AGE'] >= low))]
    n = len(dfHA);
    df2.loc[j, 'AGE'] = low;
    df2.loc[j, '2meanH'] = dfHA['Dy/Yb'].mean();
    df2.loc[j, '3standard errorsH'] = ((dfHA['Dy/Yb'].sem()));
    df2.loc[j, '4valueH'] = n;

    dflA = dfl[(((dfl['AGE']) <= high) & (dfl['AGE'] >= low))];
    m = len(dflA);
    df2.loc[j, 'AGE'] = low;
    df2.loc[j, '5meanL'] = dflA['Dy/Yb'].mean();
    df2.loc[j, '6standard errorsL'] = ((dflA['Dy/Yb'].sem()));
    df2.loc[j, '7valueL'] = m;

    simuHSi = np.random.normal(df2.loc[j, '2meanH'], df2.loc[j, '3standard errorsH'], 10000);
    simuLSi = np.random.normal(df2.loc[j, '5meanL'], df2.loc[j, '6standard errorsL'], 10000);
    diff = list(map(lambda x: x[0] - x[1], zip(simuHSi, simuLSi)));

    df2.loc[j, '8meanD'] = np.mean(diff);
    df2.loc[j, '9stdD'] = (2 * (np.std(diff)));
    low = low - movestep;
    high = high - movestep;

print(list(df2['AGE']))
print(df2.head(20))

x = list(df2.loc[:,'AGE'])
y = list(df2['2meanH'])

df2.to_csv("D:/papers/Fig4.csv")
figure = plt.figure(figsize=(15,15))
axes1 = figure.add_subplot(3,1,1)
plt.errorbar(df2['AGE'],df2['2meanH'],yerr=df2['3standard errorsH'])
plt.xlabel('AGE')
plt.ylabel('HSi DyYbn mean')
plt.xlim(0,3000)
axes2 = figure.add_subplot(3,1,2)
plt.errorbar(df2['AGE'],df2['5meanL'],yerr=df2['6standard errorsL'])
plt.xlabel('AGE')
plt.ylabel('lSi DyYbn mean')
plt.xlim(0,3000)
axes3 = figure.add_subplot(3,1,3)
plt.errorbar(df2['AGE'],df2['8meanD'],yerr=df2['9stdD'])
plt.xlabel('AGE')
plt.ylabel('Diff')
plt.xlim(0,3000)
plt.show()


# In[ ]:




