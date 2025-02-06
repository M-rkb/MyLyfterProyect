import actions as act

def student_menu():
    while True:
        print(" Menú ")
        print("1. Agregar estudiantes")
        print("2. Ver informacion de los estudiantes")
        print("3. 3 mejores promedios")
        print("4. Ver nota promedio de todos los estudiantes.")
        print("5. Exportar datos a archivo CSV")
        print("6. Cargar datos desde archivo CSV")
        print("7. Salir")

        try:
            option = int(input("Seleccione una opción (1-7): "))
            
            if option == 1:
            
                student = act.info_students() 
                act.all_student_data.append(student)

            elif option == 2:
              
                act.show_students()

            elif option == 3:
             
                act.three_best_avg()

            elif option == 4:
               
                act.show_avg()

            elif option == 5:
             
                act.export_csv()
        
            elif option == 6:
            
                act.import_csv()

            elif option == 7:
                print("Saliendo del programa.")
                break

            else:
                print("Opción no válida. Por favor seleccione una opción entre 1 y 7.")

        except ValueError:
            print("Entrada inválida, por favor ingrese un número entero.")
