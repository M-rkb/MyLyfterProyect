import csv

def  create_csv(nombre_archivo, datos):
    if not datos:
        print("No hay datos para exportar.")
        return
    encabezados = datos[0].keys()
    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
            escritor.writeheader()
            escritor.writerows(datos)
        print(f"Datos exportados exitosamente al archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error al exportar los datos: {e}")


def charge_csv(lista_destino):
    file_path = 'Datos_estudiantiles.csv'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            lista_destino.extend(data) 
            print("Datos importados exitosamente.")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{file_path}'. Asegúrese de haber exportado los datos previamente.")
    except Exception as e:
        print(f"Error al importar los datos: {e}")

