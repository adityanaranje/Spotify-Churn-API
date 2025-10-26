import streamlit as st
import pickle
import pandas as pd


st.title("Spotify Churn Prediction")


gender = st.selectbox("Gender", ["Female","Male"])
age = st.number_input("Age", min_value=1, max_value=100)
country =  st.selectbox("Country",["AU","US","DE","IN","PK","FR","UK","CA"])
subscription_type = st.selectbox("Country",["Premium","Free","Student","Family" ])
listening_time = st.number_input("Listening time in minutes", min_value=0)
songs_played_per_day = st.number_input("Songs played per day", min_value=0)
skip_rate =  st.slider("Skip Rate", min_value=0.0, max_value=1.0, step=0.01)
device_type =  st.selectbox("Country",["Desktop","Web","Mobile"])
ads_listened_per_week= st.number_input("Ads listened per week", min_value=0)
offline_listening = st.selectbox("Offline Listening", ["Yes","No"])

if st.button("Predict Churn"):

    input_data = {
        "gender": gender,
        "age": age,
        "country": country,
        "subscription_type": subscription_type,
        "listening_time": listening_time,
        "songs_played_per_day": songs_played_per_day,
        "skip_rate": skip_rate,
        "device_type": device_type,
        "ads_listened_per_week": ads_listened_per_week,
        "offline_listening": 0 if offline_listening == "No" else 1
        }

    with open("model/model_pipeline.pkl", "rb") as f:
        model = pickle.load(f)

    input_df = pd.DataFrame([input_data])
    output = model.predict(input_df)[0]
    if output == 1:
        st.success("The person is likely to churn")
    else:
        st.success("The person is not likely to churn")