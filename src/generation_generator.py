


def generation_generator(generation_size, code_lenght):

    generation_individuals = {}

    for individual in generation_size:

        individual_code = list(i for i in code_lenght)
        generation_individuals[individual] = individual_code