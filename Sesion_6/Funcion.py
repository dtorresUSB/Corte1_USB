
def suma(a,b):
    resultado = a + b
    return resultado

def imprimir(nm):
    print(nm,',Su resultado es:')

n = 'si'
nombre = input('Ingrese su nombre: ')
while n == 'si':
  
    a =int(input('ingrese un numero: '))
    b =int(input('ingrese un numero: '))
    res = suma(a,b)
    imprimir(nombre)
    print(res)
    n = input('¿Quiere sumar otro numero? (si/no)')