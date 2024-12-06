import pandas as pd
import numpy as np

def ordinal_encode(df, column, order=None):
   
    
    if order is None:
        
        order = list(df[column].unique())
    
    
    category_to_code = {category: code for code, category in enumerate(order)}
    
    
    df[column + '_encoded'] = df[column].map(category_to_code)
    
    return df


data = {'City': ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Delhi', 'Mumbai']}
df = pd.DataFrame(data)

order = ['Chennai', 'Kolkata', 'Mumbai', 'Delhi']
df_encoded = ordinal_encode(df, 'City', order)

print(df_encoded)
