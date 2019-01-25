#Classe Auteur


class Auteur:
    def __init__(self, pid, pnom):
        self.id = pid
        self.nom = pnom

    def getauteurnom(self):
        return self.nom

    def getauteurid(self):
        return self.id

    def __str__(self):
        return ("Auteur: "+self.nom)
