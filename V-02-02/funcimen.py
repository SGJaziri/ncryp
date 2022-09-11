from pyfiglet import figlet_format

def title_prim():
    print(figlet_format(" NCRYP ", font="puffy"))

def menu_s():
    title_prim()
    print("[0] ----------> ENCRIPTAR UN MENSAJE")
    print("[1] --> DESCIFRAR UN MENSAJE CIFRADO")
    print("[2] -------------------------> SALIR")
    print("")

def pros_sl():
    print("")
    print("---> PROCESANDO LA SOLICITUD <---")
    print("")

def mostrar_f(first, second):
    title_prim()
    print("----> EN HORA BUENA, SE HA REALIZADO SU OPERACION<----")
    print("------------------------------------------------------")
    print("--------> LA FRASE INGRESADA ES LA SIGUIENTE <--------")
    print("")
    print("--> " + first)
    print("------------------------------------------------------")
    print("LA FRASE OBTENIDA A PARTIR DEL SISTEMA ES LA SIGUIENTE")
    print("")
    print("--> " + second)

def thanks():
    print("")
    print("GRACIAS POR UTILIZAR EL SISTEMA 7w7")
    print("")

def men_recov():
    print("")
    print("--------------------------")
    print(" DESEA VOLVER AL INICIO?? ")
    print("--------------------------")
    print("")
    print("[0] --> SI ")
    print("[1] --> NO")
    print("")
    while True:
        try:
            comeback = int(input(""))
            if comeback in range(0, 2):
                return(comeback)
            else:
                print("")
                print("POR FAVOR INGRESE UNA OPCION CORRECTA")
                print("")
        except :
            print("")
            print("--> POR FAVOR, INGRESE UN CARACTER NUMERICO <--")
            print("")

def men_export():
    print("")
    print("--------------------------------------------------")
    print(" DESEA OBTENER EN UN ARCHIVO DE TEXTO EL CODIGO?? ")
    print("--------------------------------------------------")
    print("")
    print("[0] --> SI ")
    print("[1] --> NO")
    print("")
    while True:
        try:
            comeback = int(input(""))
            if comeback in range(0, 2):
                return(comeback)
            else:
                print("")
                print("POR FAVOR INGRESE UNA OPCION CORRECTA")
                print("")
        except :
            print("")
            print("--> POR FAVOR, INGRESE UN CARACTER NUMERICO <--")
            print("")

def men_export1():
    print("")
    print("-----------------------------------------------------------------")
    print(" DESEA OBTENER LA CLAVE CIFRADA DEL ARCHIVO DE TEXTO ALMACENADO??")
    print("-----------------------------------------------------------------")
    print("")
    print("[0] --> SI ")
    print("[1] --> NO")
    print("")
    while True:
        try:
            comeback = int(input(""))
            if comeback in range(0, 2):
                return(comeback)
            else:
                print("")
                print("POR FAVOR INGRESE UNA OPCION CORRECTA")
                print("")
        except :
            print("")
            print("--> POR FAVOR, INGRESE UN CARACTER NUMERICO <--")
            print("")

def men_o():
    print("")
    print("--------------")
    print("CLAVE OBTENIDA")
    print("--------------")
    print("")