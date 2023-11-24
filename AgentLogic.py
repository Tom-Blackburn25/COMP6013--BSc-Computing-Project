

class Agentlogic:
    def __init__(self, graph_network):
        self.Graphnetwork = graph_network
    def get_agent_location(self, agent_id):
        for node in self.Graphnetwork.nodes():
            agents_on_node = self.Graphnetwork.nodes[node]['agents']
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

