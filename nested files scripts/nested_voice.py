import os
import re
import csv

## extract demographics data for VOICED database

def extract_age_and_sex(file_path):
    age = None
    sex = None

    with open(file_path, 'r') as file:
        for line in file:
            # Try to find the lines containing age and sex information
            age_match = re.search(r'<age>:\s*(\d+)', line)
            sex_match = re.search(r'<sex>:\s*([MF])', line)

            if age_match:
                age = int(age_match.group(1))
            if sex_match:
                sex = sex_match.group(1)

            # If both age and sex are found, no need to continue parsing
            if age is not None and sex is not None:
                break

    return age, sex

def write_to_csv(csv_path, data):
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['File', 'Age', 'Sex']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for entry in data:
            writer.writerow(entry)

def main(dataset_path, output_csv):
    data = []
    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith('.hea'):
                file_path = os.path.join(root, file)
                age, sex = extract_age_and_sex(file_path)
                if age is not None and sex is not None:
                    data.append({'File': file, 'Age': age, 'Sex': sex})

    write_to_csv(output_csv, data)

if __name__ == "__main__":
    dataset_path = "/Users/sarahjiang/physionet-demographics-reporting/voice-icar-federico-ii-database-1.0.0"
    output_csv = "voice data.csv"
    main(dataset_path, output_csv)
