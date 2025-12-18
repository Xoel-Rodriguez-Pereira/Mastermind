from src.constants import PINS


def correct_code():

    color_input= input("Introduce el código de 4 colores del mastermind: ")
    
    starting_silables=("roj","v","az","am","ros","c","b","n",)
    associated_colours= dict(zip(starting_silables,PINS))

    user_input=color_input.split()
    user_pin_colors=[]

    if len(user_input) != 4:
         return print("Código invalido, se necesita 4 colores")

    for item in user_input:
     
          for key in starting_silables:
               if item.lower().find(key)==0:
                    user_pin_colors+=[associated_colours[key]]
    
    if len (user_pin_colors) <len(user_input):
       
          return print("Codigo invalido")

    return user_pin_colors



