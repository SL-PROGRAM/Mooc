"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Énoncé

TRIPLE DOUBLES LETTRES CONSÉCUTIVES

Problème

Après avoir téléchargé le fichier words.txt, en cliquant words.txt ici, donnez la liste des mots anglais provenant du
fichier words.txt, avec trois doubles lettres consécutives. Je vous donne un couple de mots qui sont presque candidats,
mais pas tout à fait. Par exemple, le mot “committee” serait parfait s’il n’y avait pas ce “i” au milieu. Ou
“Mississippi” : si on retirait les “i”, cela marcherait. Il y a cependant au moins un mot qui possède trois paires
consécutives de lettres. C’est peut-être le seul mot, ou il peut y en avoir 500. Existe-il un mot avec les mêmes
caractéristiques dans le fichier mots.txt ?


QUADRUPLE DOUBLES LETTRES NON CONSÉCUTIVES

Problème

Donnez la liste des mot français, provenant du fichier mots.txt, avec quatre doubles lettres qui ne doivent pas être
consécutives. Je vous donne un mot qui est presque candidat, mais pas tout à fait. Par exemple, le mot “commissionnaire”
serait parfait s’il se terminait par « airre » ; il y donc trois doubles lettres mais pas quatre. Existe-il un mot avec
les mêmes caractéristiques dans le fichier words.txt ?

"""


def triple_double_lettres(mot):
   """renvoie vrai si le mot contient trois double lettres consécutives"""

   i = 0
   n = len(mot)
   res = False
   while not res and i < n - 5:
       res = mot[i] == mot[i + 1] and mot[i + 2] == mot[i + 3] \
             and mot[i + 4] == mot[i + 5]
       i += 1
   return res


def n_double_non_consecutifs(mot, n):
   """renvoie vrai si le mot contient n double lettres
      éventuellement non consécutives"""

   i = 0
   long = len(mot)
   cont = 0
   while cont < n and i < long - 1:
       if mot[i] == mot[i + 1]:
           cont += 1
           i += 2
       else:
           i += 1
   return cont == n


def quadruple_double_non_consecutifs(mot):
   """renvoie vrai si le mot contient quatre double lettres
      éventuellement non consécutives"""

   return n_double_non_consecutifs(mot, 4)


# code principal
print("triple-doubles consécutifs avec words.txt")
for m in open('words.txt', encoding="UTF-8"):
   mon_mot = m.strip()
   if triple_double_lettres(mon_mot):
       print(mon_mot)

print("triple-doubles consécutifs avec mots.txt")
for m in open('mots.txt', encoding="UTF-8"):
   mon_mot = m.strip()
   if triple_double_lettres(mon_mot):
       print(mon_mot)

print("quadruples-doubles non consécutifs avec mots.txt")
for m in open('mots.txt', encoding="UTF-8"):
   mon_mot = m.strip()
   if quadruple_double_non_consecutifs(mon_mot):
       print(mon_mot)

print("quadruples-doubles non consécutifs avec words.txt")
for m in open('words.txt', encoding="UTF-8"):
   mon_mot = m.strip()
   if quadruple_double_non_consecutifs(mon_mot):
       print(mon_mot)