import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

# Load the trained model
filename = 'rf_model.pkl'
rf_model = pickle.load(open(filename, 'rb'))

# Create a title for your app
st.title("Marketing Campaign Response Prediction")

# Create input fields for user to enter data
st.header("Enter Customer Information:")

# Example input fields (replace with your actual features)
age = st.number_input("Age", min_value=18, max_value=100, value=30)
education = st.selectbox("Education", ["Undergraduate", "Graduate", "Postgraduate"])
income = st.number_input("Income", min_value=0, value=50000)

# Add more input fields for other features as needed

# Create a button to trigger prediction
if st.button("Predict Response"):
    # Prepare the input data for prediction
    input_data = pd.DataFrame({
        'Age': [Age],
        'Spending SCore' : [Spending Score],
        'Income': [Annual Income],
	'Previous Purchases' : [Previous Purchases],
	'Engagement' : [Campaign Engagement],
	'Last Purchase' : [Days Since Last Purchase],
	'Gender' : [Gender],
	'Marital' : [Marital Status],
	'Children' : [Children],
	'Social Media' : [Social Media Interaction],
	'Email' : [Email Click Rate],
	'Browsing' : [Online Browsing Time],
	'Loyalty' : [Loyalty Points],
	'Reviews' : [Product Reviews],
	'Tenure' : [Customer Tenure],
	'Response' : [Response]
        
    })

    # Make prediction using the loaded model
    prediction = rf_model.predict(input_data)[0]

    # Display the prediction
    if prediction == 1:
        st.success("The customer is likely to respond to the campaign.")
    else:
        st.warning("The customer is likely not to respond to the campaign.")

