import random
from src.constants import PINS

def mutation (children_values):

    for child in children_values:

        if random.randint(1, 200) == 1: # 0.5% de probabilidad de mutar

            gene = random.choice(range(len(child))) # selecciona la posicion de un gen aleatorio
            options = set(PINS) - set([child[gene]])
            child[gene] = random.choice(list(options))
