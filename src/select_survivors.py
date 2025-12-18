import random
from src.constants import GENERATION_SIZE

def select_survivors (generation_values, generation_fitness):

    individuals_list = []
    fitness_copy = generation_fitness[:]
    positions = list(range(len(generation_fitness)))
    for _ in range(GENERATION_SIZE):

        chosen_position = random.choices(positions, fitness_copy, k=1)
        individuals_list += chosen_position
        positions[chosen_position[0]].pop()
        fitness_copy[chosen_position[0]].pop()


    values = {individual : generation_values[individual] for individual in individuals_list}

    fitness = {individual : generation_fitness[individual] for individual in individuals_list}

    return values, fitness
