#Alejandro Suescun
print('')
print("**INGRESO VEHÍCULOS**")
print("----------------------")
print("1. Ingresar vehículo")
print("2. Eliminar")
print("3. Editar")
print("4. Imprimir")
print("5. Salir")
print("----------------------")

opcion = 0
carros = [] 
while opcion != 5:
    opcion = int(input("Digite una opción: "))
    
    if opcion == 1:
        carro = {}  
        carro["placa"] = input("Ingrese la placa: ")
        carro["marca"] = input("Ingrese la marca: ")
        carros.append(carro)  
        print("Vehículo ingresado correctamente.")
        print(carros)
        
        
    
    elif opcion == 2:
        placa = input("Ingrese la placa del vehículo a eliminar: ")
        for carro in carros:
            if carro["placa"] == placa:
                carros.remove(carro)
                print("Vehículo eliminado correctamente.")
                print(carros)
                
                
    
    elif opcion == 3:
        placa = input("Ingrese la placa del vehículo a editar: ")
        for carro in carros:
            if carro["placa"] == placa:
                carro["placa"] = input("Ingrese nueva placa: ")
                carro["marca"] = input("Ingrese nueva marca: ")
                print("Vehículo editado correctamente.")
                print(carros)
                
    
    elif opcion == 4:
            print("Listado de vehículos:")
            print(carros)
            
    
    elif opcion == 5:
        print("Usted ha salido")
        break


    
    