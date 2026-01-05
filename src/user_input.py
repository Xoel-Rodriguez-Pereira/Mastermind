from src.constants import PINS


def correct_code():
<<<<<<< HEAD

    color_input= input("Introduce el código de 4 colores del mastermind.\n" \
     "--------------------------------------------------------------------\n" \
    "COLORES DISPONIBLES: Rojo, verde, azul, amarillo, rosa, celeste, blanco, negro\n" \
     "Escribe los colores separados por espacios: ")
=======
>>>>>>> refactor
    
    starting_silables = ("roj", "v", "az", "am", "ros", "c", "b", "n")
    associated_colours = dict(zip(starting_silables, PINS))
    user_pin_colors = []
    
    is_code_valid = False
    while is_code_valid == False:
         
        color_input = input("Introduce el código de 4 colores del mastermind: ")
        user_input = color_input.split()

        if len(user_input) != 4:

            print("Código invalido, se necesita 4 colores")

        else:
            for item in user_input:
            
                for key in starting_silables:

                    if item.lower().find(key) == 0:
                            user_pin_colors += [associated_colours[key]]
            
            if len (user_pin_colors) < len(user_input):
            
                print("Codigo invalido")

            else:
                is_code_valid = True

    return user_pin_colors



