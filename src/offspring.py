import random
from colorama import Fore
from generation_generator import generation_generator

def offspring (values, fitness):

    SAMPLE_SIZE = 100
    selected_individuals = random.sample(list(values.keys()), SAMPLE_SIZE)
    weights = list(fitness[individual] for individual in selected_individuals) 

    NUM_CHILDREN = 50
    parents = [random.choices(selected_individuals, weights, k=2) for _ in range(NUM_CHILDREN)]

    return parents

