import streamlit as st
from modules.db import requests_collection  # This imports the connected collection

st.title("📋 Request Tracker")

with st.form("request_form"):
    name = st.text_input("Your Name")
    request_type = st.selectbox("Request Type", ["PO", "RFM"])
    Number = st.text_input("Number")
    description = st.text_area("Describe your request")
    submitted = st.form_submit_button("Submit")

    if submitted:
        requests_collection.insert_one({
            "name": name,
            "type": request_type,
            "description": description,
            "status": "Pending"
        })
        st.success("✅ Your request has been submitted!")
