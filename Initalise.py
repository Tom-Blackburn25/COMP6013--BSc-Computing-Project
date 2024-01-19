import networkx as nx
import random
from SaveImages import FileLocator
from AgentLogic import Agentlogic

class AgentSimulation:
    def __init__(self, num_agents, num_steps, outputfolder):
        self.Graphnetwork = nx.Graph()
        self.node_info = {
            1: "Pantry",
            2: "Retail Shop",
            3: "East Courtyard",
            4: "Palace Inside 1",
            5: "Stables Exhibition",
            6: "Stables Cafe",
            7: "Churchill Exhibition",
            8: "Flagstaff Arch",
            9: "Clock Arch",
            10: "Retail to CV",
            11: "Retail Toilet",
            12: "Palace Inside 2",
            13: "Palace Courtyard",
            14: "Churchill Male Toilet",
            15: "Churchill Female Toilet",
            16: "Formal Gardens",
            17: "West Courtyard",
            18: "Stables Male toilet",
            19: "Stables Female toilet"
        }
        
        self.Graphnetwork.add_nodes_from(self.node_info.keys(), agents=[])
        self.Graphnetwork.add_edges_from([
            (1, 2), (1, 3),
            (2, 1), (2, 3), (2, 11), (2, 10),
            (3, 8), (3, 2), (3, 12),
            (4, 13), (4, 12), (3, 9),
            (5, 15), (5, 6),
            (6, 18), (6, 19), (6, 17),
            (7, 13), (7, 15),
            (8, 3),
            (9, 3), (9, 13),
            (10, 2),
            (11, 2),
            (12, 4), (12, 13),
            (13, 3), (13, 4), (13, 5), (13, 9), (13, 15), (13, 14), (13, 7), (13, 17),
            (14, 13),
            (15, 13),
            (16, 7), (16, 17),
            (17, 16), (17, 6), (17, 13),
            (18, 6),
            (19, 6),
        ])
        self.num_steps = num_steps
        self.total_agents = num_agents
        self.pos = nx.spring_layout(self.Graphnetwork)
        self.agent_logic = Agentlogic(self.Graphnetwork)  # Create an instance of Agentlogic

    def initialize_agents(self):
        agent_id = 1  # Initialize the agent ID counter
        start_node = 8 
        for _ in range(self.total_agents):
            agent = {'id': agent_id, 'previous_nodes': [], 'time_counter': 0, 'path': [], 'current_location': start_node}
            self.Graphnetwork.nodes[start_node]['agents'].append(agent)
            agent_id += 1  # Increment the agent ID for the next agent

    def run_simulation(self):
        for step in range(self.num_steps):
            print("\n")
            print(f"Step {step}:")
            
            # Perform simulation steps here
            for node in self.Graphnetwork.nodes():
                    agents_on_node = [agent for agent in self.Graphnetwork.nodes[node]['agents'] if agent['current_location'] == node]
                    print(agents_on_node)
                    print(node)
                    for agent in agents_on_node:
                        agent_location = self.agent_logic.get_agent_location(agent['id'])
                        if not agent['path']:
                            target_location = self.agent_logic.decide_new_target_location()
                            agent['path'] = self.agent_logic.perform_a_star_search(agent_location, target_location)
                            print(target_location)
                        
                    

                            agent['time_counter'] += 1

                    #self.agent_logic.add_agent_location_history(agent['id'], agent_location, step)
                    #self.agent_logic.print_agents_location_history()
                        else:
                            should_move = self.agent_logic.decide_move_or_stay(agent)

                            if should_move:
                                print("decided to move")
                                path = agent['path']
                                if path[0] == agent["current_location"]:
                                    agent["current_location"] = path[1]
                                    agent["path"] = path[2:]

                                else:                                
                                    agent["current_location"] = path[0]
                                    agent['path'] = path[1:]
                                agent['time_counter'] = 0
                                
                            agent['time_counter'] +=1
                    
            # Prints number of agents in a node
            for node in self.Graphnetwork.nodes():
                agents_on_node = [agent for agent in self.Graphnetwork.nodes[node]['agents'] if agent['current_location'] == node]
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
    
    # Tests if the agent locations are correct
    agent_id_to_find = 5
    agent_location = simulation.agent_logic.get_agent_location(agent_id_to_find)
    if agent_location is not None:
        print(f"Agent with ID {agent_id_to_find} is currently at node {agent_location}")
    else:
        print(f"Agent with ID {agent_id_to_find} is not found or has no location.")