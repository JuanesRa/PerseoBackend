from sys import path
path.append('../PerseoBackend/funciones')



import modHab as h 
import modTipoHab as th


#h.selecHab()
def hotelperseo():
    while True:
        print('Ingresar como:\n 1-Huespéd\n 2-Administrador')
        ctrl=str(input('Ingresar como: '))
        print()
        match ctrl:
            case '0':
                break
            case '1':#aqui pone lo suyo juan :)
                pass
               
            case '2':
                while True:
                    print('Hotel Perseo\n Menu Admin\n 1-Consultar\n 2-Insertar\n 3-Eliminar\n 4-Actualizar\n 5-Reportes')
                    ctrl=str(input('Que opción deseas:'))
                    print()
                    match ctrl:
                        case '0':
                            break
                        case '1':
                            while True: 
                                print('Consultar:\n 1-Habitación\n 2-Tipo de Habitación ')
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
                                    case _ :
                                        print('Esta opción no existe')
                    
                        case '2':
                            while True:
                                print('Insertar:\n 1-Habitación\n 2-Tipo de Habitación ')
                                ctrl=str(input('Que quieres insertar: '))
                                print()
                                match ctrl:
                                    case '0':
                                        break
                                    case '1':
                                        h.inserthab() 
                                        print()
                                    case '2':
                                        th.insertTH() 
                                        print()
                                    case _ :
                                        print('Esta opción no existe')
                        case '3':
                            while True:
                                print('Eliminar:\n 1-Habitación\n 2-Tipo de Habitación ')
                                ctrl=str(input('Que quieres eliminar: '))
                                print()
                                match ctrl:
                                    case '0':
                                        break
                                    case '1':
                                        h.deletehab() 
                                        print()
                                    case '2':
                                        th.deleteTH() 
                                        print()
                                    case _ :
                                        print('Esta opción no existe')
                        case '4':
                            while True:
                                print('Actualizar:\n 1-Habitación\n 2-Tipo de Habitación ')
                                ctrl=str(input('Que quieres actualizar: '))
                                print()
                                match ctrl:
                                    case '0':
                                        break
                                    case '1':
                                        h.updatehab() 
                                        print()
                                    case '2':
                                        th.updateTH()
                                        print()
                                    case _ :
                                        print('Esta opción no existe')
                        case '5':
                             while True:
                                print('Reporte:\n 1-Habitación\n 2-Tipo de Habitación ')
                                ctrl=str(input('Que quieres actualizar: '))
                                print()
                                match ctrl:
                                    case '0':
                                        break
                                    case '1':
                                        h.reporteHabit() 
                                        print()
                                    case '2':
                                        th.reporteTipoHab()
                                        print()
                                    case _ :
                                        print('Esta opción no existe')
                            
                        
                        case _ :
                                        print('Esta opción no existe')
                
                
               
            case _ :
                print('Esta opción no existe')
        
        
                        
                    
hotelperseo()