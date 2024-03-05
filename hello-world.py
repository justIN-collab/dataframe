import pandas as pd
import streamlit as st

# Load data
@st.cache
def load_data():
    data_hari = pd.read_csv('dayy.csv')
    return data_hari

data_hari = load_data()

# Check if the necessary columns exist in the DataFrame
required_columns = ['date', 'casual', 'registered', 'cnt']
missing_columns = [col for col in required_columns if col not in data_hari.columns]

if missing_columns:
    st.error(f"Kolom berikut tidak ditemukan dalam DataFrame: {', '.join(missing_columns)}")
else:
    # Konversi kolom 'date' ke tipe data datetime
    data_hari['date'] = pd.to_datetime(data_hari['date'])

    # Ekstraksi bulan dan tahun dari kolom 'date'
    data_hari['month'] = data_hari['date'].dt.month
    data_hari['year'] = data_hari['date'].dt.year

    # Menghitung total pengguna per bulan
    total_bulan = data_hari.groupby(['year', 'month'])[['casual', 'registered', 'cnt']].sum().reset_index()

    # Menghitung total pengguna per tahun
    total_tahun = data_hari.groupby('year')[['casual', 'registered', 'cnt']].sum().reset_index()

    # Membuat chart line untuk total pengguna per bulan
    st.subheader('Hasil olah data total penggunaan perbulan')
    st.line_chart(total_bulan)
    with st.expander("See explanation"):



    # Membuat chart line untuk total pengguna per tahun

    st.line_chart(total_tahun)
    st.subheader('Rata-rata Pengguna per Hari')
st.bar_chart(rata_rata_df)

