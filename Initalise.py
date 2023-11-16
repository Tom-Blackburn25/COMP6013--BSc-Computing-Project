import networkx as nx
import random
import string

class AgentSimulation:
    def __init__(self, num_agents, num_steps):
        self.Graphnetwork = nx.Graph()
        self.Graphnetwork.add_node(0, agents=[])
        self.Graphnetwork.add_node(1, agents=[])
        self.Graphnetwork.add_node(2, agents=[])
        self.Graphnetwork.add_node(3, agents=[])
        self.Graphnetwork.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])
        self.num_steps = num_steps
        self.total_agents = num_agents
        self.pos = nx.spring_layout(self.Graphnetwork)

    def initialize_agents(self):
        agent_id = 1  # Initialize the agent ID counter
        for _ in range(self.total_agents):
            random_node = random.choice(list(self.Graphnetwork.nodes()))
            agent = {'id': agent_id}
            self.Graphnetwork.nodes[random_node]['agents'].append(agent)
            agent_id += 1  # Increment the agent ID for the next agent

    def run_simulation(self):
        for step in range(self.num_steps):
            # Perform simulation steps here
            
            #Prints number of agents in a node
            print(f"Step {step}:")
            for node in self.Graphnetwork.nodes():
                agents_on_node = self.Graphnetwork.nodes[node]['agents']
                print(f"Node {node}: {len(agents_on_node)} agents")
                for agent in agents_on_node:
                    print(f"   Agent ID: {agent['id']}")
            print("\n")

            
if __name__ == "__main__":
    num_agents = 100
    num_steps = 12
    simulation = AgentSimulation(num_agents, num_steps)
    simulation.initialize_agents()
    simulation.run_simulation()