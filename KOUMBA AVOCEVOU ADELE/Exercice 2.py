class Vehicle:

    def __init__(self, nom, max_speed, mileage):
        self.nom = nom
        self.max_speed = max_speed
        self.mileage = mileage


vehicule1 = Vehicle("Tesla Model S", 250, 18)

print("Nom du véhicule :", vehicule1.nom)
print("Vitesse maximale :", vehicule1.max_speed)
print("Kilométrage :", vehicule1.mileage)