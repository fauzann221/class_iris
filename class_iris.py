import pickle
import streamlit as st

# membaca model
model = pickle.load(open('class_iris.sav', 'rb'))

#judul web
st.title('Prediksi Spesies Tumbuhan Iris')

SepalLengthCm = st.number_input ('Panjang Sepal Bungan Dalam Cm')
SepalWidthCm = st.number_input ('Lebar Sepal Bungan Dalam Cm')
PetalLengthCm = st.number_input ('Panjang Kelopak Bungan Dalam Cm')
PetalWidthCm = st.number_input ('Lebar Kelopak Bungan Dalam Cm')

# code untuk prediksi
predict = ''

# membuat tombol untuk prediksi
if st.button('Test'):
    iris_predict = model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])

    if iris_predict == 0:
        predict = 'Tumbuhan Termasuk Kedalam Kelompok Iris Setosa'
    elif iris_predict == 1:
        predict = 'Tumbuhan Termasuk Kedalam Kelompok Iris Versicolor'
    else:
        predict = 'Tumbuhan Termasuk Kedalam Kelompok Iris Virginica'
st.success(predict)
