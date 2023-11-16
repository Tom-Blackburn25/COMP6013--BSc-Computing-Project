
if __name__ == "__main__":
    num_agents = 100
    num_steps = 12
    simulation = AgentSimulation(num_agents, num_steps)
    simulation.initialize_agents()
    simulation.run_simulation()