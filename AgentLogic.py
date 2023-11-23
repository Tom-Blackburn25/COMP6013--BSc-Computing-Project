

class Agentlogic:
    def __init__(self, graph_network):
        self.Graphnetwork = graph_network
    def get_agent_location(self, agent_id):
        for node in self.Graphnetwork.nodes():
            agents_on_node = self.Graphnetwork.nodes[node]['agents']
            for agent in agents_on_node:
                if agent['id'] == agent_id:
                    return node  # Return the node where the agent is located





if __name__ == "__main__":
    num_agents = 100
    num_steps = 12
    simulation = AgentSimulation(num_agents, num_steps)

    # Initialize agents and run simulation
    simulation.initialize_agents()
    simulation.run_simulation()

    # Get the current location of agent with ID = 5
    agent_id_to_find = 5
    agent_location = simulation.get_agent_location(agent_id_to_find)
    if agent_location is not None:
        print(f"Agent with ID {agent_id_to_find} is currently at node {agent_location}")
    else:
        print(f"Agent with ID {agent_id_to_find} is not found or has no location.")