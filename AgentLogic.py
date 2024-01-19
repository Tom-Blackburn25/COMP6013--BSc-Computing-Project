import networkx as nx
import random

class Agentlogic:
    def __init__(self, graph_network):
        self.Graphnetwork = graph_network
    def get_agent_location(self, agent_id):
        for node in self.Graphnetwork.nodes():
            agents_on_node = [agent for agent in self.Graphnetwork.nodes[node]['agents'] if agent['current_location'] == node]
            for agent in agents_on_node:
                if agent['id'] == agent_id:
                    return node  # Return the node where the agent is located



    def add_agent_location_history(self, agent_id, current_node, step):
        for node in self.Graphnetwork.nodes():
            agents_on_node = self.Graphnetwork.nodes[node]['agents']
            for agent in agents_on_node:
                if agent['id'] == agent_id:
                    agent['previous_nodes'].append({'node': current_node, 'step': step})
                    return  # Exit loop after appending the location
        print(f"Agent with ID {agent_id} not found or has no location.")  # Print error if agent ID is not found

    def print_agents_location_history(self):
        for node in self.Graphnetwork.nodes():
            agents_on_node = self.Graphnetwork.nodes[node]['agents']
            for agent in agents_on_node:
                print(f"Agent ID: {agent['id']}")
                if agent['previous_nodes']:
                    print("Location History:")
                    for loc in agent['previous_nodes']:
                        print(f"   Node: {loc['node']}, Step: {loc['step']}")
                else:
                    print("No location history available")
                print("\n")    

    def perform_a_star_search(self, current_node, target_node):
        if current_node not in self.Graphnetwork.nodes or target_node not in self.Graphnetwork.nodes:
            print("Invalid nodes for A* search.")
            return None
        try:
            path = nx.astar_path(self.Graphnetwork, current_node, target_node)
            return path
        except nx.NetworkXNoPath:
            print(f"No path found from {current_node} to {target_node}.")
            return None
        
    def decide_new_target_location(self):
        # Define the target locations and their corresponding percentages
        target_locations = {
            7: 6.534152512, #Churchill Exhibition
            6: 8.601373329, #Stables Cafe
            11: 18.90133719, #Retail Toilet
            2: 25.12468377, #Retail Shop
            5: 8.832670763, #Stables Exhibition
            1: 16.55222262, #Pantry
            12: 8.398988074, #Palace Inside 2
            19: 2.13227322, #Stables Female toilet
            14: 1.676906397, #Churchill Male Toilet
            15: 1.539573545, #Churchill Female Toilet
            18: 1.705818576 #Stables Male toilet
        }

        # Normalize percentages to sum up to 1
        total_percentage = sum(target_locations.values())
        normalized_percentages = {location: percent / total_percentage for location, percent in target_locations.items()}

        # Choose a target location based on percentages
        chosen_location = random.choices(list(normalized_percentages.keys()), weights=normalized_percentages.values())[0]

        return chosen_location
    
    def decide_move_or_stay(self, agent):
        time_counter = agent['time_counter']
        random_factor = random.uniform(0, 0.15)
        total_factor = time_counter * random_factor

        return total_factor > 0.5