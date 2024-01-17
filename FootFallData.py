import csv

def calculate_footfall(csv_file):
    footfall_per_description = {}

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        
        # Skip header if present
        next(reader, None)

        for row in reader:
            if len(row) >= 6:  # Ensure the row has at least 6 columns
                description = row[5].strip()  # Assuming columns are 0-indexed
                footfall = int(row[3]) if row[3].isdigit() else 0

                # If description exists and footfall is a valid number, update the dictionary
                if description and footfall:
                    footfall_per_description[description] = footfall_per_description.get(description, 0) + footfall

    return footfall_per_description


csv_file_path = '2024-01-06-ff.csv'  
result = calculate_footfall(csv_file_path)

# Output the result
for description, total_footfall in result.items():
    print(f"{description}: {total_footfall} footfall")

    