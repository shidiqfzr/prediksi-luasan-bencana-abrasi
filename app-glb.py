import streamlit as st
import predict

def main():
    st.title('Aplikasi Prediksi Luasan Bencana Abrasi')
    st.write('Aplikasi ini melakukan prediksi luasan daerah yang terdampak oleh bencana abrasi berdasarkan faktor-faktor demografi')
    menu = ['Home','Predict']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.write('Selamat Datang di Aplikasi Prediksi Bencana Abrasi')
    else :
        predict.predict_data()

if __name__ == '__main__':
    main()
