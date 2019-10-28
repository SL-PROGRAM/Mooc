"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

HISTORIQUE_TEMPETES

Écrivons une fonction historique_tempetes qui reçoit en paramètre formel la liste vent_max de ces valeurs et imprime
 pour chaque année si les îles ont subi une tempête ou un cyclone et si c’est le cas, de quelle catégorie.

"""

def categorie(vent):
   """renvoie la catégorie de cyclone enregistré en fonction du vent"""

   assert vent > 118 # sinon provoque une erreur dans le code

   if vent < 154:
       res = 1
   elif vent < 178:
       res = 2
   elif vent < 210:
       res = 3
   elif vent < 251:
       res = 4
   else: # catégorie 5
       res = 5
   return res

def historique_tempetes(vent_max):
   """affiche pour chaque année la catégorie de vents subis cette année-là
   entrée : vent_max: liste des vents maximums enregistrés en km/h
   chaque année (composante 0 étant pour l'an 2000)"""

   annee = 2000
   for vent in vent_max:
       if vent < 64:
           print("En", annee, ": pas de tempête enregistrée")
       elif vent < 119:
           print("En", annee, ": il y a eu au moins une tempête mais pas de cyclone")
       else:
           print("En", annee, ": le plus gros cyclone enregistré était de catégorie",
           categorie(vent))
       annee += 1


mes_valeurs = [75, 200, 230, 260, 100, 80, 50, 45, 180, 100, 200, 63, 64, 65,\
        118, 119, 153, 154, 280, 345]
historique_tempetes(mes_valeurs)