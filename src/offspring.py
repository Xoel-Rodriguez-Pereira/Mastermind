import random
from colorama import Fore
from reproduction import reproduction
from fitness_function import fitness_function
from select_survivors import select_survivors

def offspring (values, fitness, solution):

    SAMPLE_SIZE = 100
    selected_individuals = random.sample(list(values.keys()), SAMPLE_SIZE)
    weights = list(fitness[individual] for individual in selected_individuals) 

    NUM_CHILDREN = 50
    parents = [random.choices(selected_individuals, weights, k=2) for _ in range(NUM_CHILDREN)]

    chidren_values = reproduction(parents, values)
    children_weights = [fitness_function(solution, chidren_values[child]) for child in range(NUM_CHILDREN)]
    
    generation_values = values + chidren_values
    generation_weights = weights + children_weights

    return select_survivors (generation_values, generation_weights, NUM_CHILDREN)   