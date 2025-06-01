import streamlit as st 
import requests


st.title('Insurance Premium Category Predictor')

st.markdown('Enter You details below : ')

# input fields

age = st.number_input("Age",min_value = 1,max_value = 119,value = 30)
weight = st.number_input("Weight in kgs",min_value = 1.0,value = 45.50)
height = st.number_input("Height in mtrs",min_value = 0.5,max_value = 2.5)
income_lpa = st.number_input("Income(LPA)",value = 10.0,min_value = 0.1)

smoker = st.selectbox(
    "Are you smoker or not?",options=["Yes","No"]
)
smoker = True if smoker=='Yes' else False

city = st.text_input('City',value = "Mumbai")

occupation = st.selectbox(
    'Occupation',
    ('retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'),
)

if st.button('Predict Premium Category'):
    input_data = {
        'age':age,
        'weight':weight,
        'height':height,
        'income_lpa':income_lpa,
        'smoker':smoker,
        'city':city,
        'occupation':occupation
    }
    try:
        response = requests.post('https://insurance-premium-predictor-api.onrender.com/predict',json=input_data)

        if response.status_code == 200:
            prediction = response.json().get('predicted_category')
            st.header(f'Insurance Premium Category is {prediction}')
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")

