import csv

def calculate_footfall(csv_file):
    footfall_per_description = {}

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        
       
        next(reader, None)

        for row in reader:
            if len(row) >= 6:  
                description = row[5].strip()  
                footfall = int(row[3]) if row[3].isdigit() else 0

                
                if description and footfall:
                    footfall_per_description[description] = footfall_per_description.get(description, 0) + footfall

    return footfall_per_description


csv_file_path06 = '2024-01-06-ff.csv'  
csv_file_path07 = '2024-01-07-ff.csv'
result06 = calculate_footfall(csv_file_path06)
result07 = calculate_footfall(csv_file_path07)

# Output the result
for description, total_footfall in result07.items():
    print(f"{description}: {total_footfall} footfall")

