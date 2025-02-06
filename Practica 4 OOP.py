class Head:
    def __init__(self):
        pass

class Hand:
    def __init__(self, side):
        self.side = side
        print(f"Completa la mano {self.side}")
        
class Arm:
    def __init__(self, side, hand):
        self.side = side
        self.hand = hand
        print(f"Completo el brazo {self.side} junto a mano {self.hand.side}")

class Feet:
    def __init__(self, side):
        self.side = side
        print(f"Complet el pie {self.side}")

class Leg :
    def __init__(self, side, feet):
        self.side = side
        self.feet = feet
        print(f"Completla pierna {self.side} junto al pie {self.feet.side}")

cabeza = Head()

Mano_izq = Hand("izquierda") 
Mano_der = Hand("derecha") 

Brazo_izq = Arm("izquierdo", Mano_izq)
Brazo_der = Arm("derecho", Mano_der)

Pie_izq = Feet("Izquierdo")
Pie_der = Feet("Derecho")

Pierna_izq = Leg("Izquierda", Pie_izq)
Pierna_der = Leg("Derecha", Pie_der)


class Torso:
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg
        print("Todo esta unido")

torso = Torso(cabeza,Brazo_der,Brazo_izq,Pierna_der,Pierna_izq)


class Human:
    def __init__(self, torso):
        self.torso = torso
        print("Humano creado")

humano= Human(torso)