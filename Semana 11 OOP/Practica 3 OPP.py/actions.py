import heapq
from data import create_csv, charge_csv
from models import Student, Grade

all_student_data = []

def info_students():

    Nombre = str(input("Ingrese el nombre del estudiante: "))
    Grupo = str(input("Ingrese la seccion del estudiante : "))

    estudiante = Student(Nombre, Grupo)


    def ask_grades(subject):
        while True:
            try: 
                subject = int(input(f"Ingresela nota de {subject}:(0 a 100): "))
                if 0 <= subject <= 100:
                    return subject
                else:
                    print ("La nota debe estar entre 0 y 100.")
            except ValueError:
                print("Ingrese un numero entero")

    estudiante.add_grade (Grade ("espanol", ask_grades("espanol") )) 
    estudiante.add_grade (Grade ("estudios sociales ", ask_grades("estudios sociales") )) 
    estudiante.add_grade (Grade ("ingles", ask_grades("ingles ") )) 
    estudiante.add_grade (Grade ("ciencias", ask_grades("ciencias") )) 
 
    print("Estudiante ingresado correctamente!") 

    return estudiante
    

def show_students():
    if all_student_data:
        print("Información de los estudiantes:")
        print()
        for student in all_student_data:
            print(f"Nombre: {student.name}")
            print(f"Sección: {student.group}")
            print(f"Promedio: {student.get_average_score()}")
            for grade in student.grades:
                print(f"Nota {grade.name}: {grade.score}") 
    else:
        print("No hay estudiantes registrados.")


def three_best_avg():
    if all_student_data:
        
        topthree = heapq.nlargest(3, all_student_data, key=lambda student: student.get_average_score())
        print("Los 3 mejores promedios:")

        for i, student in enumerate(topthree, 1):
            print(f"{i}. {student.name } - Promedio: {student.get_average_score()}")
    else:
        print("No hay estudiantes registrados.")


def show_avg():
    if all_student_data:  
        prom_general = 0  
        for student in all_student_data:
            prom_general += float(student.get_average.score()) 

        all_average = prom_general / len(all_student_data)
        print(f"El promedio total del grupo es {all_average:}") 
    else:
        print("No hay estudiantes registrados.")

def export_csv():
    if all_student_data:
            create_csv('Datos_estudiantiles.csv', all_student_data)

def import_csv():
    charge_csv(all_student_data)
