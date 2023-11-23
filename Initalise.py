import networkx as nx
import random
import string
from SaveImages import FileLocator
from AgentLogic import Agentlogic
class AgentSimulation:
    def __init__(self, num_agents, num_steps, outputfolder):
        self.Graphnetwork = nx.Graph()
        self.Graphnetwork.add_node(0, agents=[])
        self.Graphnetwork.add_node(1, agents=[])
        self.Graphnetwork.add_node(2, agents=[])
        self.Graphnetwork.add_node(3, agents=[])
        self.Graphnetwork.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])
        self.num_steps = num_steps
        self.total_agents = num_agents
        self.pos = nx.spring_layout(self.Graphnetwork)
        self.agent_logic = Agentlogic(self.Graphnetwork)  # Create an instance of Agentlogic

    def initialize_agents(self):
        agent_id = 1  # Initialize the agent ID counter
        for _ in range(self.total_agents):
            random_node = random.choice(list(self.Graphnetwork.nodes()))
            agent = {'id': agent_id}
            self.Graphnetwork.nodes[random_node]['agents'].append(agent)
            agent_id += 1  # Increment the agent ID for the next agent

    def run_simulation(self):
        for step in range(self.num_steps):
            print(f"Step {step}:")
            
            # Perform simulation steps here
            for node in self.Graphnetwork.nodes():
                agents_on_node = self.Graphnetwork.nodes[node]['agents']
                for agent in agents_on_node:
                    agent_location = self.agent_logic.get_agent_location(agent['id'])
                    if agent_location is not None:
                        print(f"Agent with ID {agent['id']} is currently at node {agent_location}")
                    else:
                        print(f"Agent with ID {agent['id']} is not found or has no location.")

            #Prints number of agents in a node
            for node in self.Graphnetwork.nodes():
                agents_on_node = self.Graphnetwork.nodes[node]['agents']
                print(f"Node {node}: {len(agents_on_node)} agents")
                for agent in agents_on_node:
                    print(f"   Agent ID: {agent['id']}")
            print("\n")
            


if __name__ == "__main__":
    num_agents = 100
    num_steps = 12
    filelocation = FileLocator.decide_fileLocation("InitalisePrint", num_steps)
    simulation = AgentSimulation(num_agents, num_steps, filelocation)
    simulation.initialize_agents()
    simulation.run_simulation()
    
#tests if the agent locations are correct
    agent_id_to_find = 5
    agent_location = simulation.get_agent_location(agent_id_to_find)
    if agent_location is not None:
        print(f"Agent with ID {agent_id_to_find} is currently at node {agent_location}")
    else:
        print(f"Agent with ID {agent_id_to_find} is not found or has no location.")