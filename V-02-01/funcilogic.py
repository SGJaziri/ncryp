from os import system
from time import sleep
from sys import platform

from funcimen import pros_sl, mostrar_f, men_export1

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

def time_out_f(slep):
    sleep(slep)
    if platform == "win32":
        system("cls")
    else:
        if platform() == "linux":
            system("clear")

def find(abecedario, v):
        for k in abecedario:
            if abecedario[k] == v:
                return k

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
    elec = men_export1()
    if elec == 0:
        text_ci = impor_txt()
    else:
        print("")
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

def expor_txt(txt):
    t = open('clave.txt', 'w')
    t.write(txt)
    t.close()

def impor_txt():
    t = open('clave.txt', 'r')
    text_cif = t.read()
    t.close()
    return(text_cif)