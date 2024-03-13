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
        if step <= 60: # first hour (9 o'clock - 10 o'clock)
            Base_Probability_based_on_visitors = {
            1: 24.64788732,  # Pantry
            2: 37.32394366,  # Retail Shop
            4: 11.97183099,  # Palace Inside 1
            5: 2.816901408,  # Stables Exhibition
            6: 1.877934272,  # Stables Cafe
            7: 1.408450704,  # Churchill Exhibition
            11: 4.460093897,  # Retail Toilet
            12: 1.408450704,  # Palace Inside 2
            14: 0,  # Churchill Male Toilet
            15: 0.234741784,  # Churchill Female Toilet
            17: 10.79812207,  # West Courtyard
            18: 0.704225352,  # Stables Male toilet
            19: 2.34741784  # Stables Female toilet
        }
        if 60 < step <=120: # second hour (10 o'clock - 11 o'clock)
            Base_Probability_based_on_visitors = {
            1: 23.00506033,  # Pantry
            2: 34.21564811,  # Retail Shop
            4: 4.242896069,  # Palace Inside 1
            5: 8.952899961,  # Stables Exhibition
            6: 2.296613468,  # Stables Cafe
            7: 7.940833009,  # Churchill Exhibition
            11: 7.123394317,  # Retail Toilet
            12: 3.269754768,  # Palace Inside 2
            14: 0.350330868,  # Churchill Male Toilet
            15: 0.622810432,  # Churchill Female Toilet
            17: 7.473725185,  # West Courtyard
            18: 0.233553912,  # Stables Male toilet
            19: 0.272479564  # Stables Female toilet
        }
        if 120 < step <=180: # third hour (11 o'clock - 12 o'clock)
            Base_Probability_based_on_visitors = {
            1: 20.46746684,  # Pantry
            2: 26.72141503,  # Retail Shop
            4: 4.358812382,  # Palace Inside 1
            5: 7.285744367,  # Stables Exhibition
            6: 2.295220046,  # Stables Cafe
            7: 9.854706254,  # Churchill Exhibition
            11: 6.780374816,  # Retail Toilet
            12: 12.00252685,  # Palace Inside 2
            14: 0.463255422,  # Churchill Male Toilet
            15: 0.758054327,  # Churchill Female Toilet
            17: 7.369972626,  # West Courtyard
            18: 0.58959781,  # Stables Male toilet
            19: 1.052853232  # Stables Female toilet
        }
        if 180 < step <=240: # fourth hour (12 o'clock - 1 o'clock)
            Base_Probability_based_on_visitors = {
            1: 18.22135573,  # Pantry
            2: 21.59568086,  # Retail Shop
            4: 3.269346131,  # Palace Inside 1
            5: 7.828434313,  # Stables Exhibition
            6: 2.984403119,  # Stables Cafe
            7: 16.15176965,  # Churchill Exhibition
            11: 4.349130174,  # Retail Toilet
            12: 12.32753449,  # Palace Inside 2
            14: 1.484703059,  # Churchill Male Toilet
            15: 1.469706059,  # Churchill Female Toilet
            17: 9.328134373,  # West Courtyard
            18: 0.419916017,  # Stables Male toilet
            19: 0.569886023  # Stables Female toilet
        }
        if 240 < step <=300: # fifth hour (1 o'clock - 2 o'clock)
            Base_Probability_based_on_visitors = {
            1: 23.73098479,  # Pantry
            2: 17.91833467,  # Retail Shop
            4: 3.426741393,  # Palace Inside 1
            5: 4.803843074,  # Stables Exhibition
            6: 2.61008807,  # Stables Cafe
            7: 18.15852682,  # Churchill Exhibition
            11: 4.883907126,  # Retail Toilet
            12: 11.52922338,  # Palace Inside 2
            14: 1.168935148,  # Churchill Male Toilet
            15: 1.024819856,  # Churchill Female Toilet
            17: 8.710968775,  # West Courtyard
            18: 0.64051241,  # Stables Male toilet
            19: 1.393114492  # Stables Female toilet
        }
        if 300 < step <=360: # sixth hour (2 o'clock - 3 o'clock)
            Base_Probability_based_on_visitors = {
            1: 16.68226173,  # Pantry
            2: 28.71273894,  # Retail Shop
            4: 2.392728245,  # Palace Inside 1
            5: 5.77462906,  # Stables Exhibition
            6: 3.515572784,  # Stables Cafe
            7: 17.52439513,  # Churchill Exhibition
            11: 2.780376955,  # Retail Toilet
            12: 9.864991311,  # Palace Inside 2
            14: 1.042641358,  # Churchill Male Toilet
            15: 1.082742949,  # Churchill Female Toilet
            17: 8.795615559,  # West Courtyard
            18: 0.735195829,  # Stables Male toilet
            19: 1.096110146  # Stables Female toilet
        }
        if 360 < step <=420: # seventh hour (3 o'clock - 4 o'clock)
            Base_Probability_based_on_visitors = {
            1: 20.10531355,  # Pantry
            2: 27.38152226,  # Retail Shop
            4: 2.808361257,  # Palace Inside 1
            5: 8.648476145,  # Stables Exhibition
            6: 4.786979416,  # Stables Cafe
            7: 11.72809957,  # Churchill Exhibition
            11: 3.207276209,  # Retail Toilet
            12: 8.871868518,  # Palace Inside 2
            14: 0.73400351,  # Churchill Male Toilet
            15: 0.510611138,  # Churchill Female Toilet
            17: 9.350566459,  # West Courtyard
            18: 0.686133716,  # Stables Male toilet
            19: 1.180788256  # Stables Female toilet
        }
        if 420 < step <=480: # eighth hour (4 o'clock - 5 o'clock)
            Base_Probability_based_on_visitors = {
            1: 24.6978852,  # Pantry
            2: 25,  # Retail Shop
            4: 2.467270896,  # Palace Inside 1
            5: 4.43101712,  # Stables Exhibition
            6: 2.970795569,  # Stables Cafe
            7: 15.25679758,  # Churchill Exhibition
            11: 6.218529708,  # Retail Toilet
            12: 8.056394763,  # Palace Inside 2
            14: 0.83081571,  # Churchill Male Toilet
            15: 0.704934542,  # Churchill Female Toilet
            17: 8.358509567,  # West Courtyard
            18: 0.730110775,  # Stables Male toilet
            19: 0.27693857  # Stables Female toilet
        }
        if 480 < step <= 510: # ninth hour (5 o'clock - 5:30)
            Base_Probability_based_on_visitors = {
            1: 24.51923077,  # Pantry
            2: 2.884615385,  # Retail Shop
            4: 4.326923077,  # Palace Inside 1
            5: 0,  # Stables Exhibition
            6: 13.46153846,  # Stables Cafe
            7: 0,  # Churchill Exhibition
            11: 3.365384615,  # Retail Toilet
            12: 17.30769231,  # Palace Inside 2
            14: 0,  # Churchill Male Toilet
            15: 0.961538462,  # Churchill Female Toilet
            17: 25.96153846,  # West Courtyard
            18: 1.442307692,  # Stables Male toilet
            19: 5.769230769  # Stables Female toilet
        }
        
        for node in visitedNodes:
            if node in Base_Probability_based_on_visitors:
                del Base_Probability_based_on_visitors[node]
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
        
        # Handle the case when an agent has visited all nodes
        if not Base_Probability_based_on_visitors:
                        
            return 8 # Leave Palace


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
