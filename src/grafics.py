import matplotlib.pyplot as plt

def fitness_grafic(generations_almanac, fitness_almanac):
    """
    generations: list of generation numbers (X axis)
    fitness_per_generation: list of lists, where each sublist
                            contains the fitness values of the
                            individuals in that generation
    """

    # Compute total fitness per generation
    total_fitness = [sum(fitness_list) for fitness_list in fitness_almanac]

    # Create the plot
    plt.figure()
    plt.plot(generations_almanac, total_fitness, marker='o', linestyle='-')

    # Labels and title
    plt.xlabel("Generation")
    plt.ylabel("Total Fitness")
    plt.title("Total Fitness per Generation")

    # Show grid and plot
    plt.grid(True)
    plt.show()
    