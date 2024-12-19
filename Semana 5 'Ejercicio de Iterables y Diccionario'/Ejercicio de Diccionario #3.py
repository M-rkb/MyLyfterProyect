Genshin={
    "Name":"Arlecchino", 
    "Weapon":"Polearm",
    "Rol":"DPS",
    "Element":"Pyro",
    }
delete_list=['Rol', 'Element']
for keys in delete_list:
    Genshin.pop(keys)
print(Genshin)