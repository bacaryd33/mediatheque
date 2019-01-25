#Classe Article

from Texte import Texte

class Article(Texte):
    def __init__(self, pid, ptitre, pcopyright, pauteur, pediteur, ptitrerevue, pnumedition):
        self.id = pid
        self.titre = ptitre
        self.copyright = pcopyright
        self.editeur = pediteur
        self.auteur = pauteur
        self.titrerevue = ptitrerevue
        self.numeroedition = pnumedition

    def __str__(self):
        return Texte.__str__(self) + " | Livre | Titre revue : " +self.titrerevue+" | Numéro édition : "+ str(self.numeroedition)