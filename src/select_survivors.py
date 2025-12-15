import random
from constants import GENERATION_SIZE

def select_survivors (generation_values, generation_fitness):

    individual_positions = random.choices(range(len(generation_values)), generation_fitness, k=GENERATION_SIZE)

    values = {individual : generation_values[individual] for individual in individual_positions}

    fitness = {individual : generation_fitness[individual] for individual in individual_positions}

    return values, fitness