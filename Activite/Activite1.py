def calculer_indice(mot: str) -> str:
    """Calcule l'indice d'un mot.

    Args:
        mot (str): mot à calculer l'indice

    Returns:
        str: indice du mot
    """
    indice = list(mot.upper()) # upper() permet de mettre en majuscule comme cela on ne se soucie pas de la case
    indice.sort()
    return "".join(indice)


def sont_anagrammes(mot1: str, mot2: str) -> bool:
    """Vérifie si deux mots sont des anagrammes.

    Args:
        mot1 (str): Premier mot à vérifier
        mot2 (str): Deuxième mot à vérifier

    Returns:
        bool: True si les deux mots sont des anagrammes, False sinon
    """
    return calculer_indice(mot1) == calculer_indice(mot2)


def dictionnaire_indices_mots(listes: list) -> dict:
    """Crée un dictionnaire avec comme clé l'indice d'un mot et comme valeur la liste des mots qui ont cet indice.

    Args:
        listes (list): Liste de mots

    Returns:
        dict: Dictionnaire avec comme clé l'indice d'un mot et comme valeur la liste des mots qui ont cet indice
    """
    ans = {}
    for x in listes:
        if calculer_indice(x) not in ans:
            ans[calculer_indice(x)] = [x]
        else:
            ans[calculer_indice(x)].append(x)
    return ans


def fichier_indice_mots(fichier_in: str, fichier_out: str) -> None:
    """Crée un fichier avec comme clé l'indice d'un mot et comme valeur la liste des mots qui ont cet indice.

    Args:
        fichier_in (str): chemin du fichier d'entrée
        fichier_out (str): chemin du fichier de sortie
    """    """"""
    with open(fichier_in, "r") as f:
        data = f.read().splitlines()
    with open(fichier_out, "w") as f:
        objs = str(dictionnaire_indices_mots(data)).replace(']', '\n').replace(',', '').replace("'", '').replace('[', '')[1:-2].split('\n')
        for objpos in range(len(objs)):
            objs[objpos] = objs[objpos].strip() # Pour enlever les espaces
        f.write("\n".join(objs))


print(calculer_indice("kayak"))
print(sont_anagrammes("chien", "niche"))
print(dictionnaire_indices_mots(["CRIME", "COUCOU", "PRIERES", "MERCI", "RESPIRE", "REPRISE"]))

with open("repertoire_francais_tout.txt", "r") as f:
    listFrenchWords = f.read().splitlines() # Pour ne pas conserver les \n on utilise read puis splitlines qui crée une liste comme readlines mais sans les \n

print(len(dictionnaire_indices_mots(listFrenchWords))) # On trouve 116534 couple d'anagramme (en comptant les mots avec un indice unique) avec le fichier tout
fichier_indice_mots("repertoire_francais_tout.txt", "anagrammes.txt")
