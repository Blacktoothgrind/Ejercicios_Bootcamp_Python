def menu():
    print("\t MENU")
    print("\t Opcion A - Agregar un contacto")
    print("\t Opcion B - Buscar un contacto")
    print("\t Opcion C - Eliminar un contacto")
    print("\t Ingrese cualquier otra letra para salir: ")
    return input('\t')

def agregar(agenda):
    '''Esta funcion agrega un contacto a la agenda'''
    dni = input('Introduce el DNI : ')
    nombre = input('Introduce el nombre del cliente: ')
    direccion = input('Introduce la dirección del cliente: ')
    telefono = input('Introduce el teléfono del cliente: ')
    persona = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono }
    agenda[dni] = persona
    return(agenda)

'''Esto es para probar la función agregar'''
#agregar()

def buscar(agenda):
    dni = input('Introduce DNI del cliente: ')
    if dni in agenda:
        print('DNI :', dni)
        for clave, valor in agenda[dni].items():
                print('\t' + clave.title() + ':', valor)
                
    else:
        print('No existe la persona con el DNI ', dni)

def eliminar(agenda):
    dni = input('Introduce DNI de la persona a borrar de la Agenda: ')
    if dni in agenda:
            del agenda[dni]
            return(agenda)
    else:
        print('\t' + 'No existe la persona con del DNI ', dni)


# PROGRAMA
agenda = {}

while True:
    op = menu()
    if op.lower() == "a":
        agenda = agregar(agenda)
    elif op.lower() == "b":
        buscar(agenda)
    elif op.lower() == "c":
        agenda = eliminar(agenda)
    else:
        break

print("LA AGENDA TIENE ESTOS VALORES: ", agenda)
