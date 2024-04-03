import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Formulas:
    def plot_score_surface(self, time_counters, planned_durations, output_folder):
        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        # Iterate over overcrowdedness scores from 0 to 1 in steps of 0.2
        for score in np.arange(0, 1.2, 0.2):
            # Create a meshgrid of time_counters and planned_durations
            X, Y = np.meshgrid(time_counters, planned_durations)
        
            # Calculate the score for each combination of time_counter and planned_duration
            scores = np.minimum(Y / X, 1.0) * score
        
            # Plot the 3D surface
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot_surface(X, Y, scores, cmap='viridis')
        
            # Set labels and title
            ax.set_xlabel('Planned Duration')
            ax.set_ylabel('Time Counter')
            ax.set_zlabel('Score')
            ax.set_title(f'Score as Planned Duration and Time Counter Vary (Overcrowdedness = {score})')
            
            # Save the plot with the corresponding filename
            filename = os.path.join(output_folder, f'overcrowdedness_{score:.1f}.png')
            plt.savefig(filename)
            plt.close()
            print(f"Plot saved as: {filename}")



    def generate_stay_durations(theta, k, num_samples):
        return np.random.gamma(k, theta, num_samples)
    
your_class_instance = Formulas()
# Base durability for the node
base_durability = 2  # minutes

# Varying theta and k values for the gamma distribution
theta_values = [1]  # Example theta values
k_values = [1,2,3]        # Example k values

# Number of samples to generate
num_samples = 1000

# Plotting the distributions for each combination of theta and k values
plt.figure(figsize=(10, 6))
for theta in theta_values:
    for k in k_values:
        # Calculate mean from theta and k for gamma distribution
        mean_duration = theta * k
        # Generate stay durations
        stay_durations = Formulas.generate_stay_durations(theta, k, num_samples)
        # Plot histogram
        plt.hist(stay_durations, bins=30, alpha=0.5, label=f"Theta={theta}, K={k}")

# Plot formatting
plt.title('Distribution of Stay Durations')
plt.xlabel('Stay Duration (minutes)')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

# Example usage




# Initialize Formulas instance






#time counter code~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define the range of time counters and planned durations
#time_counters = np.arange(1, 21)
#planned_durations = np.arange(1, 21)

# Set the output folder
#output_folder = 'overcrowdedness_plots'

# Plot the 3D surface of score for different overcrowdedness scores and save them
#your_class_instance.plot_score_surface(time_counters, planned_durations,  output_folder)