import streamlit as st
import pandas as pd
import joblib
st.title("USEDCAR PRICE PREDICTION PAGE")
st.image("https://miro.medium.com/max/647/1*ZOcUPrSXLYucFxppoI-dYg.png")
scaler = joblib.load(open("scaler.joblib","rb"))
model = joblib.load(open("xgb_model.joblib","rb"))
columns = joblib.load("columns.joblib")

st.sidebar.title('Configure Your Car')
Year = st.sidebar.number_input("Year", min_value =2000, max_value = 2018, value=2014)
Present_Price = st.sidebar.number_input("Present_Price", min_value =0.00, max_value = 35.00, value=5.59)
Kms_Driven = st.sidebar.number_input("Kms_Driven", value=27000, step=100)
Fuel_Type = st.sidebar.selectbox("Fuel_Type", ["Petrol","Diesel", "CNG"])
Seller_Type = st.sidebar.selectbox("Fuel_Type", ["Dealer", "Individual"])
Transmission = st.sidebar.selectbox("Fuel_Type", ["Manual", "Automatic"])
Owner = st.sidebar.number_input("Owner", min_value =0, max_value = 3, value=0)
data = {}
data["Year"]=Year
data["Present_Price"]=Present_Price
data["Kms_Driven"]=Kms_Driven
data["Fuel_Type"]=Fuel_Type
data["Seller_Type"]=Seller_Type
data["Transmission"]=Transmission
data["Owner"]=Owner
predict = st.sidebar.button("P R E D I C T")
if predict:
    df = pd.DataFrame([data])
    df["Year"] = 2018 - df["Year"]
    df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)
    df = scaler.transform(df)
    result = model.predict(df)
    st.table(pd.DataFrame([data]))
    st.write(f"$ {result[0]:.5f}")



