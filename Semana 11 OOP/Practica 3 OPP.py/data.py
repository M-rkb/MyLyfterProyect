import csv
from models import Student, Grade


def  create_csv(nombre_archivo, datos):
    if not datos:
        print("No hay datos para exportar.")
        return
    datos= object_to_dic(datos)
    encabezados = datos[0].keys()
    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
            escritor.writeheader()
            escritor.writerows(datos)
        print(f"Datos exportados exitosamente al archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error al exportar los datos: {e}")
    

def object_to_dic(datos):
    estudiantes = []
    for dato in datos:
        dic = {}
        dic["name"] = dato.name
        dic["group"] = dato.group
        for grade in dato.grades:
            dic[grade.name] = grade.score
        estudiantes.append(dic)
    return estudiantes
       

def charge_csv(lista_destino):
    file_path = 'Datos_estudiantiles.csv'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            data = dic_to_object(data)
            lista_destino.extend(data) 
            print("Datos importados exitosamente.")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{file_path}'. Asegúrese de haber exportado los datos previamente.")
    except Exception as e:
        print(f"Error al importar los datos: {e}")


def dic_to_object(datos):
    estudiantes = []
    for dato in datos:
        estudiante = Student(dato["name"],dato["group"] )

        for grade in dato.keys():
            if grade not in ["name","group"]:
                estudiante.add_grade (Grade (grade, int(dato[grade] ))) 
        estudiantes.append(estudiante)
    return estudiantes