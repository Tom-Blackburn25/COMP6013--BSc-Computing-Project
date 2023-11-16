# RUN IN TERMINAL ~ pip install numpy matplotlib networkx
#Randomly assigned to the grid and all agents randomly move
import os
import random
import networkx as nx
import matplotlib.pyplot as plt


output_folder = 'graph_images'
os.makedirs(output_folder, exist_ok=True)



# Create the network graph
Graphnetwork = nx.Graph()
Graphnetwork.add_node(0, num_of_agents=0)
Graphnetwork.add_node(1, num_of_agents=0)
Graphnetwork.add_node(2, num_of_agents=0)
Graphnetwork.add_node(3, num_of_agents=0)
Graphnetwork.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])

# Set the number of simulation steps
num_steps = 12

# Set the graph layout and have it remain the same
pos = nx.spring_layout(Graphnetwork)

# Initialize 100 agents randomly placed on the graph
total_agents = 100

for _ in range(total_agents):
    random_node = random.choice(list(Graphnetwork.nodes()))
    Graphnetwork.nodes[random_node]['num_of_agents'] += 1

# Movement of agents
for step in range(1, num_steps + 1):
    print(f"Step {step}:")
    for node in Graphnetwork.nodes():
        num_agents_in_node = Graphnetwork.nodes[node]['num_of_agents']

        for _ in range(num_agents_in_node):
            # Each agent independently decides to move with a 50/50 chance
            if random.choice([True, False]):
                neighbors = list(Graphnetwork.neighbors(node))
                if neighbors:  # Check if the node has neighbors
                    new_location = random.choice(neighbors)
                    Graphnetwork.nodes[node]['num_of_agents'] -= 1
                    Graphnetwork.nodes[new_location]['num_of_agents'] += 1

    # Print the current locations of agents
    for node, agents in Graphnetwork.nodes(data='num_of_agents'):
        print(f"Node {node}: {agents} agents")

    # Visualize the network and agent counts at each node
    # Draw the network
    nx.draw(Graphnetwork, pos, with_labels=True, node_size=200, node_color='lightblue')

    labels = {node: f"{agents}" for node, agents in Graphnetwork.nodes(data='num_of_agents')}
    label_pos = {k: (v[0], v[1] + 0.05) for k, v in pos.items()}
    nx.draw_networkx_labels(Graphnetwork, label_pos, labels=labels)

    plt.title(f'Step {step}')

    image_name = f'step_{step}.png'
    image_path = os.path.join(output_folder, image_name)
    plt.savefig(image_path)

    plt.show()