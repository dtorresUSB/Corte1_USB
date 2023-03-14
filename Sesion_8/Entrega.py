import ejercicio1
import ejercicio2
import ejercicio3

def main():
    opc = input('ingrese una opcion: ')
    if opc=='1':
        ejercicio1.digitos()
    elif opc =='2':
        ejercicio2.fibonacci()
    elif opc =='3':
        ejercicio3.primos()

if __name__== "__main__":
    main()