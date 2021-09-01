# -*- coding: utf-8 -*-
"""h8dsft_P0W1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xz-uZXvKLVl3CaaaxN0EdqLivdSoQbHT

##Fathur Rachman
##FTDS
##Batch 003
##Graded Challange

##Import Pustaka
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

"""##Data Loading"""

poke_data = pd.read_csv('Pokemon.csv')

poke_data

"""didapatkan hasil baris dan kolom sebesar 800 dan 13

##Missing Values
"""

poke_data.info()

"""Melakukan pengecekan apakah ada value yang null. Didapatkan Type 2 memiliki null sebanyak 414

##Manipulation Columns

Menghapus kolom # dan Type 2 karena tidak dibutuhkan dan memiliki null lebih dari 50%
"""

poke_data.drop(['#', 'Type 2'], axis=1, inplace=True)

poke_data

Type = poke_data['Type 1'].unique()
Type

"""##Data Query

Analis memfokuskan analisanya untuk mencari Pokemon yang paling outstanding. Oleh sebab itu tools yang digunakan adalah quantile dengan nilai 0.99

###Looking pokemon that more sustain in battle (HP)
"""

Poke_HP = poke_data['HP'].quantile([0.05, 0.25, 0.5, 0.75, 0.95, 0.99])
Poke_HP

"""Kesimpulan: HP dengan quartile paling tinggi berada diatas 150 HP"""

print('pokemon tanky')
pokemon_tanky = poke_data[poke_data["HP"] > 150.00]
pokemon_tanky

pokemon_tanky.shape

"""###Looking pokemon that give more damage in battle (Attack)"""

Poke_ATK = poke_data['Attack'].quantile([0.05, 0.25, 0.5, 0.75, 0.95, 0.99])
Poke_ATK

"""Kesimpulan: Damage dengan quartile paling tinggi berada diatas 165 Attack. Thats a lot of damage!"""

print('Strongest Pokemon')
pokemon_str = poke_data[poke_data["Attack"] > 165]
pokemon_str

pokemon_str.shape

"""###Looking pokemon that can move swiftly in battle (Speed)"""

Poke_SPD = poke_data['Speed'].quantile([0.05, 0.25, 0.5, 0.75, 0.95, 0.99])
Poke_SPD

"""Kesimpulan: Speed dengan quartile paling tinggi berada diatas 145 movement speed. Hard to catch"""

print('Fastest Pokemon')
pokemon_spd = poke_data[poke_data["Speed"] > 145]
pokemon_spd

pokemon_spd.shape

"""##Grouping and Aggregating (Based on Quartile 0.99)

###Have Highest HP
"""

Most_HP = poke_data[['Name','Type 1','HP', 'Generation', 'Legendary']].sort_values(by='HP',ascending=False).head(6)
Most_HP

"""HP paling tinggi dipegang oleh Blissey dengan HP 255 dan bukan termasuk Pokemon Legendary"""

MostHP = Most_HP['Type 1'].unique()
MostHP

"""###Have Highest Damage (Attack)"""

Most_ATK = poke_data[['Name','Type 1','Attack', 'Generation', 'Legendary']].sort_values(by='Attack',ascending=False).head(7)
Most_ATK

"""Attack paling tinggi dipegang oleh MewtwoMega Mewtwo X dengan Attack 190 dan
termasuk Pokemon Legendary
"""

MostATK = Most_ATK['Type 1'].unique()
MostATK

"""###Have Highest Agility (Speed)"""

Most_AGI = poke_data[['Name','Type 1','Speed', 'Generation', 'Legendary']].sort_values(by='Speed',ascending=False).head(6)
Most_AGI

"""Speed paling tinggi dipegang oleh DeoxysSpeed Forme dengan Speed 180 dan
termasuk Pokemon Legendary
"""

MostAGI = Most_AGI['Type 1'].unique()
MostAGI

"""##Data Visualization

##1. Jumlah Pokemon Berdasarkan Type
"""

fig, ax = plt.subplots(figsize = (20,8))
sns.countplot(data = poke_data, x = 'Type 1')
plt.ylabel('jumlah pokemon')
plt.title('kategori pokemon berdasarkan tipe')
plt.xticks(rotation = 45, horizontalalignment = 'right')
plt.show()

"""##2. Kategori Pokemon Berdasarkan Generasi"""

fig, ax = plt.subplots(figsize = (20,8))
sns.countplot(data = poke_data, x = 'Generation', hue= 'Type 1')
plt.ylabel('jumlah pokemon')
plt.title('Kategori Pokemon Berdasarkan Generasi dan Tipe')
plt.xticks(rotation = 45, horizontalalignment = 'right')
plt.show()

"""##3. Kategori Pokemon Berdasarkan Statusnya"""

sns.countplot(data = poke_data, x = 'Legendary')
plt.ylabel('jumlah pokemon')
plt.title('Jumlah Pokemon Standar dan Legend')
plt.show()

"""##4. Jumlah Pokemon yang Dikategorikan Berdasarkan HP Terbanyak dan Tipe"""

plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(20,15))
x= Most_HP.groupby("Type 1").HP.sum().sort_values(ascending= False)
fig= sns.barplot(x.values,x.index)
plt.title('Kategori Pokemon yang Memiliki HP Terbanyak')
fig.set_xlabel("HP")
fig.set_ylabel("Type 1")
plt.show()

"""##5. Jumlah Pokemon yang Dikategorikan Berdasarkan Damage Terbanyak dan Tipe"""

plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(20,15))
x= Most_ATK.groupby("Type 1").Attack.sum().sort_values(ascending= False)
fig= sns.barplot(x.values,x.index)
plt.title('Kategori Pokemon yang Memiliki Damage Terbesar')
fig.set_xlabel("Attack")
fig.set_ylabel("Type 1")
plt.show()

"""##6. Jumlah Pokemon yang Dikategorikan Berdasarkan Paling Lincah dan Tipe"""

plt.style.use('seaborn-darkgrid')
plt.figure(figsize=(20,15))
x= Most_AGI.groupby("Type 1").Speed.sum().sort_values(ascending= False)
fig= sns.barplot(x.values,x.index)
plt.title('Kategori Pokemon yang Paling Lincah')
fig.set_xlabel("Speed")
fig.set_ylabel("Type 1")
plt.show()

"""##Pengerjaan dan Kesimpulan

###Pengerjaan
- Tujuan dari analisa ini adalah untuk mencari Pokemon mana yang paling outstanding berdasarkan kagetori HP, Attack, dan Speed
- Untuk mencari outstanding analisis menggunakan metode quantile 0.99 untuk mencari mana yang paling besar dari kategori yang dijelaskan di poin 2

###Kesimpulan

- Jika dikelompokkan berdasarkan tipe, maka Pokemon dengan tipe Air memiliki anggota paling banyak
- Jumlah Pokemon dengan status legendary tergolong sedikit dibandingkan dengan yang standar
- Tipe Pokemon yang memiliki HP paling banyak dipegang oleh tipe Normal
- Tipe Pokemon yang memiliki Attack paling banyak dipegang oleh tipe Dragon
- Tipe Pokemon yang memiliki Speed paling banyak dipegang oleh tipe Psychic
"""