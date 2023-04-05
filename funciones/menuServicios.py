import crudservicio
import crudtiposervicio

while True:
    print("Como administrador puedo: ")
    print("1-Insertar un nuevo servicio")
    print("2-Eliminar un servicio")
    print("3-Modificar un servicio")
    print("4-Consultar servicios como prefiera")
    print("5-Consultar la tabla de servicios")
    print("6-Insertar un nuevo tipo de servicio")
    print("7-Eliminar un tipo de servicio")
    print("8-Modificar un servicio")
    print("9-Consultar tipos de servicios como prefiera")
    print("10-Consultar la tabla de tipos de servicios")
    opcion=int(input("ingrese la opcion que desee: "))

    match opcion:
        case 1:
            print(crudservicio.insertar())
        case 2:
            print(crudservicio.eliminar())
        case 3:
            print(crudservicio.modificar())
        case 4:
            print(crudservicio.consultar())
        case 5:
            print(crudservicio.consultartodo())
        case 6:
            print(crudtiposervicio.insertartipo())
        case 7:
            print(crudtiposervicio.eliminartipo())
        case 8:
            print(crudtiposervicio.modificartipo())
        case 9:
            print(crudtiposervicio.consultartipo())   
        case 10:
            print(crudtiposervicio.consultartodotipo())  
        case _:
            print("opcion no valida")   
            break           
