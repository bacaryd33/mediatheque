#Classe Document


class Document:
    def __init__(self, pid, ptitre, pcopyright, pediteur, pauteur):
        self.id = pid
        self.titre = ptitre
        self.copyright = pcopyright
        self.editeur = pediteur
        self.auteur = pauteur

    def gettitredocument(self):
        return self.titre

    def getdocumentid(self):
        return self.id

    def affiche(self):
        self.__str__()

    def __str__(self):
        msg = str(self.id)
        msg += " | "+self.titre
        msg += " |"+str(self.copyright)
        msg += " | "+str(self.auteur)
        msg += " | "+str(self.editeur)
        return msg

