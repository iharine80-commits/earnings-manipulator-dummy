import streamlit as st
import pickle
import numpy as np

st.title("Earnings Manipulation Detector")

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.write("Enter Beneish model ratios")

DSRI = st.number_input("DSRI", value=0.0)
GMI = st.number_input("GMI", value=0.0)
AQI = st.number_input("AQI", value=0.0)
SGI = st.number_input("SGI", value=0.0)
DEPI = st.number_input("DEPI", value=0.0)
SGAI = st.number_input("SGAI", value=0.0)
ACCR = st.number_input("ACCR", value=0.0)
LEVI = st.number_input("LEVI", value=0.0)

if st.button("Predict"):
    X = np.array([[DSRI, GMI, AQI, SGI, DEPI, SGAI, ACCR, LEVI]])
    pred = model.predict(X)

    if pred[0] == 1:
        st.error("⚠️ Likely Earnings Manipulator")
    else:
        st.success("✅ Not a Manipulator")
