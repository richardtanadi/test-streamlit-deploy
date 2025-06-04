import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.title("Program Streamlit JCDSOL19")
st.write("House Price Prediction Program")

#columns
#'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom',
#    'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea',
#    'furnishingstatus'

user_session = st.session_state

if 'value' not in user_session:
    user_session['value'] = 0

##testing markdown
st.markdown(f"""
    # Harga Rumah Hasil Prediksi: 
    # :red[$ {user_session['value']:.2f}]
""")

col1, col2 = st.columns(2)
with col1:
    area_input = st.slider(
        label="Input Luas Rumah",
        min_value = 1650.0,
        max_value = 20000.0
    )

    bedrooms_input = st.slider(
        label="Jumlah Kamar",
        min_value = 0,
        max_value = 10,
        value=1
    )

    bathrooms_input = st.slider(
        label="Jumlah Toilet",
        min_value = 0,
        max_value = 5,
        value=1
    )

    stories_input = st.slider(
        label="Jumlah Lantai",
        min_value = 0,
        max_value = 5,
        value=1
    )
    parking_input = st.slider(
        label="Jumlah Parkir Mobil",
        min_value = 0,
        max_value = 5,
        value=1
    )
with col2:
#    'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea',
    mainroad_selection = st.checkbox(
        label="Is Mainroad?", help="Yes/No apakah rumah ada di mainroad"
    )
    guestroom_selection = st.checkbox(
        label="Is There a Guestroom?", help="Yes/No apakah rumah punya kamar tamu"
    )
    basement_selection = st.checkbox(
        label="Is There a Basement?", help="Yes/No apakah rumah punya Basement"
    )
    hotwaterheating_selection = st.checkbox(
        label="Is There a Water Heater?", help="Yes/No apakah rumah punya Water Heater"
    )
    aircoditioning_selection = st.checkbox(
        label="Is There an AC?", help="Yes/No apakah rumah ada AC"
    )
    prefarea_selection = st.checkbox(
        label="Is Located in Preferred Area?", help="Yes/No apakah rumah di lokasi bagus"
    )
    furnishing_status = st.selectbox(
        label = "Kondisi Furnishing", 
        options = ['furnished', 'semi-furnished', 'unfurnished']
    )
#ordinal_column = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea','furnishingstatus']
user_input_data = {
    'area': area_input, 
    'bedrooms': bedrooms_input, 
    'bathrooms': bathrooms_input,
    'stories': stories_input,
    'mainroad': "yes" if mainroad_selection is True else "no", 
    'guestroom': "yes" if guestroom_selection is True else "no", 
    'basement': "yes" if basement_selection is True else "no", 
    'hotwaterheating': "yes" if hotwaterheating_selection is True else "no", 
    'airconditioning':"yes" if aircoditioning_selection is True else "no", 
    'parking': parking_input,
    'prefarea': "yes" if prefarea_selection is True else "no", 
    'furnishingstatus': furnishing_status
}

#convert user input jadi dataframe
df_pred = pd.DataFrame(
    data = user_input_data,
    index=[0]
)
#import encoder
with open("encoder_p43.pkl", 'rb') as f:
    data_encoder = pickle.load(f)

#encode inputs
X_pred = data_encoder.transform(df_pred)
#import model
with open("model_p43.pkl", "rb") as f:
    model = pickle.load(f)

y_pred = model.predict(X_pred)
user_session['value'] = y_pred[0]

if st.button("increment"):
    user_session['value']+=1