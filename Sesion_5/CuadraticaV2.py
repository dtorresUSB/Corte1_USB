from math import sqrt as raizc

a = eval(input('Ingrese el valor de a = '))
b = int(input('Ingrese el valor de b = '))
c = int(input('Ingrese el valor de c = '))

if ((b**2)-4*a*c)<0:
    print('La solucion es imaginaria')
else:
    x1 = (-b + raizc((b**2)-4*a*c))/(2*a)
    x2 = (-b - raizc((b**2)-4*a*c))/(2*a)
    print('el primer resultado es ', x1)
    print('el segundo resultado es ', x2)



