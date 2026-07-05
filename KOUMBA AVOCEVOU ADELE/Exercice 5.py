class Product:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def total_value(self):
        return self.prix * self.quantite


# Création de l'objet
p1 = Product("Laptop", 899.99, 5)

# Affichage du résultat
print(f"Valeur totale du stock de {p1.nom} : {p1.total_value():.2f} $")