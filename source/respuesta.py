from colorama import Fore, init
init(autoreset=True)




def correct_code(color1,color2,color3,color4):

     print("Introduce el código de 4 colores del mastermind")
     Starting_silables=("roj","ama","ver","azu","ros","neg","bla","cel")
     PINS = (Fore.RED + '𒊹', Fore.YELLOW + '𒊹', Fore.GREEN + '𒊹', Fore.BLUE + '𒊹',
            Fore.MAGENTA + '𒊹', Fore.BLACK + '𒊹', Fore.WHITE + '𒊹', Fore.LIGHTCYAN_EX + '𒊹')
     associated_colours= dict(zip(Starting_silables,PINS))
     
     user_input=[color1,color2,color3,color4]
   
     user_pin_colors=[]
    
     for item in user_input:
     
          for key in Starting_silables:
               if item.lower().find(key)==0:
                    user_pin_colors+=[associated_colours[key]]
    
     if len (user_pin_colors) <len(user_input):
       
          print("Codigo invalido")
     


     return user_pin_colors











