import numpy as np
import pandas as pd
data={"Name": ['Avery Bradley','Jae Crowder','John Holland','R.J.Hunter','Jonas Jerebko'],
      "Position": ['SG','SF','SG','SG','PF'],
      "Age": [25,25,27,22,29],
      "Height":[170,175,180,172,171],
      "Weight": [85,80,90,90,85],
      "College": ['Texas','Marquette','Texas','Georgia State',np.nan],
      "Salary": [7730337,6796117,np.nan,1148640,5000000]}
df=pd.DataFrame(data)
#기능1
df.Salary=df.Salary.replace(np.nan, 0)
print(df)

#기능2
df.loc[(df['Position']=='SG'),'Salary']+=100000
print(df)

#기능3
df.loc[(df['College']=='Texas') & (df['Age']>26),'Salary']+=100000
print(df)

# 기능4
df['BMI'] = [0,0,0,0,0]
for i in range(5):
    bmi = df.iloc[i,4] / (df.iloc[i,3]*0.01)**2
    if bmi < 24:
        df.iloc[i,7] = 'A'
    elif bmi >= 24 and bmi < 28:
        df.iloc[i,7] = 'B'
    elif bmi > 28:
        df.iloc[i,7] = 'C'
print(df)

#기능5
for i in range(5):
    if df.iloc[i,7] == 'C':
        print(df.iloc[i])

print(df)
