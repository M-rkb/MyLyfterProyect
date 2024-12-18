import json

filename = "pokemon22.json"

with open (filename, 'r')as file:
    data=json.load(file)

Name = input('Ingrese el nombre del pokemon : ')
Type = input('Ingrese el tipo del pokemon: ').split(",")
Hp = int(input('Ingese  Hp :'))
Atk = int(input('Ingese Ataque :'))
Def = int(input('Ingese Defensa :'))
Sp_Atk = int(input('Ingese Ataque Especial :'))
Sp_Def = int(input('Ingese Defensa Especial  :'))
Spd = int(input('Ingese el Velocidad :'))

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

data.append(Pokemon)

with open(filename, 'w') as file:
    json.dump(data, file, indent=4)

print("Actualizado")