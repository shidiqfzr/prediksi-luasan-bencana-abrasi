import pickle
import streamlit as st
import pandas as pd

#load model
with open('model.pkl', 'rb') as file1:
    loaded_model = pickle.load(file1)

def predict_data():
    st.title('Prediksi Luasan Bencana Abrasi di Kabupaten Sambas')

    jarak = st.number_input('Jarak ke Ibu Kota Kabupaten (km)')
    jumlah_p = st.number_input('Jumlah Penduduk')
    padat_p = st.number_input('Kepadatan Penduduk')
    perempuan = st.number_input('Perempuan')
    lansia = st.number_input('Usia Lansia (60 ke atas)')
    anak = st.number_input('Usia Anak (0-14 tahun)')
    hamil = st.number_input('Ibu Hamil')
    pendidikan = st.number_input('Tingkat Pendidikan (SMA/sederajat)')

    input = pd.DataFrame({
    'Jarak ke Ibu Kota Kabupaten (km)' : [jarak],
    'Jumlah Penduduk' : [jumlah_p],
    'Kepadatan Penduduk': [padat_p],
    'Perempuan': [perempuan],
    'Usia Lansia (60 ke atas)': [lansia],
    'Usia Anak (0-14 tahun)': [anak],
    'Ibu Hamil': [hamil],
    'Tingkat Pendidikan (SMA/sederajat)': [pendidikan]
    })

    if st.button('Prediksi'):
        pred = loaded_model.predict(input)
        pred_rounded = f"{pred[0]:.2f}"
        st.write(f'Prediksi Luas Daerah Terdampak Bencana Abrasi: {pred_rounded} Ha')

if __name__ == '__main__':
    predict_data()