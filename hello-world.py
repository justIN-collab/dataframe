import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Load data
data_hari = pd.read_csv('dayy.csv')

# Konversi kolom 'date' ke tipe data datetime
data_hari['date'] = pd.to_datetime(data_hari['date'])

# Ekstraksi bulan dan tahun dari kolom 'date'
data_hari['month'] = data_hari['date'].dt.month
data_hari['year'] = data_hari['date'].dt.year

# Menghitung total pengguna per bulan
total_bulan = data_hari.groupby(['year', 'month'])[['casual', 'registered', 'cnt']].sum()

# Menghitung total pengguna per tahun
total_tahun = data_hari.groupby('year')[['casual', 'registered', 'cnt']].sum()

# Menghitung rata-rata pengguna per hari
rata_rata = data_hari['cnt'].mean()

# Create a DataFrame with a single row containing the average value
rata_rata_df = pd.DataFrame({'Rata-rata Pengguna per Hari': [rata_rata]})

# Membuat chart line untuk total pengguna per bulan
plt.figure(figsize=(10, 6))
for col in total_bulan.columns:
    bulan_tahun = total_bulan.index.map(lambda x: f"{x[0]}-{x[1]:02}")  
    plt.plot(bulan_tahun, total_bulan[col], label=col)

st.subheader('Hasil olah data total penggunaan perbulan')

plt.title('Total Pengguna per Bulan')
plt.xlabel('Tanggal')
plt.ylabel('Total Pengguna')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)
with st.expander("See explanation"):
    st.write(
        """Dari data diatas menemukan jumlah penyewaan paling tinggi berada pada bulan 09 tahun 2012, lalu nomor dua tertinggi berada pada bulan 08 tahun 2012 sedangkan untuk hasil terendah berada dalam bulan 01 tahun 2011
        """
    )

st.subheader('Rata-rata Pengguna per Tahun')
# Membuat chart line untuk total pengguna per tahun
plt.figure(figsize=(10, 6))
for col in total_tahun.columns:
    plt.plot(total_tahun.index, total_tahun[col], label=col)

plt.title('Total Pengguna per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Total Pengguna')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# Membuat chart bar untuk rata-rata pengguna per hari
st.subheader('Rata-rata Pengguna per Hari')
st.bar_chart(rata_rata_df)
with st.expander("See explanation"):
    st.write(
        """Dari data table diatas disimpulkan bahwa rata rata pengguna perharinya berada pada angka sekitar 4.500
        """
    )

