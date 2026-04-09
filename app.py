# import streamlit as st
# import pandas as pd
# import pickle

# # Load saved files
# model = pickle.load(open("streaming_churn_model_1.pkl", "rb"))
# scaler = pickle.load(open("scaler_1.pkl", "rb"))
# encoder = pickle.load(open("encoder_1.pkl", "rb"))

# st.title("📡 Simple Telco Churn Predictor (8 Features)")
# st.write("Fill the details below:")

# # Inputs
# senior = st.selectbox("Senior Citizen", [0, 1])
# tenure = st.number_input("Tenure (months)", 0, 100)
# monthly = st.number_input("Monthly Charges", 0.0, 200.0)

# contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
# internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
# payment = st.selectbox("Payment Method", 
#                        ["Electronic check", "Mailed check",
#                         "Bank transfer (automatic)", "Credit card (automatic)"])
# online_sec = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
# tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

# # Encode categorical values using ONE encoder (same training logic)
# def enc(x):
#     return encoder.fit_transform([x])[0]

# # Build row
# df = pd.DataFrame([{
#     "SeniorCitizen": senior,
#     "tenure": tenure,
#     "MonthlyCharges": monthly,
#     "Contract": enc(contract),
#     "InternetService": enc(internet),
#     "PaymentMethod": enc(payment),
#     "OnlineSecurity": enc(online_sec),
#     "TechSupport": enc(tech_support)
# }])

# # Scale numeric columns
# num_cols = ["SeniorCitizen", "tenure", "MonthlyCharges"]
# df[num_cols] = scaler.transform(df[num_cols])

# # Predict
# if st.button("Predict Churn"):
#     pred = model.predict(df)[0]
#     if pred == 1:
#         st.error("⚠️ Customer is likely to churn!")
#     else:
#         st.success("✅ Customer is NOT likely to churn!")





import streamlit as st
import pandas as pd
import pickle

# Load saved files
model = pickle.load(open("streaming_churn_model_1.pkl", "rb"))
scaler = pickle.load(open("scaler_1.pkl", "rb"))
encoder = pickle.load(open("encoder_1.pkl", "rb"))

st.title("📡 Simple Telco Churn Predictor (8 Features)")
st.write("Fill the details below:")

# -----------------------------------------------------
# TWO INPUTS PER ROW
# -----------------------------------------------------

# Row 1
col1, col2 = st.columns(2)
with col1:
    senior = st.selectbox("Senior Citizen", [0, 1])
with col2:
    tenure = st.number_input("Tenure (months)", 0, 100)

# Row 2
col3, col4 = st.columns(2)
with col3:
    monthly = st.number_input("Monthly Charges", 0.0, 200.0)
with col4:
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

# Row 3
col5, col6 = st.columns(2)
with col5:
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
with col6:
    payment = st.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check",
         "Bank transfer (automatic)", "Credit card (automatic)"]
    )

# Row 4
col7, col8 = st.columns(2)
with col7:
    online_sec = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
with col8:
    tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

# -----------------------------------------------------
# SINGLE ENCODER LOGIC
# -----------------------------------------------------
def enc(x):
    return encoder.fit_transform([x])[0]

# Build input row
df = pd.DataFrame([{
    "tenure": tenure,
    "MonthlyCharges": monthly,
    "TotalCharges":(tenure * monthly),
    "Contract": enc(contract),
    "PaymentMethod": enc(payment),
    "InternetService": enc(internet),
    "OnlineSecurity": enc(online_sec),
    "TechSupport": enc(tech_support)
}])

# Scale numeric columns
num_cols = ["tenure", "MonthlyCharges", "TotalCharges"]
df[num_cols] = scaler.transform(df[num_cols])

# Predict button
if st.button("Predict Churn"):
    pred = model.predict(df)[0]
    if pred == 1:
        st.error("⚠️ Customer is likely to churn!")
    else:
        st.success("✅ Customer is NOT likely to churn!")
