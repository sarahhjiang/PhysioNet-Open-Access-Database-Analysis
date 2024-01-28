import pandas as pd

def process_csv(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Remove duplicate rows based on the 'subject_id' column
    df_unique = df.drop_duplicates(subset='subject_id')

    # Count the number of occurrences of each race
    race_counts = df_unique['race'].value_counts()

    return race_counts

if __name__ == "__main__":
    file_path = 'C:/Users/ashar/Downloads/admissions.csv/admissions.csv'  # Replace with the path to your CSV file
    race_counts = process_csv(file_path)
    print(race_counts)


