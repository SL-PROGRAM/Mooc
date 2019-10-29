"""Auteur: Simon LEYRAL
   Date : Octobre 2017


Énoncé




Écrire une fonction replace(in_path, out_path, pattern, subst) qui ouvre le fichier dont le chemin est in_path, y
remplace toutes les occurrences sans chevauchement de pattern par subst, et écrit le résultat dans le fichier dont le
chemin est out_path.
Consignes

    On peut supposer que la chaîne pattern ne contient pas le caractère de fin de ligne.

    Le remplacement sans chevauchement de “aa” par “aaa” dans la chaîne “aaa” donne “aaaa”. Seule la première
    sous-chaîne “aa” est remplacée par “aaa”.

    Les fichiers utilisés par UpyLaB pour tester la fonction sont accessibles aux adresses suivantes :

            https://upylab.ulb.ac.be/pub/data/Zola.txt

            https://upylab.ulb.ac.be/pub/data/le-petit-prince.txt




"""

def replace(in_path, out_path, pattern, subst):
    out = []
    for lign in open(in_path, encoding="utf-8"):
        if pattern in lign:
            new_lign = lign.replace(pattern, subst)
        else:
            new_lign = lign
        out.append(new_lign)

    f_out = open(out_path, "w", encoding="utf-8")
    for elem in out:
        f_out.write(elem)
    f_out.close()

replace("words.txt", "test.txt", "aa", "aaaaaaaaaaaaaaaaa")