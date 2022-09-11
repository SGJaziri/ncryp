from funcilogic import dicc, cifrar, descifrar, time_out_f, expor_txt
from funcimen import thanks, menu_s, men_recov, title_prim, men_export, men_o

def menu_p():
    time_out_f(0)
    title_prim()
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

list_leters = dicc()
i = 0

while i == 0:
    elec = menu_p()
    if elec == 0:
        text_ci = cifrar()
        export = men_export()
        if export == 0:
            expor_txt(text_ci)
            men_o()
        elec_1 = men_recov()
        if elec_1 == 0:
            i = 0
        else:
            i=1
            thanks()
            time_out_f(1)
    else: 
        if elec == 1:
            text_des = descifrar()
            elec_1 = men_recov()
            if elec_1 == 0:
                i = 0
            else:
                i=1
                thanks()
                time_out_f(1)
        else:
            i = 1
            thanks()
            time_out_f(1)