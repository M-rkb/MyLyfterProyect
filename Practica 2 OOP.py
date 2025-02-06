class Person():
    def __init__(self, name):
        self.name = name 
    
class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passengers (self, person):
        if len(self.passengers)< self.max_passengers:
            self.passengers.append(person)
            print(f"Pasajero {person.name} agregado.")
        else:
            print("El bus está lleno. No se puede agregar más pasajeros.") 

    def remove_passenger(self, person):  
        if person in self.passengers:  
            self.passengers.remove(person)  
            print(f"Pasajero {person.name} bajado del bus.")  



passenger_1 = Person("Juan")
passenger_2 = Person("Nidya")
passenger_3 = Person("Luis")
passenger_4 = Person("Pedro")
passenger_5 = Person("Omar")
passenger_6 = Person("Jose")


my_bus = Bus(3)

my_bus.add_passengers(passenger_1)
my_bus.add_passengers(passenger_2)
my_bus.add_passengers(passenger_3)
my_bus.add_passengers(passenger_4)  
my_bus.add_passengers(passenger_5) 

my_bus.remove_passenger (passenger_3)
my_bus.remove_passenger (passenger_2)
my_bus.remove_passenger (passenger_1)
my_bus.remove_passenger (passenger_4)