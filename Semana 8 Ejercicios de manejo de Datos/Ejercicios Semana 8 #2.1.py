import csv


game_list = []

while True:
     
    game = {
        'nombre': '',
        'genero': '',
        'desarrollador': '',
        'clasificacion': '',
    }
    game['nombre'] = input('Escriba el nombre del videojuego por agregar: ')
    game['genero'] = input('Escriba el genero del videojuego mencionado: ')
    game['desarrollador'] = input('Escriba el desarrollador del videojuego mencionado: ')
    game['clasificacion'] = input('Escriba la clasificacion del videojuego mencionado: ')

    game_list.append(game)	
    continuar = input('¿Agregar otro juego? (yes/no): ').lower()
    if continuar != 'yes':
	    break

headers = ['nombre', 'genero', 'desarrollador', 'clasificacion']



def write_csv_file(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, headers, delimiter='\t')
    writer.writeheader()
    writer.writerows(data)

	   
     
write_csv_file('gamest.csv',game_list, headers)

