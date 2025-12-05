import random
from colorama import Fore

def generation_generator(generation_size, code_lenght):

    pins = (Fore.RED + '𒊹', Fore.GREEN + '𒊹', Fore.BLUE + '𒊹',
            Fore.YELLOW + '𒊹', Fore.MAGENTA + '𒊹', Fore.LIGHTBLUE_EX + '𒊹', 
            Fore.WHITE + '𒊹', Fore.BLACK + '𒊹')

    generation = {individual : list(pins[random.randint(0,7)] for _ in range(code_lenght)) for individual in range(generation_size)}

    return generation
