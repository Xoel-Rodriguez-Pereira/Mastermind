import random
from colorama import Fore
from src.fitness_function import fitness_function

def generation_generator(generation_size, code_lenght, solution):

    pins = (Fore.RED + '𒊹', Fore.GREEN + '𒊹', Fore.BLUE + '𒊹',
            Fore.YELLOW + '𒊹', Fore.MAGENTA + '𒊹', Fore.LIGHTBLUE_EX + '𒊹', 
            Fore.WHITE + '𒊹', Fore.BLACK + '𒊹')


    individual_value = tuple(list(pins[random.randint(0,7)] for _ in range(code_lenght)) for _ in range(generation_size))
    generation = {individual : (individual_value[individual], fitness_function(solution, individual_value[individual])) for individual in range(generation_size)}

    return generation


