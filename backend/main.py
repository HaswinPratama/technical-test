from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from data import merged_df  # Importing merged_df from data.py

app = FastAPI()

class CustomerData(BaseModel):
    customer_id: str

@app.post("/predict/")
def predict_next_purchase(customer_data: CustomerData, n: int = Query(5, ge=1, le=10)):
    try:
        # Load the trained model (assuming RandomForestClassifier)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        # Assuming features and target are already defined in model.py
        features = ['page_views', 'time_spent', 'price', 'ratings']
        target = 'product_id'

        # Prepare customer features for prediction
        customer_features = get_customer_features(customer_data.customer_id)
        customer_features = customer_features[features]  # Keep only relevant features

        # Train the model with the merged_df
        X_train = merged_df[features]
        y_train = merged_df[target]
        model.fit(X_train, y_train)

        # Make predictions
        predictions = model.predict(customer_features)

        # Get the top N predicted products
        top_n_products_info = get_top_n_products_info(predictions, n)

        return {"customer_id": customer_data.customer_id, "top_n_products": top_n_products_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_customer_features(customer_id):
    # Fetch customer features from merged_df based on customer_id
    customer_features = merged_df[merged_df['customer_id'] == customer_id]
    return customer_features

def get_top_n_products_info(predictions, n):
    top_n_products_info = []
    for product_id in predictions[:n]:
        product_info = merged_df[merged_df['product_id'] == product_id].iloc[0]
        top_n_products_info.append({
            "product_id": str(product_id),  # Convert to string
            "category": str(product_info['category']),  # Convert to string
            "price": str(product_info['price']),  # Convert to string
            "ratings": str(product_info['ratings'])  # Convert to string
        })
    return top_n_products_info

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
