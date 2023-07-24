import os
import csv
import re

def extract_age_and_sex(text):
    age_match = re.search(r'Age:\s*(\d+)', text)
    sex_match = re.search(r'Sex:\s*([MF])', text) ## change 'Sex' to 'Gender' for human balance evaluation db

    age = int(age_match.group(1)) if age_match else None
    sex = sex_match.group(1) if sex_match else None

    return age, sex

def parse_folder_and_save_to_csv(folder_path, csv_filename):
    age_sex_data = []

    # List all .hea files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".hea"):
            file_path = os.path.join(folder_path, filename)

            # Read the content of the .hea file
            with open(file_path, "r") as file:
                content = file.read()

            # Extract age and sex information
            age, sex = extract_age_and_sex(content)

            # Store the data in a list (you can use a dictionary if you need more details)
            age_sex_data.append({"filename": filename, "age": age, "sex": sex})

    # Save the data to a CSV file
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['Filename', 'Age', 'Sex']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for data in age_sex_data:
            writer.writerow({'Filename': data['filename'], 'Age': data['age'], 'Sex': data['sex']})

folder_path = "/Users/sarahjiang/physionet-demographics-reporting/"  # Replace this with the path to your folder
csv_filename = "age_sex_data.csv"     # Specify the desired CSV filename

parse_folder_and_save_to_csv(folder_path, csv_filename)
