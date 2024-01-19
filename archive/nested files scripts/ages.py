import os
import pandas as pd

# Base path where the folders are located
base_path = 'DataPaper/'

# List to store all ages
ages = []

# Iterate over all folders in the base path
for folder_name in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder_name)
    
    # Check if the path is indeed a directory
    if os.path.isdir(folder_path):
        # Construct the full file path - adjust the 'file_name.csv' to your file naming convention
        file_path = os.path.join(folder_path, 'user_info.csv')
        
        # Check if the file exists
        if os.path.exists(file_path):
            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            
            # Assuming 'age' column contains the age information
            # Extend the ages list with the age data from the DataFrame
            ages.extend(df['Age'].tolist())

# Now, ages list contains all the ages from all files across the folders

print(ages)