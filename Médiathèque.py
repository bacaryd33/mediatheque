# Class Mediatheque

class Mediatheque(object):
    def __init__(self, pid, plabel):
        self.id = pid
        self.label = plabel
        self.banquelivre = {}

    def getmediathequetid(self):
        return self.id

    def getmediathequelabel(self):
        return self.label

    def ajoutelivre(self, pdoc):
        self.banquelivre[pdoc.id]
        self.banquelivre[pdoc]

    def supprimelivre(self,pid):
        if self.banquelivre.has_key(pid):
            del self.banquelivre[pid]

    #def each_livre(self):

    #def each_article(self):

    def __str__(self):
        return ("Mediatheque: "+self.label)
