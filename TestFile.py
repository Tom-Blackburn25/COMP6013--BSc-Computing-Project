from Initalise import AgentSimulation
from SaveImages import FileLocator

if __name__ == "__main__":
    num_agents = 100
    num_steps = 12
    Filelocation = "graph_images"
    ImagePath = FileLocator.decide_fileLocation(Filelocation,num_steps)
    print(ImagePath)

    #ImagePath = 



    simulation = AgentSimulation(num_agents, num_steps, ImagePath)
    simulation.initialize_agents()
    simulation.run_simulation()


#plt.savefig(image_path)
    