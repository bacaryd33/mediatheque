#Classe Éditeur


class Editeur:
    def __init__(self, pid, pnom):
        self.id = pid
        self.nom = pnom

    def getediteurid(self):
        return self.id

    def getediteurnom(self):
        return self.nom

    def __str__(self):
        return "Editeur: "+self.nom
