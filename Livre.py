#Classe Livre

from Texte import Texte

class Livre(Texte):
    def __init__(self, pid, ptitre, pcopyright, pauteur, pediteur, panneeparution, pnumedition):
        self.id = pid
        self.titre = ptitre
        self.copyright = pcopyright
        self.editeur = pediteur
        self.auteur = pauteur
        self.anneeparution = panneeparution
        self.numeroedition = pnumedition

    def __str__(self):
        return Texte.__str__(self) + " | Livre | Année parution : " +self.anneeparution+" | Numéro édition : "+ str(self.numeroedition)