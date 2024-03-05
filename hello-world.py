import pandas as pd
import streamlit as st

# Load data
@st.cache_data
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
total_bulan = data_hari.groupby(['year', 'month']).agg({'casual': 'sum', 'registered': 'sum', 'cnt': 'sum'})

# Menghitung total pengguna per tahun
total_tahun = data_hari.groupby('year').agg({'casual': 'sum', 'registered': 'sum', 'cnt': 'sum'})

# Menampilkan chart line untuk total pengguna per bulan
for col in total_bulan.columns:
    st.line_chart(total_bulan[col], use_container_width=True)

# Menampilkan chart line untuk total pengguna per tahun
for col in total_tahun.columns:
    st.line_chart(total_tahun[col], use_container_width=True)
