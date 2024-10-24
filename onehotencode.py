import pandas as pd
import numpy as np

def one_hot_encode(df, column):
    """
    Function to perform one-hot encoding on a specified column.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the data
    column (str): The name of the column to encode

    Returns:
    pd.DataFrame: DataFrame with the one-hot encoded columns
    """
    
    # Get the unique values from the column
    unique_values = df[column].unique()
    
    # Create a new DataFrame for the one-hot encoded columns
    one_hot_encoded_df = pd.DataFrame()
    
    # Iterate over the unique values and create binary columns
    for value in unique_values:
        one_hot_encoded_df[column + '_' + str(value)] = np.where(df[column] == value, 1, 0)
    
    # Concatenate the original DataFrame with the one-hot encoded columns
    df = pd.concat([df, one_hot_encoded_df], axis=1)
    
    # Optionally, drop the original column
    df = df.drop(column, axis=1)
    
    return df

# Example usage
data = {'City': ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Delhi', 'Mumbai']}
df = pd.DataFrame(data)

# Perform one-hot encoding
df_encoded = one_hot_encode(df, 'City')

print(df_encoded)
