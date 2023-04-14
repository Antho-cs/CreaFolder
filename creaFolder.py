import os

# Les chemins des dossiers racine
chemin = ["X:/Anime/", "X:/Série/"]

# Saisie utilisateur
choix = int(input("Est-ce une Animé (0) ou un Série (1) :"))
nom_serie = input("Saisie le nom du dossier :")
nb_saison = int(input("Saisie le nombre de saison :"))

# Traitement
os.mkdir(chemin[choix] + nom_serie)
for x in range(nb_saison):
    os.mkdir(chemin[choix] + nom_serie + r"/Saison " + str(x + 1) )
