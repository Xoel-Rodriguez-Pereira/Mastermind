import random
from reproduction import reproduction
from fitness_function import fitness_function
from select_survivors import select_survivors

def offspring (values, fitness, solution):

    NUM_CHILDREN = 50
    parents = [random.choices(list(fitness.keys()), list(fitness.values()), k=2) for _ in range(NUM_CHILDREN)]

    chidren_values = reproduction(parents, values)
    children_fitness = [fitness_function(solution, chidren_values[child]) for child in range(NUM_CHILDREN)]
    
    generation_values = list(values.values()) + chidren_values
    generation_fitness = list(fitness.values()) + children_fitness

    return select_survivors (generation_values, generation_fitness, NUM_CHILDREN)   

