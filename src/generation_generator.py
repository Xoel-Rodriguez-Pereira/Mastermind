import random
from colorama import Fore
from fitness_function import fitness_function

def generation_generator(code_lenght, solution):

    pins = (Fore.RED + '𒊹', Fore.GREEN + '𒊹', Fore.BLUE + '𒊹',
            Fore.YELLOW + '𒊹', Fore.MAGENTA + '𒊹', Fore.LIGHTBLUE_EX + '𒊹', 
            Fore.WHITE + '𒊹', Fore.BLACK + '𒊹')

    GENERATION_SIZE = 200

    individual_value = tuple(list(pins[random.randint(0,7)] for _ in range(code_lenght)) for _ in range(GENERATION_SIZE))
    values = {individual : individual_value[individual] for individual in range(GENERATION_SIZE)}
    fitness = {individual : fitness_function(solution, individual_value[individual]) for individual in range(GENERATION_SIZE)}

    return values, fitness


