AskAgain = True
while(AskAgain):
    Nombre = input("Cual es tu nombre?")
    if(Nombre.isdigit()):
        AskAgain = True
    else:
        AskAgain = False
        print(f"Lindo nombre, {Nombre}")
        break
