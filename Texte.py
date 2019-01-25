#Classe Texte

from Document import Document

class Texte(Document):

    def __init__(self, pid, ptitre, pcopyright, pauteur, pediteur):
        self.id = pid
        self.titre = ptitre
        self.copyright = pcopyright
        self.editeur = pediteur
        self.auteur = pauteur

    def __str__(self):
        return Document.__str__(self)