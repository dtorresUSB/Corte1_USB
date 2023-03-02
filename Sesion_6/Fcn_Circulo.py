
def Area(r):
    pi = 3.1416
    A = pi*(r**2)
    return A

def Volumen(h,A):
    V = A*h
    return V

r = int(input('Ingrese el valor del radio: '))
h = int(input('Ingrese el valor del altura: '))

A = Area(r)
V = Volumen(h,A)

print(f'el area es {A} y el volumen es {V}')


