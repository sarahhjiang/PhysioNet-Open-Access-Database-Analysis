import os
import re
import csv

def extract_gender(file_path):
    gender = None

    with open(file_path, 'r') as file:
        for line in file:
            if "Gender:" in line:
                gender_text = line.split(":")[1].strip().lower()
                if gender_text == 'female':
                    gender = 'Female'
                elif gender_text == 'male':
                    gender = 'Male'
                break

    return gender

# def write_to_csv(csv_path, data):
#     with open(csv_path, 'w', newline='') as csvfile:
#         fieldnames = ['File', 'Gender']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()

#         for entry in data:
#             writer.writerow(entry)

def main(dataset_path):
    male_count = 0
    female_count = 0

    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                gender = extract_gender(file_path)
                if gender == 'Male':
                    male_count += 1
                elif gender == 'Female':
                    female_count += 1

    print("Number of males (Male):", male_count)
    print("Number of females (Female):", female_count)

if __name__ == "__main__":
    dataset_path = "/Users/sarahjiang/physionet-demographics-reporting/Archived users"
    main(dataset_path)
