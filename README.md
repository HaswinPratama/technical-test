# technical-test

# Github Repo : https://github.com/HaswinPratama/technical-test.git
# Web URL : https://predict-frontend-vq36ocpmka-et.a.run.app/

# We build a predictive model using Random Forest to forecast the next product a customer is likely to purchase.

# Reason why using Random Forest :
# 1. It's an ensemble learning method that combines multiple decision trees to improve predictive performance.
# 2. Random Forest can capture complex nonlinear relationships between features and the target.
# 3. It's robust to overfitting and noise in the data.
# 4. It provides feature importance scores, which can help in understanding which features are most influential in predicting the 5. target variable.

# Backend : FastAPI 
# Frontend : Streamlit
# Deployment : Google Cloud Run

# How to use the AI Application ?
# 1. Visit URL : https://predict-frontend-vq36ocpmka-et.a.run.app/
# 2. Enter Customer ID between 1 and 5
# 3. It will give you top predicted products based on the Random Forest model
# 4. Because the dataset is small so the model accuracy is not good enough