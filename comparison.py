import os
import csv
import matplotlib.pyplot as plt
class realdataresults:
    def extract_data(csv_file):
        time_series_data = {}
        
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            
            for row in reader:
                if len(row) >= 4:
                    time = row[0]  # Time (first column)
                    footfall = int(row[2]) if row[2].isdigit() else 0  # Footfall number (third column)
                    zone = row[3].strip()  # Zone name (fourth column)

                    if time and footfall and zone:
                        if zone not in time_series_data:
                            time_series_data[zone] = {'time': [], 'footfall': []}
                        
                        time_series_data[zone]['time'].append(time)
                        time_series_data[zone]['footfall'].append(footfall)
        
        return time_series_data

    def plot_and_save_time_series(time_series_data, output_folder):
        os.makedirs(output_folder, exist_ok=True)
        
        for zone, data in time_series_data.items():
            plt.plot(data['time'], data['footfall'])
            
            # Set x-axis ticks to display only every 20th time step
            plt.xticks(data['time'][::20])
            
            plt.xlabel('Time')
            plt.ylabel('Footfall')
            plt.title(f'Footfall Over Time for {zone}')
            plt.savefig(os.path.join(output_folder, f'{zone}_time_series.png'))
            plt.close()



    def convert_time_to_time_step_by_zone(csv_file):
        zone_time_step_data = {}

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            
            for row in reader:
                if len(row) >= 4:
                    time = row[0]  # Time (first column)
                    footfall = int(row[2]) if row[2].isdigit() else 0  # Footfall number (third column)
                    zone = row[3].strip()  # Zone name (fourth column)

                    # Calculate time step based on the time
                    hours, minutes, seconds = map(int, time.split(':'))
                    total_seconds = (hours - 9) * 3600 + minutes * 60 + seconds
                    time_step = total_seconds // 60  # Convert to minutes

                    # Store footfall count for the time step and zone
                    if zone not in zone_time_step_data:
                        zone_time_step_data[zone] = {}
                    if time_step not in zone_time_step_data[zone]:
                        zone_time_step_data[zone][time_step] = 0
                    zone_time_step_data[zone][time_step] += footfall

        return zone_time_step_data
    def get_unique_time_steps(csv_file):
        unique_time_steps = set()

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
                
            for row in reader:
                if len(row) >= 4:
                    time = row[0]  # Time (first column)

                    # Calculate time step based on the time
                    hours, minutes, seconds = map(int, time.split(':'))
                    total_seconds = (hours - 9) * 3600 + minutes * 60 + seconds
                    time_step = total_seconds // 60  # Convert to minutes

                    # Add time step to the set of unique time steps
                    unique_time_steps.add(time_step)

        return sorted(unique_time_steps)  # Return sorted list of unique time steps
    def get_unique_zones(csv_file):
        unique_zones = set()

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
                
            for row in reader:
                if len(row) >= 4:
                    zone = row[3].strip()  # Zone name (fourth column)
                    unique_zones.add(zone)

        return sorted(unique_zones)  # Return sorted list of unique zone names



    def link_footfall_by_time_and_zone(csv_file):
        footfall_by_time_and_zone = {}

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
                
            for row in reader:
                if len(row) >= 4:
                    time = row[0]  # Time (first column)
                    footfall = int(row[2]) if row[2].isdigit() else 0  # Footfall number (third column)
                    zone = row[3].strip()  # Zone name (fourth column)

                    # Calculate time step based on the time
                    hours, minutes, seconds = map(int, time.split(':'))
                    total_seconds = (hours - 9) * 3600 + minutes * 60 + seconds
                    time_step = total_seconds // 60  # Convert to minutes

                    # Create a dictionary for the zone if it doesn't exist
                    if zone not in footfall_by_time_and_zone:
                        footfall_by_time_and_zone[zone] = {}

                    # Link footfall to the time step for the zone
                    footfall_by_time_and_zone[zone][time_step] = footfall

        return footfall_by_time_and_zone

    def plot_footfall_by_zone(footfall_data, unique_zones):
        for zone in unique_zones:
            if zone in footfall_data:
                data = footfall_data[zone]
                time_steps = list(data.keys())
                footfall_counts = list(data.values())
                
                plt.plot(time_steps, footfall_counts, label=zone)

        plt.xlabel('Time (minutes)')
        plt.ylabel('Footfall')
        plt.title('Footfall Over Time for Each Zone')
        plt.legend()
        plt.show()

    # Example usage:
    csv_file_path = '2024-01-06-kf.csv'

    # Get unique zone names
    unique_zones = get_unique_zones(csv_file_path)
    print("Unique Zones:", unique_zones)

    # Link footfall by time and zone
    footfall_data = link_footfall_by_time_and_zone(csv_file_path)
    print("Footfall Data by Time and Zone:", footfall_data)
    # CSV file path

    outputfolder = "real_data_time_series"
    plot_footfall_by_zone(footfall_data,unique_zones)