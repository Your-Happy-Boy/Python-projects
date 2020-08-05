AskAgain = True
while(AskAgain):
    Nombre = input("Cual es tu nombre?")
    if(Nombre.isdigit()):
        print("Uh... ¿Estas seguro? Dejame preguntar de nuevo")
        AskAgain = True
    else:
        AskAgain = False
        print(f"Lindo nombre, {Nombre}")
        break
