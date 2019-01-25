#Classe Multimédia

from Document import Document

class Multimedia(Document):
    def __init__(self, pid, ptitre, pcopyright, pediteur, pauteur):
        self.id = pid
        self.titre = ptitre
        self.copyright = pcopyright
        self.editeur = pediteur
        self.auteur = pauteur

    def imprime(self):
        print("L'impression du document "+self.titre+" est lancée.")

    def __str__(self):
        return Document.__str__(self) + " | Multimédia"