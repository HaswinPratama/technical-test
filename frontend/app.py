import streamlit as st
import requests

# Function to make a prediction request to the backend API
def predict_next_purchase(customer_id):
    try:
        # Update the URL to point to the deployed backend API
        backend_url = "https://predict-backend-vq36ocpmka-et.a.run.app/predict/"
        response = requests.post(backend_url, json={"customer_id": customer_id})
        data = response.json()
        predicted_products = data.get("top_n_products", [])
        return predicted_products
    except Exception as e:
        st.error(f"Error: {e}")

# Streamlit UI
st.title("Predicted Products")

# Input field for entering customer ID
customer_id = st.text_input("Enter Customer ID:")

# Button to trigger prediction
if st.button("Predict"):
    if customer_id:
        # Make prediction request to the deployed backend API
        predicted_products = predict_next_purchase(customer_id)
        if predicted_products:
            st.success("Top Predicted Products:")
            # Display predicted products in a table
            st.table(predicted_products)
        else:
            st.error("Unable to fetch predicted products. Please try again.")
    else:
        st.warning("Please enter a customer ID.")
