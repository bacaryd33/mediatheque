#classe Vidéo

from Document import Document

class Vidéo(Document):
    def __init__(self, pid, ptitre, pcopyright, pediteur, pauteur):
        self.id = pid
        self.titre = ptitre
        self.copyright = pcopyright
        self.editeur = pediteur
        self.auteur = pauteur


    def __str__(self):
        return Document.__str__(self)+" | Vidéo "