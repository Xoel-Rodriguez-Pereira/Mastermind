from src.constants import MAX_GENERATIONS
from colorama import Fore

def print_solutions(solutions_history, generation):
    
    selected_code_string = ' '.join(item for item in solutions_history[-1][0])

    if solutions_history[-1][1] == 8:

        print ('''Se ha adivinado el código
{0} {1} {2}          
en {3} intentos.'''.format(selected_code_string, Fore.RESET + '|',solutions_history[-1][1], generation))
        
    elif generation < MAX_GENERATIONS:
        
        print (''' Intento: {3}
{0} {1} {2}'''.format(selected_code_string, Fore.RESET + '|',solutions_history[-1][1], generation))

    elif generation >= MAX_GENERATIONS:

        print ('No se ha podido adivinar el código')


if __name__ == '__main__':

    from colorama import Fore

    print_solutions([([Fore.RED + '𒊹', Fore.RED + '𒊹', Fore.RED + '𒊹', Fore.RED + '𒊹'],8)], 4)
    print_solutions([([Fore.BLUE + '𒊹', Fore.RED + '𒊹', Fore.BLUE + '𒊹', Fore.RED + '𒊹'],4)], 7)
    print_solutions([([Fore.RED + '𒊹', Fore.RED + '𒊹', Fore.RED + '𒊹', Fore.RED + '𒊹'],0)], 12)
