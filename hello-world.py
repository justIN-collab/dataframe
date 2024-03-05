import pandas as pd
import streamlit as st

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

# Menampilkan total pengguna per bulan menggunakan Streamlit
st.line_chart(total_bulan)
