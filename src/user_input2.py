from constants import PINS

def correct_code():
    color_input = input("Introduce el código de 4 colores del mastermind: ")

    starting_silables = ("ro", "v", "az", "am", "ros", "c", "b", "n")
    associated_colours = dict(zip(starting_silables, PINS))

    user_input = color_input.split()
    user_pin_colors = []

    if len(user_input) != 4:
        return print("Código invalido, se necesita 4 colores")

    for item in user_input:
        found = False
        for key in starting_silables:
            if item.lower().startswith(key):
                user_pin_colors.append(associated_colours[key])
                found = True
                break
        if not found:
            return print("Codigo invalido")

    return user_pin_colors
     
