import heapq
from data import create_csv, charge_csv

all_student_data = []


def info_students():
    list_student = {}
    
    list_student['Name'] = str(input("Ingrese el nombre del estudiante: "))
    list_student['Group'] = str(input("Ingrese la seccion del estudiante : "))
    
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

    list_student['score_spanish'] = ask_grades("espanol")
    list_student['score_english'] = ask_grades("ingles")
    list_student['score_history'] = ask_grades("sociales")
    list_student['score_science'] = ask_grades("ciencias")

    list_student['average'] = (list_student['score_spanish'] + 
                               list_student['score_english'] + 
                               list_student['score_history'] + 
                               list_student['score_science']) / 4
    
    
    print("Estudiante ingresado correctamente!") 

    return list_student
    
def show_students():
    if all_student_data:
        print("Información de los estudiantes:")
        print()
        for student in all_student_data:
            print(f"Nombre: {student['Name']}")
            print(f"Sección: {student['Group']}")
            print(f"Nota Español: {student['score_spanish']}")
            print(f"Nota Inglés: {student['score_english']}")
            print(f"Nota Sociales: {student['score_history']}")
            print(f"Nota Ciencias: {student['score_science']}")
            print(f"Promedio: {student['average']}")
            print()
    else:
        print("No hay estudiantes registrados.")


def three_best_avg():
    if all_student_data:

        topthree = sorted([ d['average'] for d in all_student_data],reverse=True)[:3]
        print(topthree)
        topthree = heapq.nlargest(3, all_student_data, key=lambda student: student['average'])
        print("Los 3 mejores promedios:")
        for i, student in enumerate(topthree, 1):
            print(f"{i}. {student['Name']} - Promedio: {student['average']}")
    else:
        print("No hay estudiantes registrados.")


def show_avg():
    if all_student_data:  
        prom_general = 0  
        for student in all_student_data:
            prom_general += float(student["average"]) 

        all_average = prom_general / len(all_student_data)
        print(f"El promedio total del grupo es {all_average:}") 
    else:
        print("No hay estudiantes registrados.")

def export_csv():
    if all_student_data:
            create_csv('Datos_estudiantiles.csv', all_student_data)

def import_csv():
    charge_csv(all_student_data)
