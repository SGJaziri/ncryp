#-*-coding:utf8;-*-
#qpy:console

#Elector de etapas
i = 0
abecedario= {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'ñ':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
def find(abecedario, v):
        for k in abecedario:
            if abecedario[k] == v:
                return k


print("Hola, este scrip esta hecho para poder encriptar un texto :D")
print("Y para ganarle a pasiche e Ismael 7w7")
print("")
    
while (i == 0):
#ELECCION 
    print("Ahora tendra la opcion de elegir cifrar una frase completa")
    print("O decodificar una frace cifrada")
    print("")
    print("[0] --> PARA CIFRAR UNA FRASE NUEVA")
    print("[1] --> PARA DECODIFICAR UNA FRASE CIFRADA") 
    print("")
    eleccion = input("Cual es la acción que decea realizar : ")
    eleccion_n = int(eleccion)
#CIFRAR LETRAS 
    if eleccion_n == 0:
        print("")
        text = input ("Ingrese la palabra para cifrar: ")
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

        print()   
        print(texto_cifrado)
        i=1
    else:
        print("xd")


