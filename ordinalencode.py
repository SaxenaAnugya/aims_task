import pandas as pd
import numpy as np

def ordinal_encode(df, column, order=None):
   
    
    if order is None:
        # Use the unique values in the column if no specific order is provided
        order = list(df[column].unique())
    
    # Create a dictionary that maps each category to an integer based on the provided order
    category_to_code = {category: code for code, category in enumerate(order)}
    
    # Apply the mapping to the column
    df[column + '_encoded'] = df[column].map(category_to_code)
    
    return df

# Example usage
data = {'City': ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Delhi', 'Mumbai']}
df = pd.DataFrame(data)

# Ordinal encoding with a specified order
order = ['Chennai', 'Kolkata', 'Mumbai', 'Delhi']
df_encoded = ordinal_encode(df, 'City', order)

print(df_encoded)
