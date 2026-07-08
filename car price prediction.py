import pandas as pd
import numpy as np
import datetime
import xgboost as xgb
import streamlit as st

def main():
    html_temp = """<h1> Price Prediction</h1>"""
    
    model = xgb.XGBRegressor()
    model.load_model("xgb_model.json")
    
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("This app will help you predict your car selling price") 

    p1 = st.number_input("Enter the ex-showroom price of the car (in Lakhs):", 2.5,25.0, step=1.0)
    p2 = st.number_input("Enter car driven distance (in Kms):", 100, 50000, step=100)

    s1 = st.selectbox("Select the fuel type of the car:", ["Petrol", "Diesel", "CNG", ])

    if s1 == "Petrol":
        p3 = 0
    elif s1 == "Diesel":
        p3 = 1
    else:
        p3 = 2
    
    s2 = st.selectbox("Select the seller type of the car:", ["Individual", "Dealer", ])

    if s2 == "Individual":
        p4 = 0
    else:
        p4 = 1

    s3 = st.selectbox("Select the transmission type of the car:", ["Manual", "Automatic", ])

    if s3 == "Manual":
        p5 = 0
    else:
        p5 = 1

    p6 = st.slider("how many owners has the car had?", 0, 5, step=1)    
    
    years = st.number_input("Enter the year of purchase of the car:", 1990,datetime.datetime.now().year, step=1)
    p7 = datetime.datetime.now().year - years

    data_new = pd.DataFrame({'Present_Price':p1, 'Kms_Driven':p2, 'Fuel_Type':p3, 'Seller_Type':p4, 'Transmission':p5, 'Owner':p6, 'Age':p7}, index=[0])
    
    if st.button("Predict"):
        prediction = model.predict(data_new)
        st.success(f"The predicted selling price of the car is: {prediction[0]:.2f} Lakhs")
        
if __name__ == "__main__":
    main()