"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Écrire une fonction store_email(liste_mails) qui reçoit en paramètre une liste d’adresses e-mail et qui renvoie un
 dictionnaire avec comme clés les domaines des adresses e-mail et comme valeurs les listes d’utilisateurs
 correspondantes, triées par ordre croissant (UTF-8).


Consignes

Dans cet exercice, il vous est demandé d’écrire seulement la fonction store_email.

Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait
en particulier aucun appel à input ou à print.


"""
def store_email(lst_mail):
    dico_mail = {}
    for mail in lst_mail:
        mail = mail.split("@")
        dico_mail.setdefault (mail[1])
        if type(dico_mail[mail[1]]) != list:
            dico_mail[mail[1]] = []
        dico_mail[mail[1]].append(mail[0])
        dico_mail[mail[1]].sort()
    return dico_mail


print(store_email(['ludo@prof.ur', 'andre.colon@stud.ulb', 'thierry@profs.ulb', 'sébastien@prof.ur', 'eric.ramzi@stud.ur', 'bernard@profs.ulb', 'jean@profs.ulb']))
print({'profs.ulb': ['bernard', 'jean', 'thierry'], 'prof.ur': ['ludo', 'sébastien'], 'stud.ulb': ['andre.colon'], 'stud.ur': ['eric.ramzi']})