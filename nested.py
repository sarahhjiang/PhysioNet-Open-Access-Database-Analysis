#!/usr/bin/env python3

import os
import re
import csv

def extract_age_gender(file_path):
    age = None
    gender = None

    with open(file_path, 'r') as file:
        for line in file:
            # Try to find the line containing age and gender information
            match = re.match(r'#\s*(\d+)\s*([MF])', line)
            if match:
                age = int(match.group(1))
                gender = match.group(2)
                break

    return age, gender

def write_to_csv(csv_path, data):
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['File', 'Age', 'Gender']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main(dataset_path, output_csv):
    data = []
    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith('.hea'):
                file_path = os.path.join(root, file)
                age, gender = extract_age_gender(file_path)
                if age is not None and gender is not None:
                    data.append({'File': file, 'Age': age, 'Gender': gender})

    write_to_csv(output_csv, data)

if __name__ == "__main__":
    dataset_path = "/Users/sarahjiang/physionet-demographics-reporting/recordings-excluded-from-the-nsr-db-1.0.0"
    output_csv = "NSR DB age_gender_data.csv" ## change csv name for each file
    main(dataset_path, output_csv)



