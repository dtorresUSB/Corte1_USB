
print('Escoja una de las siguientes opciones:\n')
print('1. for in range(final)')
print('2. for in range(inicio, final)')
print('3. for in range(inicio, final, paso)')

opc = input('Escoja una opcion: ')

if opc == '1':
    for i in range(10):
        print(i+1)
    print('fin del proceso 1')

elif opc=='2':
    for i in range(1,11):
        print(i)
    print('fin del proceso 2')
elif opc=='3':
    for i in range(10,21,2):
        print(i)
    print('fin del proceso 3')

