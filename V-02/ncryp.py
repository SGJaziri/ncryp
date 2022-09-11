from funci import dicc, menu_p, cifrar, descifrar, thanks

list_leters = dicc()

elec = menu_p()
if elec == 0:
    cifrar()
    thanks()
else: 
    if elec == 1:
        descifrar()
        thanks()
    else:
        thanks()