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

#to test file locations
#agent_id_to_find = 5
    #agent_location = simulation.get_agent_location(agent_id_to_find)
    #if agent_location is not None:
       # print(f"Agent with ID {agent_id_to_find} is currently at node {agent_location}")
   # else:
     #   print(f"Agent with ID {agent_id_to_find} is not found or has no location.")

#plt.savefig(image_path)
    