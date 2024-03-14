import pickle
import streamlit as st
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

with open('model_v1.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

def predict_loan_approval(age, annual_income, credit_score, employment_years, loan_amount_requested):
    features = pd.DataFrame({
        'Age': [age],
        'Annual_Income': [annual_income],
        'Credit_Score': [credit_score],
        'Employment_Years': [employment_years],
        'Loan_Amount_Requested': [loan_amount_requested]
    })
    print(features)
    prediction = loaded_model.predict(features)
    print(prediction[0])
    return prediction[0]

st.set_page_config(page_title="VIT", layout='wide')

# Streamlit app
def main():
    st.title('Loan Approval Prediction App')

    # Input fields
    age = st.number_input('Age', min_value=18, max_value=100)
    annual_income = st.number_input('Annual Income')
    credit_score = st.number_input('Credit Score')
    employment_years = st.number_input('Employment Years', min_value=0, max_value=50)
    loan_amount_requested = st.number_input('Loan Amount Requested')

    # Predict button
    if st.button('Predict'):
        prediction = predict_loan_approval(age, annual_income, credit_score, employment_years, loan_amount_requested)
        if prediction != 'No':
            st.header('Loan Approved')
        else:
            st.header('Loan Rejected')

if __name__ == '__main__':
    main()
