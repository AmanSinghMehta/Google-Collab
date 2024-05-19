# -*- coding: utf-8 -*-
"""aman.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ln6TnMGTmo7j_78_2UBQp7RoTZwnJCei
"""

print("hello")

import pandas as pd
df= pd.read_csv('/content/sample_data/E-commerce-data.csv')

print(df.head())

df['Remarks'].unique()

effective_df=df[df['Remarks']!='Verified Orders']
effective_df

total_count=effective_df['Count'].sum()
total_count

effective_df.groupby(['Remarks']).sum().plot(kind='pie',y='Count', autopct='%1.2f%%')

df2 = effective_df.groupby(['Period', 'Remarks']).agg({'Count': ['sum']})
df2

import matplotlib.pyplot as plt
df2.reset_index(inplace=True)
plt.figure(figsize=(15,7))

for name, group in df2.groupby('Remarks'):
    plt.plot(group['Period'],group['Count']['sum'],label=name)
plt.legend()
plt.xlabel('Period')
plt.ylabel('Count')
plt.show()

df3=effective_df.groupby(['Channel','Remarks']).agg({'Count':['sum']})

df3.unstack().plot(kind='bar')
plt.legend()
plt.title("Bar graph order by remarks by Channel")
plt.xlabel('Channel')
plt.ylabel('Count')
plt.show()

df4=effective_df.groupby(['State']).agg({'Count':['sum']})
# print(df4)
df4.plot(kind='barh',figsize=(15,7))
plt.legend()
plt.title("Bar graph order by remarks by state")
plt.xlabel('State')
plt.ylabel('Count')
plt.show()

df5=effective_df.groupby(['Dest Zone','Remarks']).agg({'Count':['sum']})
df5
df5.unstack().plot(kind='bar')
plt.legend()
plt.title("Bar graph order by remarks by Dest zone")
plt.xlabel('Destination')
plt.ylabel('Count')
plt.show()

df5=effective_df.groupby(['Dest Zone','Remarks']).agg({'Count':['sum']})
df5
df5.unstack().plot(kind='bar',stacked=True)
plt.legend()
plt.title("Bar graph order by remarks by Dest zone")
plt.xlabel('Destination')
plt.ylabel('Count')
plt.show()

df6=df.groupby(['Payment']).agg({'Count':['sum']})
df6['% Share']=100*df6['Count','sum']/df6[('Count','sum')].sum()
df6

df6.plot(kind='pie',y='Count',autopct='%1.2f%%')

andhra_pradesh_data = effective_df[effective_df['State'] == 'ANDHRA PRADESH']
andhra_pradesh_data.groupby(['Remarks']).sum().plot(kind='pie', y='Count', autopct='%1.2f%%')