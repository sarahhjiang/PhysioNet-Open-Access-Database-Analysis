import os
import re
import csv

def extract_age_gender(file_path):
    age = None
    gender = None

    with open(file_path, 'r') as file:
        for line in file:
            # Try to find the line containing age information
            age_match = re.match(r'#Age:\s*(\d+)', line)
            if age_match:
                age = int(age_match.group(1))

            # Try to find the line containing gender information
            gender_match = re.match(r'Sex:\s*([MF])', line)
            if gender_match:
                gender = gender_match.group(1)

            # If both age and gender are found, no need to continue parsing
            if age is not None and gender is not None:
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
    dataset_path = "congestive_heart_failure_rr-interval-database-1.0.0/"
    output_csv = "congestive_hf_rr.csv"
    main(dataset_path, output_csv)
