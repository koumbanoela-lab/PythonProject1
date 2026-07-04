class Rectangle:

    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def area(self):
        return self.longueur * self.largeur

    def perimeter(self):
        return 2 * (self.longueur + self.largeur)


rect = Rectangle(10, 4)

print("Aire :", rect.area())
print("Périmètre :", rect.perimeter())