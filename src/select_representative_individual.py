import random

def select_representative_individual (values, fitness, solutions_history):

    max_generation_fitness = max(fitness.values())

    for _ in range(20): ## Da 5 oportunidades de encontrar un individuo que no esté en el registro

        representative_individual = random.choice([individual for individual, fitness_weight in fitness.items() if fitness_weight == max_generation_fitness])

        representative_individual_value = random.choice([individual_value for individual, individual_value in values.items() if individual == representative_individual])

        if [(representative_individual_value, max_generation_fitness)] not in solutions_history:

            return [(representative_individual_value, max_generation_fitness)]
