//PROBLEMAS SOCIALES
import time
import os
def menu():
    print("PROBLEMAS SOCIALES.")
    print()
    print("AREQUIPA - BULLING")
    print("PUNO - POBREZA")
    print("CUZCO - CONTAMINACION")
    print()
    n=str(input("Ingrese su nombre: "))
    d=str(input("Ingrese su Departamento: "))
    print()
    d=d.lower()

    if d=='arequipa':
        print("SR. ",n," EL PROBLEMA SOCIAL QUE ACTUALMENTE ENFRENTA AREQUIPA ES EL BULLING")
        time.sleep(2)
    elif d=='puno':
        print("SR. ",n," EL PROBLEMA SOCIAL QUE ACTUALMENTE ENFRENTA PUNO ES LA POBREZA")
        time.sleep(2)
    elif d=='cuzco':
        print("SR. ",n," EL PROBLEMA SOCIAL QUE ACTUALMENTE ENFRENTA CUZCO ES LA CONTAMINACION")
        time.sleep(2)
    else:
        print("SR. ",n," DEPARTAMENTO NO ENCONTRADO EN NUESTRA BASE DE DATOS")
        print("VUELVA A INTENTAR")
        time.sleep(2)
        os.system("clear")
        menu()
                
menu()
