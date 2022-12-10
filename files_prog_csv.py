def main():
    import csv
    print("Contactos")
    
    # Obtiene la Lista de mascotas
    mascotas = list()
    archivo= open( "mascotas.csv", "r" )
    archivo_csv = csv.reader(archivo)
    for row in archivo_csv:
        mascotas.append(row)
    archivo.close()
    

    
    choice = 0
    while choice != 4:
        print("\n Seleccione la opción correspondiente \n")
        print("1. Agregar Mascota")
        print("2. Buscar Mascota")
        print("3. Mostrar todas las mascotas")
        print("4. Quitar y guardar")
        choice = int(input())

        if choice == 1:
            print("Agregar una mascota")
            nombre = input("Agrega nombre de la mascota: ")
            owner = input("Agrega nombre del dueño: ")
            telefono = input("Agrega el teléfono del dueño: ")
            mascotas.append([nombre, owner, telefono])

        elif choice == 2:
            print("Busca una mascota")
            keyword = input("Escribe el término buscado: ")
            for mascota in mascotas:
                if keyword in mascota:
                    print(mascota)
        elif choice == 3:
            print("Mostrando todas las mascotas \n")
            for i in range(len(mascotas)):
                print(mascotas[i])
        elif choice == 4:
            print("Saliendo del programa")
        else:
            print("Respuesta inválida")

    ### Modifica desde aquí para que al cerrar usando la opción 4 en vez de guardar un archivo Binario lo guarde en un archivo de texto separado por comas,
    # Recuerda que a diferencia del archivo binario pickle, cuando se graba un archivo en un documento de texto, este se irá añadiendo línea por línea al archivo generado
    # Por lo que deberás usar un iterador y un marcador de fin de línea "/n" para delimitar cada mascota.
    
 
    archivo_w = open("mascotas.csv", "w")
    
    with archivo_w:
       for row in mascotas:
          archivo_csv_w = csv.writer(archivo_w)
          archivo_csv_w.writerow(row)
          
    archivo_w.close()
        
main()
