import json
file_path = "C:/Users/ashar/Downloads/Patient.ndjson"

race_counts = {}
ethnicity_counts = {}
missing_ethnicity_count = 0  # Counter for missing ethnicity data

with open(file_path, 'r') as file:
    for line in file:
        data = json.loads(line)
        has_ethnicity = False  # Flag to track presence of ethnicity data

        # Extract race and ethnicity information
        if 'extension' in data:
            for ext in data['extension']:
                if ext['url'] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-race':
                    race = ext['extension'][0]['valueCoding']['display']
                    race_counts[race] = race_counts.get(race, 0) + 1
                elif ext['url'] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity':
                    has_ethnicity = True
                    ethnicity = ext['extension'][0]['valueCoding']['display']
                    ethnicity_counts[ethnicity] = ethnicity_counts.get(ethnicity, 0) + 1

        # If no ethnicity data is present, increment the counter
        if not has_ethnicity:
            missing_ethnicity_count += 1

print("Race Counts:", race_counts)
print("Ethnicity Counts:", ethnicity_counts)
print("Number of Patients with Missing Ethnicity Data:", missing_ethnicity_count)
