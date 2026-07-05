class Student:
    def __init__(self, nom, notes):
        self.nom = nom
        self.notes = notes

    def average(self):
        return sum(self.notes) / len(self.notes)


# Création de l'objet
s1 = Student("Alice", [85, 90, 78, 92, 88])

# Affichage du résultat
print(f"Moyenne de {s1.nom} : {s1.average():.1f}")