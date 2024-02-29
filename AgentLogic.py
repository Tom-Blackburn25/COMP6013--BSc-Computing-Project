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
                

    def remove_agent_from_graph(self, agent):
        current_location = agent['current_location']
        self.Graphnetwork.nodes[current_location]['agents'].remove(agent)


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
        
    def decide_new_target_location(self, agent, step ,visitedNodes):
        Base_Probability_based_on_visitors = {
            1: 16.55222262,  # Pantry
            2: 25.12468377,  # Retail Shop
            5: 8.832670763,  # Stables Exhibition
            6: 8.601373329,  # Stables Cafe
            7: 6.534152512,  # Churchill Exhibition
            11: 18.90133719,  # Retail Toilet
            12: 8.398988074,  # Palace Inside 2
            14: 1.676906397,  # Churchill Male Toilet
            15: 1.539573545,  # Churchill Female Toilet
            18: 1.705818576,  # Stables Male toilet
            19: 2.13227322  # Stables Female toilet
        }
        visited_nodes = set(agent['visited_count'].keys())

    # Filter out visited nodes from base probabilities
        
    # Leave Palace decision logic
        
        time_in_palace_factor = agent['time_in_palace'] / 210  # Normalize time in palace to range 0-1
        stepchance = 0
        if step > 300:
             stepchance = ((step - 300) / 300)

        total_chance = time_in_palace_factor + stepchance
        
        if total_chance > 1:
            total_chance = 1    

        if random.random() < total_chance:
            return 8  # Leave Palace

    

    # Normalize percentages to sum up to 1 for unvisited nodes
        total_percentage_unvisited = sum(Base_Probability_based_on_visitors.values())
        normalized_percentages_unvisited = {location: prob / total_percentage_unvisited for location, prob in Base_Probability_based_on_visitors.items()}

    # Choose a target location based on percentages for unvisited nodes
        chosen_location = random.choices(list(normalized_percentages_unvisited.keys()), weights=normalized_percentages_unvisited.values())[0]

        return chosen_location

    def decide_move_or_stay(self, agent):
        time_counter = agent['time_counter']
        random_factor = random.uniform(0, 0.15)
        total_factor = time_counter * random_factor
        return total_factor > 0.5
    
    
    def update_last_node(self, agent_id, current_node):
        for node in self.Graphnetwork.nodes():
            agents_on_node = [agent for agent in self.Graphnetwork.nodes[node]['agents'] if agent['current_location'] == node]
            for agent in agents_on_node:
                if agent['id'] == agent_id:
                    agent['last_node'] = [current_node]
                    return  # Exit loop after updating the previous node
        print(f"Agent with ID {agent_id} not found or has no location.")  # Print error if agent ID is not found
