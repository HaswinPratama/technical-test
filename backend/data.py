import pandas as pd

# Load datasets
customer_interactions_df = pd.read_csv('customer_interactions.csv')
product_details_df = pd.read_csv('product_details.csv')
purchase_history_df = pd.read_csv('purchase_history.csv')

# Remove the delimiter ";;" from the column headers
purchase_history_df.columns = purchase_history_df.columns.str.replace(';;', '')

# Remove the delimiter ";;" from all values in the DataFrame
purchase_history_df = purchase_history_df.applymap(lambda x: str(x).replace(';;', ''))

# Convert 'customer_id' and 'product_id' columns to the same data type
customer_interactions_df['customer_id'] = customer_interactions_df['customer_id'].astype(str)
purchase_history_df['customer_id'] = purchase_history_df['customer_id'].astype(str)
purchase_history_df['product_id'] = purchase_history_df['product_id'].astype(str)
product_details_df['product_id'] = product_details_df['product_id'].astype(str)

# Explore datasets
print("Customer Interactions:")
print(customer_interactions_df.head())
print("\nProduct Details:")
print(product_details_df.head())
print("\nPurchase History:")
print(purchase_history_df.head())

# Check for missing values
print("\nMissing Values:")
print("Customer Interactions:", customer_interactions_df.isnull().sum())
print("Purchase History:", purchase_history_df.isnull().sum())
print("Product Details:", product_details_df.isnull().sum())

# Merge customer_interactions_df with purchase_history_df on 'customer_id'
merged_df = pd.merge(customer_interactions_df, purchase_history_df, on='customer_id', how='left')

# Merge the resulting DataFrame with product_details_df on 'product_id'
merged_df = pd.merge(merged_df, product_details_df, on='product_id', how='left')

# Display the merged DataFrame
print(merged_df)