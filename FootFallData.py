import csv

def calculate_footfall(csv_file):
    footfall_per_description_hourly = {}

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) >= 6:  
                description = row[5].strip()  
                footfall = int(row[3]) if row[3].isdigit() else 0
                time = row[2]  # Assuming column 3 is the time column

                if description and footfall:
                    hour = int(time.split(':')[0])  # Extracting the hour
                    if 8 <= hour <= 18:  # Check if hour is between 8 and 18
                        footfall_per_hour = footfall_per_description_hourly.setdefault(description, {})
                        footfall_per_hour[hour] = footfall_per_hour.get(hour, 0) + footfall

    return footfall_per_description_hourly

csv_file_path06 = '2024-01-06-ff.csv'  
csv_file_path07 = '2024-01-07-ff.csv'
csv_file_path10 = '2024-02-10-ff.csv'
result06 = calculate_footfall(csv_file_path06)
result07 = calculate_footfall(csv_file_path07)
result10 = calculate_footfall(csv_file_path10)
# Output the result
for description, hour_footfall in result10.items():
    print(f"Description: {description}")
    for hour in range(8, 19):  # Iterate over hours from 8 to 18
        footfall = hour_footfall.get(hour, 0)  # Get footfall count or default to 0
        print(f"Hour {hour}: {footfall} footfall")
    print()