import json

filename = "Pokemon.json"

with open (filename, 'r')as file:
    data=json.load(file)
print(data)

Pokemon = []

while True:

    Name = input('Ingrese el nombre del pokemon : ')
    Type = input('Ingrese el tipo del pokemon: ')
    Hp = input('Ingese  Hp :')
    Atk = input('Ingese Ataque :')
    Def = input('Ingese Defensa :')
    Sp_Atk = input('Ingese Ataque Especial :')
    Sp_Def = input('Ingese Defensa Especial  :')
    Spd = input('Ingese el Velocidad :')
    continuar = input('¿Agregar otro pokemon? (yes/no): ').lower()
    if continuar != 'yes':
	    break



Pokemon = {
    "name": {
      "english": Name
    },
    "type":Type,
    "base": {
      "HP": Hp,
      "Attack": Atk,
      "Defense": Def,
      "Sp. Attack": Sp_Atk,
      "Sp. Defense": Sp_Def,
      "Speed": Spd
    }
}


print(Pokemon)