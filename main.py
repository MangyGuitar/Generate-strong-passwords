import os
import json
import random
import string

try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")

colorama.init()



config = json.load(open("config.json"))
max_characters = int(config["Characters"]["Maxium"])
min_characters = int(config["Characters"]["Minium"])
letters = config["Containers"]["Letters"]
numbers = config["Containers"]["Numbers"]
symbols = config["Containers"]["Symbols"]
characters = ""
generate_many_password = config["Extra"]["Generate_many_passwords"]

def json_config():
    global characters
    characters = ""
    if letters or numbers or symbols:
        if letters:
            characters += string.ascii_letters
        if numbers:
            characters += string.digits
        if symbols:
            characters += string.punctuation


def txtfile():
    if config["Extra"]["Generate_many_passwords"] == True:
        with open("passwords.txt", "a") as f:
            for i in range(config["Extra"]["How_many_passwords"]):
                password = gen_password()
                f.write(password + "\n")
    else:
        print("Failed, pls contact the developer")

def gen_password():
    if max_characters < min_characters or min_characters > max_characters or min_characters <= 0:
       input(colorama.Fore.RED + "ERROR, check " + colorama.Fore.MAGENTA +"CONFIG.JSON" + colorama.Fore.RED + ", press enter to exit...")
       exit()  
    else:
        contraseña = "".join(random.choice(characters) for i in range(max_characters))
        return contraseña
    
json_config()
def main():
    if generate_many_password == True:
        print(colorama.Fore.MAGENTA + "-----------------------\n "
        + colorama.Fore.RED + " Generador de Contraseñas: \n "
        + colorama.Fore.CYAN + " Check the file passwords.txt"
        + colorama.Fore.MAGENTA + "\n -----------------------")
        txtfile()
    else:
        print(colorama.Fore.MAGENTA + "-----------------------\n "
        + colorama.Fore.RED + " Generador de Contraseñas: \n "
        + colorama.Fore.BLUE + " " + gen_password() 
        + colorama.Fore.MAGENTA + "\n -----------------------")

main()


finish = input("Press enter to exit...")
