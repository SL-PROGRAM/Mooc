"""Auteur: Simon LEYRAL
   Date : Octobre 2017

Enoncé

Voici le début d’une suite logique inventée par John Horton Conway (et connue donc sous le nom de suite de Conway).

1
1 1
2 1
1 2 1 1
1 1 1 2 2 1
3 1 2 2 1 1
...

Chaque ligne, à partir de la deuxième, décrit la précédente :

    la première ligne, 1, est formée de un “1”, d’où la deuxième ligne : 1 1 ;

    la troisième ligne décrit la deuxième ligne, où l’on voit deux “1”, d’où 2 1 ;

    la quatrième ligne décrit la troisième ligne, où l’on voit un “2” et un “1”, d’où 1 2 1 1 ;

    et ainsi de suite.

Écrire une fonction next_line(line) qui reçoit une liste d’entiers décrivant une ligne de cette suite, et qui
retourne la liste correspondant à la ligne suivante.


Consignes

    Dans cet exercice, il vous est demandé d’écrire seulement la fonction next_line. Le code que vous soumettez à
    UpyLaB doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel
     à input ou à print.

    Notez que l’appel next_line([]) sur la liste vide retourne par convention la liste [1].



"""

def next_line(line):
    next_line = []
    if not line:
        next_line = [1]
    elif line == [1]:
        next_line = [1,1]
    else:
        i=1
        count = 1
        value = line[i - 1]
        while i < len(line):
            if line[i-1] == line[i]:
                count += 1
                if i+1 == len(line):
                    value = line[i]
                    next_line.extend([count])
                    next_line.extend([value])
            else:
                value = line[i - 1]
                next_line.append(count)
                next_line.append(value)
                count = 1
                if i+1 == len(line):
                    next_line.extend([1])
                    next_line.extend([line[i]])
            i+=1

    return next_line

print(next_line([1, 1, 1, 2, 2, 1]))