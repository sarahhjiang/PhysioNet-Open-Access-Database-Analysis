import wfdb
from pathlib import Path

path_to_data = Path("/media/nvme1/perisa-data/WFDBRecords")

male_count = 0
female_count = 0
other_sex_count = 0
ages = []
nan_age_count = 0
other_sex_files = []

for file_path in path_to_data.rglob("*.hea"):
    try:
        header = wfdb.rdheader(file_path.parent / file_path.stem)
        age_found = False
        sex_found = False

        for comment in header.comments:
            if comment.startswith('Age'):
                age_str = comment.split(': ')[1]
                age_found = True
                if age_str.isdigit():
                    ages.append(int(age_str))
                else:
                    nan_age_count += 1

            if comment.startswith('Sex'):
                sex = comment.split(': ')[1].strip()
                sex_found = True
                if sex == 'Male':
                    male_count += 1
                elif sex == 'Female':
                    female_count += 1

        if not sex_found or (sex_found and sex not in ['Male', 'Female']):
            other_sex_count += 1
            other_sex_files.append(file_path)

    except ValueError as e:
        print(f"Error processing file {file_path}: {e}")

# Calculate mean, min, and max age
mean_age = sum(ages) / len(ages) if ages else 0
min_age = min(ages, default=0)
max_age = max(ages, default=0)

print(f"Male Count: {male_count}")
print(f"Female Count: {female_count}")
print(f"Other Sex Count: {other_sex_count}")
print(f"Mean Age: {mean_age}")
print(f"Minimum Age: {min_age}")
print(f"Maximum Age: {max_age}")
print(f"NaN Age Count: {nan_age_count}")

# Optionally, print or process files with 'other' sex
for file in other_sex_files:
    print(f"File with other/missing sex: {file}")
