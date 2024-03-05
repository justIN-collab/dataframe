import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load data
@st.cache
def load_data():
    data_hari = pd.read_csv('dayy.csv')
    return data_hari

data_hari = load_data()

# Konversi kolom 'date' ke tipe data datetime
data_hari['date'] = pd.to_datetime(data_hari['date'])

# Ekstraksi bulan dan tahun dari kolom 'date'
data_hari['month'] = data_hari['date'].dt.month
data_hari['year'] = data_hari['date'].dt.year

# Menghitung total pengguna per bulan
total_bulan = data_hari.groupby(['year', 'month'])[['casual', 'registered', 'cnt']].sum()

# Menampilkan chart line untuk total pengguna per bulan
plt.figure(figsize=(10, 6))
for col in total_bulan.columns:
    bulan_tahun = total_bulan.index.map(lambda x: f"{x[0]}-{x[1]:02}")  # Misalnya: "2022-01"
    plt.plot(bulan_tahun, total_bulan[col], label=col)

plt.title('Total Pengguna per Bulan')
plt.xlabel('Tanggal')
plt.ylabel('Total Pengguna')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Menampilkan plot menggunakan Streamlit
st.pyplot(plt)
