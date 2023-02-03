#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

# Verileri okutuyoruz.
data = pd.read_csv('sales.csv')

# Verileri düzenliyoruz burda boş verileri siliyoruz.
data.dropna(inplace=True)
data = df[df['Total Net Sales'] > 0]

# Türlerine göre sınıflandırıma yapıyoruz.
grup = data.groupby('Product Type').agg({'Net Quantity': 'sum',
                                           'Gross Sales': 'sum',
                                           'Discounts': 'sum',
                                           'Returns': 'sum',
                                           'Total Net Sales': 'sum'})

# Verileri özelleştirip çiziyoruz.
grup.plot.bar(y='Total Net Sales', color='pink')
plt.xlabel('Product Type')
plt.ylabel('Total Net Sales')
plt.title('Aggregated Sales by Product Type')
plt.show()

# İstatistik Ölçümü yapıp ekrana yazdırıyoruz.
print("Sales Data Statistics:")

print("Satılan Toplam Net Kar: ", grup['Net Quantity'].sum())
print("Bürüt Satış: $", grup['Gross Sales'].sum())
print("Toplam İndirimler: $", grup['Discounts'].sum())
print("Toplam İadeler: $", grup['Returns'].sum())
print("Toplam Satış Miktarları: $", grup['Total Net Sales'].sum())


# In[ ]:




