def select_survivors (generation_values, generation_fitness, NUM_CHILDREN):

    minimum_fitness = set(generation_fitness[:])[NUM_CHILDREN]

    survivors_values_list = [generation_values[individual] for individual in range(len(generation_values)) if generation_fitness[individual] >= minimum_fitness]

    survivors_fitness_list = [generation_fitness[individual] for individual in range(len(survivors_values_list)) if individual == generation_values[individual]]

    survivors_values = {individual : value for individual, value in enumerate(survivors_values_list)}

    survivors_fitness = {individual : fitness for individual, fitness in enumerate(survivors_fitness_list)}

    return survivors_values, survivors_fitness