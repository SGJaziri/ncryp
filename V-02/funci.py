from os import system
from time import sleep

def dicc():
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    diccionario = {}
    for x in abecedario:
        value = ord(x)
        value_n = (value - 97)
        if value_n == 144:
            value_n = (value_n - 130)
        else:
            if value_n > 13:
                value_n = (value_n + 1)
        diccionario[x] = value_n
    return(diccionario)

def menu_p():
    print("")
    print("Hola :D, con la ayuda de esta herramienta podran encriptar de una manera sencilla")
    print("sus fraces, asi que comencemos 7w7")
    print("")
    print("Selecciona una de las 3 opciones que tenemos dentro del Script :3")
    print("")
    print("[0] ----------> ENCRIPTAR UN MENSAJE")
    print("[1] --> DESCIFRAR UN MENSAJE CIFRADO")
    print("[2] -------------------------> SALIR")
    print("")
    while True:
        try:
            elec = int(input("Cual de las opciones desea escoger : "))
            if elec in range(0, 3):
                return(elec)
            else:
                print("")
                print("POR FAVOR INGRESE UNA OPCION CORRECTA")
                print("")
                time_out_f(1.5)
                menu_s()
        except :
            print("")
            print("--> POR FAVOR, INGRESE UN CARACTER NUMERICO <--")
            print("")
            time_out_f(1.25)
            menu_s()

def time_out_f(slep):
    sleep(slep)
    system("clear")

def menu_s():
    print("")
    print("-----------> NCRYP V2.0 <-----------")
    print("")
    print("[0] ----------> ENCRIPTAR UN MENSAJE")
    print("[1] --> DESCIFRAR UN MENSAJE CIFRADO")
    print("[2] -------------------------> SALIR")
    print("")

def find(abecedario, v):
        for k in abecedario:
            if abecedario[k] == v:
                return k

def pros_sl():
    print("")
    print("---> PROCESANDO LA SOLICITUD <---")
    print("")

def mostrar_f(first, second):
    print("")
    print("----> EN HORA BUENA, SE HA REALIZADO SU OPERACION<----")
    print("------------------------------------------------------")
    print("--------> LA FRASE INGRESADA ES LA SIGUIENTE <--------")
    print("")
    print("--> " + first)
    print("------------------------------------------------------")
    print("LA FRASE OBTENIDA A PARTIR DEL SISTEMA ES LA SIGUIENTE")
    print("")
    print("--> " + second)

def cifrar():
    print("")
    abecedario = dicc()
    text = input ("Ingrese la frase para cifrar: ")
    texto_cifrado = ""

    for x in text:
        if x.isalpha():
            for y in abecedario:
                if x == y:
                    indice= abecedario[y]
                    indice_n= (indice + 4)
                    if indice_n > 26:
                        indice_n = (indice_n - 27)
                    letra_n =find(abecedario, indice_n)
                    letra_nn= str(letra_n)
                    texto_cifrado = texto_cifrado + letra_nn
        else:
            texto_cifrado = texto_cifrado + x
    time_out_f(0.75)
    pros_sl()
    time_out_f(0.75)
    mostrar_f(text, texto_cifrado)
    return(texto_cifrado)

def descifrar():
    print("")
    abecedario = dicc()
    text_ci = input ("Ingrese la frase cifrada : ")
    texto_descifrado = ""

    for x in text_ci:
        if x.isalpha():
            for y in abecedario:
                if x == y:
                    indice= abecedario[y]
                    indice_n= (indice - 4)
                    if indice_n < 0:
                        indice_n = (indice_n + 27)
                    if indice_n > 26:
                        indice_n = (indice_n - 27)
                    letra_n =find(abecedario, indice_n)
                    letra_nn= str(letra_n)
                    texto_descifrado = texto_descifrado + letra_nn
        else:
            texto_descifrado = texto_descifrado + x
    time_out_f(0.75)
    pros_sl()
    time_out_f(0.75)
    mostrar_f(text_ci, texto_descifrado)
    return(texto_descifrado)

def thanks():
    print("")
    print("GRACIAS POR UTILIZAR EL SISTEMA 7w7")
    print("")
