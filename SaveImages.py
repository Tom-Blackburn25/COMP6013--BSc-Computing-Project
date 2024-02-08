import os
import matplotlib.pyplot as plt

class FileLocator: 
    def decide_fileLocation(name_of_file, num_of_steps ):
        ImagePrintLocation = name_of_file
        os.makedirs(ImagePrintLocation, exist_ok=True)
        image_name = f'step_{num_of_steps}.png'
        image_path = os.path.join(ImagePrintLocation, image_name)
        return image_path
        
    #plt.savefig(image_path)  The saving of the file command

    def Save(FileLocation):
        plt.savefig(FileLocation)