import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Data_Penjualan_Toko_Online.csv")
print(df.head)

print(df.info())
print(df.isnull().sum())

df = df.dropna()

print("Statistik deskriptif:")
print(df.describe)

print("\nProduk terlaris:")
print(df.groupby("Produk")["Jumlah"].sum().sort_values(ascending=False))

plt.figure(figsize=(8,5))
sns.barplot(data=df, x="Produk", y="Pendapatan", estimator=sum, ci=None)
plt.title("Total pendapatan per Produk")
plt.show()

plt.figure(figsize=(10,5))
sns.lineplot(data=df, x="Tanggal", y="Pendapatan", marker="o")
plt.title("Tren Pendaparan Mingguan")
plt.show()

df['Diskon'] = 0.10

df['Pendapatan Bersih'] = df['Pendapatan'] - (df['Pendapatan'] * df['Diskon'])

plt.figure(figsize=(10,5))
plt.bar(df['Produk'], df['Pendapatan Bersih'])
plt.title("Pendapatan Bersih per Produk (Setelah Diskon 10% biar customer senang)")
plt.xlabel("Produk")
plt.ylabel("Pendapatan Bersih")
plt.show()

df.to_csv("analisis_diskon.csv", index=False)
print("File 'analisis_diskon.csv' sudah tersimpan!")