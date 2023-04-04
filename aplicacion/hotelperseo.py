from sys import path
path.append('../PerseoBackend/funciones')



import modHab as h 
import modTipoHab as th


#h.selecHab()
def hotelperseo():
    while True:
        print('Hotel Perseo\n Menu\n 1-Consultar\n 2-Insertar\n 3-Eliminar\n 4-Actualizar')
        ctrl=str(input('Que opción deseas:'))
        print()
        match ctrl:
            case '0':
                break
            case '1':
                while True:
                    print('Consultar:\n 1-Habitaciones\n 2-Tipos de Habitaciones ')
                    ctrl=str(input('Que quieres consultar: '))
                    print()
                    match ctrl:
                        case '0':
                            break
                        case '1':
                            h.selecHab()
                            print()
                        case '2':
                            th.selecTH()
                            print()
    
hotelperseo()