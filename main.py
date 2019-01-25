from Médiathèque import Mediatheque
from Auteur import Auteur
from Editeur import Editeur
from Article import Article
from Livre import Livre
from Vidéo import Vidéo
from Audio import Audio
from Multimédia import Multimedia

lam = Mediatheque(1, "Le Bouscat")
Massi = Auteur(1, "Ouldrabah")
MassiEdition = Editeur(1, "MassiEdition")
vid1 = Vidéo(2, "La Bourboule", True, Massi, MassiEdition)
aud1 = Audio(3, "La Bourboule", True, Massi, MassiEdition)
mult1 = Multimedia(4, "La Bourboule", True, Massi, MassiEdition)
livre1 = Livre(5, "La Bourboule", True, Massi, MassiEdition, "03/03/2013", 3366)
art1 = Article(6, "Se futon de la gueule du monde? ", True, Massi, MassiEdition, "Gorafi", 3366)

print(lam)
print(Massi)
print(MassiEdition)
print(vid1)
print(aud1)
print(mult1)
print(livre1)
print(art1)