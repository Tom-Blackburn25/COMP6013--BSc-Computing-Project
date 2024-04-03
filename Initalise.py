import networkx as nx
import random
import os
import sys
from SaveImages import FileLocator
from AgentLogic import Agentlogic
import matplotlib.pyplot as plt
import numpy as np

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
            10: "Retail to CoV",
            11: "Retail Toilet",
            12: "Palace Inside 2",
            13: "Palace Courtyard",
            14: "Churchill Male Toilet",
            15: "Churchill Female Toilet",
            16: "Formal Gardens",
            17: "West Courtyard",
            18: "Stables Male toilet",
            19: "Stables Female toilet",
            20: "East Courtyard Seating",
        }
        
        self.Graphnetwork.add_nodes_from(self.node_info.keys(), agents=[])
        self.Graphnetwork.add_edges_from([
            (1, 2), (1, 3),
            (2, 1), (2, 3), (2, 11), (2, 10),
            (3, 8), (3, 2), (3,20),
            (4, 13), (4, 12), (3, 9),
            (5, 13), (5, 6),
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
            (20,3)
        ])
        
        
        #placing the nodes
        self.node_positions = {
            1: (-5,-2),
            2: (-3,-2),
            3: (-4,0),
            4: (-0.2,5),
            5: (3,-1),
            6: (4,-1.5),
            7: (1.5,6),
            8: (-6,0),
            9: (-2,0),
            10: (-3,-1),
            11: (-1,-2),
            12: (0.75,7),
            13: (0,0),
            14: (1.5,4.75),
            15: (2,4),
            16: (3.5,3.5),
            17: (4,0),
            18: (5,-0.85),
            19: (5,-2.15),
            20: (-4,0.75)
        }



        self.num_steps = num_steps
        self.total_agents = num_agents
        self.outputfolder = outputfolder
        self.pos = self.node_positions
        self.agent_logic = Agentlogic(self.Graphnetwork)  # Create an instance of Agentlogic
        self.time_series_data = []

    
        
    
    

  
    
    def add_agents(self,numberOfAgentsToAdd,currentAgentId):
        agent_id = currentAgentId # Initialize the agent ID counter
        start_node = 8 
        numAgents = numberOfAgentsToAdd
        for _ in range(numAgents):
            agent = {
            'id': agent_id,
            'previous_nodes': [],
            'last_node': [8],
            'time_counter': 0,
            'Apath': [],
            'current_location': start_node,
            'time_in_palace': 0,
            'visited_count': {node: 0 for node in self.Graphnetwork.nodes},
            'leaving' : 0,
            'planned_duration': 0
            }
            self.Graphnetwork.nodes[start_node]['agents'].append(agent)
            agent_id += 1  # Increment the agent ID for the next agent
        return agent_id

    def distribute_agents(self,step):
        if step <= 60: # first hour (9 o'clock - 10 o'clock)
            agentsacrossthehour = 144
        if 60 < step <=120: # second hour (10 o'clock - 11 o'clock)
            agentsacrossthehour = 404
        if 120 < step <=180: # third hour (11 o'clock - 12 o'clock)
            agentsacrossthehour = 732
        if 180 < step <=240: # fourth hour (12 o'clock - 1 o'clock)
            agentsacrossthehour = 746
        if 240 < step <=300: # fifth hour (1 o'clock - 2 o'clock)
            agentsacrossthehour = 852
        if 300 < step <=360: # sixth hour (2 o'clock - 3 o'clock)
            agentsacrossthehour = 892
        if 360 < step <=420: # seventh hour (3 o'clock - 4 o'clock)
            agentsacrossthehour = 900
        if 420 < step <=480: # eighth hour (4 o'clock - 5 o'clock)
            agentsacrossthehour = 538
        if 480 < step <= 510: # ninth hour (5 o'clock - 5:30)
            agentsacrossthehour = 166


        mean_agents_per_step = agentsacrossthehour / 60  # Mean number of agents per step
        std_dev = np.sqrt(mean_agents_per_step)  # Standard deviation
    
    # Generate the number of agents to add to each step
        agents_per_step = np.random.normal(mean_agents_per_step, std_dev, 60).astype(int)
        agents_per_step = np.clip(agents_per_step, 0, None)
        return agents_per_step


    def run_simulation(self):
        agent_id_setter = 0
        distributed_agents = None
        for step in range(self.num_steps):
            print("\n")
            print(f"Step {step}:")

            if step % 60 == 0:
                distributed_agents = self.distribute_agents(step)

            if distributed_agents is not None:
                agents_to_add = distributed_agents[step % 60]
                agent_id_setter = self.add_agents(agents_to_add, agent_id_setter)


            

            agents_on_nodes = {node: 0 for node in self.Graphnetwork.nodes()}

            # Perform simulation steps here
            for node in self.Graphnetwork.nodes():
                    agents_on_node = [agent for agent in self.Graphnetwork.nodes[node]['agents'] if agent['current_location'] == node]
                    agents_on_nodes[node] = len(agents_on_node)

                    nx.set_node_attributes(self.Graphnetwork, {node: {'time_step': step, 'agents_count': agents_on_nodes[node]}})


                    for agent in agents_on_node:
                        agent['time_in_palace'] += 1
                        current_location = agent['current_location']
                        last_node = agent['last_node']
                        if agent['time_in_palace'] < 1:
                            self.agent_logic.update_last_node(agent['id'], agent["current_location"])
                        if current_location != last_node:
                            agent['visited_count'][current_location] += 1
                        
                        

                        agent_location = self.agent_logic.get_agent_location(agent['id'])
                        if not agent['Apath']:
                            visitedNodes = []

                            for node, count in agent['visited_count'].items():
                                 if count > 0:
                                    visitedNodes.append(node)

                            
                            target_location = self.agent_logic.decide_new_target_location(agent,step,visitedNodes)
                            if target_location == 8:
                                agent['leaving'] = 1
                            
                            agent['Apath'] = self.agent_logic.perform_a_star_search(agent_location, target_location)
                            print("Agent:", agent['id'] ,"is routing to" , target_location)
                            agent['planned_duration'] = self.agent_logic.decide_duration(agent)
                            

                            agent['time_counter'] += 1
                        
                        else:
                            if agent['planned_duration'] > agent['time_counter']:
                                numofagents = agents_on_nodes[node]
                                overcrowededScore = self.agent_logic.overcrowededcheck(node,numofagents)
                                
                            should_move = self.agent_logic.decide_move_or_stay(agent)
                            
                            if agent['leaving'] == 1 and agent['current_location'] == 8:
                                self.agent_logic.remove_agent_from_graph(agent)
                            elif should_move:
                                print("decided to move")
                                Apath = agent['Apath']
                                if Apath[0] == agent["current_location"]: 
                                    if len(Apath) > 1:
                                        self.agent_logic.update_last_node(agent['id'], agent["current_location"])
                                        agent["current_location"] = Apath[1]
                                        agent["Apath"] = Apath[2:]
                                    else:
                                        target_location = self.agent_logic.decide_new_target_location(agent, step, visitedNodes)
                                        if target_location ==8:
                                            agent['leaving'] = 1
                                        agent_location = agent["current_location"]
                                        agent['Apath'] = self.agent_logic.perform_a_star_search(agent_location, target_location)                                    

                                    
                                    

                                else:                                
                                    self.agent_logic.update_last_node(agent['id'], agent["current_location"])
                                    agent["current_location"] = Apath[0]
                                    agent['Apath'] = Apath[1:]
                                agent['time_counter'] = 0

                            agent['time_counter'] +=1
                    
            # Prints number of agents in a node
            self.time_series_data.append(agents_on_nodes.copy())


            for node in self.Graphnetwork.nodes():
                agents_on_node = [agent for agent in self.Graphnetwork.nodes[node]['agents'] if agent['current_location'] == node]
                print(f"Node {node}: {len(agents_on_node)} agents")
                for agent in agents_on_node:
                    print(f"   Agent ID: {agent['id']}")
            print("\n")



            if step % 20 == 0:
                self.save_graph(step)

        
                


    def plot_time_series(self):
        time_steps = range(self.num_steps)
        nodes = list(self.node_info.keys())
        output_folder = "time_series_plot"
        os.makedirs(output_folder, exist_ok=True)
        # Create a plot for each node
        for node in nodes:
            agents_counts = [data[node] for data in self.time_series_data]
            plt.plot(time_steps, agents_counts)
            plt.xlabel("Time Step")
            plt.ylabel("Number of Agents")
            plt.title(f"Node {node} - Number of Agents Over Time")
            output_path = os.path.join(output_folder, f"node_{node}_plot.png")
            plt.savefig(output_path)
            plt.close()
        plt.figure()
        for node in nodes:
            agents_counts = [data[node] for data in self.time_series_data]
            plt.plot(time_steps, agents_counts, label=f"Node {node}")

        plt.xlabel("Time Step")
        plt.ylabel("Number of Agents")
        plt.title("Number of Agents on Each Node Over Time")
        plt.legend()
        
        # Save the combined plot
        output_path_combined = os.path.join(output_folder, "combined_plot.png")
        plt.savefig(output_path_combined)
        
        # Show the combined plot
        plt.show()
                
    def save_graph(self, step):
        # Create a filename for the saved graph using the step number
        filename = f"graph_step_{step}.png"

        # Create the full path for saving the image
        output_path = os.path.join(self.outputfolder, filename)

        # Ensure the output folder exists before saving the file
        os.makedirs(self.outputfolder, exist_ok=True)

        # Plot and save the graph using matplotlib
        plt.figure(figsize=(10, 8))
        nx.draw(self.Graphnetwork, pos=self.pos, with_labels=False, node_color='lightblue', node_size=250,)
        for node, label in self.node_info.items():
            agents_on_node = [agent for agent in self.Graphnetwork.nodes[node]['agents'] if agent['current_location'] == node]
            total_agents = len(agents_on_node)
            # Display total agents slightly lower
            plt.text(self.pos[node][0], self.pos[node][1] - 0.2, f"Total Agents: {total_agents}", ha='center', va='center')

            # Display node name above the node
            plt.text(self.pos[node][0], self.pos[node][1] + 0.1, label, ha='center', va='center')

        plt.title(f"Agent Simulation - Step {step}")
        plt.savefig(output_path)
        plt.close()     

    def plot_distribution(self):
        for node, label in self.node_info.items():
            durations = self.agent_logic.get_stay_durations(node)

            # Plot histogram
            plt.hist(durations, bins=20, alpha=0.7, color='blue')
            plt.xlabel('Stay Duration')
            plt.ylabel('frequency')
            plt.title(f'Distribution of Stay Durations for Node {label}')
            plt.show()
        
        # Save data to a file
            filename = f"{node}_stay_distribution.txt"
            with open(filename, 'w') as file:
                for duration in durations:
                    file.write(f"{duration}\n")
            print(f"Data saved to {filename}")    


if __name__ == "__main__":
    num_agents = 100 #Total avg People per Day 3837  /   100 is testing number
    num_steps = 510 # 8.5 hours of visiting times starting at 9 ending 5:30

    filelocation = FileLocator.decide_fileLocation("InitalisePrint", num_steps)
    if filelocation is None or filelocation == "":
        print("Error: filelocator is empty. Exiting program.")
        sys.exit()
    simulation = AgentSimulation(num_agents, num_steps, filelocation)
    
    simulation.run_simulation()
    simulation.plot_time_series()
    simulation.plot_distribution()
    
    # Tests if the agent locations are correct
    agent_id_to_find = 5
    agent_location = simulation.agent_logic.get_agent_location(agent_id_to_find)
    if agent_location is not None:
        print(f"Agent with ID {agent_id_to_find} is currently at node {agent_location}")
    else:
        print(f"Agent with ID {agent_id_to_find} is not found or has no location.")