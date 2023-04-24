import random


FILENAME = "repertoire_francais_tout.txt"


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


def tirage_lettres(n: int) -> list:
    """Tire n lettres au hasard dans l'alphabet en tenant compte du nombre de plaques.

    Args:
        n (int): nombre de lettres à tirer

    Returns:
        list: liste de n lettres tirées au hasard
    """
    lettersList = ["A", "E", "I", "O", "U"] * 5 + ["B", "C", "D", "F", "G", "H", "L", "M", "N", "P", "R", "S", "T"] * 2 + ["K", "J", "Q", "V", "W", "X", "Y", "Z"]
    ans = []
    while n > 0:
        randomPos = random.randint(0, len(lettersList) - 1)
        ans.append(lettersList[randomPos])
        lettersList.pop(randomPos)
        n -= 1
    return ans


def liste_binaire(n: int) -> list:
    """Renvoie toute les liste formées de 0 et de 1 de longueur n.

    Args:
        n (int): longueur des listes

    Returns:
        list: liste de toutes les listes formées de 0 et de 1 de longueur n
    """    """"""
    ans = []
    for i in range((2 ** n) - 1, 0, -1):
        ans.append(list(f"{i:0{n}b}")) # f"{i:0{n}b}" est un f-string qui permet de convertir i en binaire (grâce au b) et de le mettre dans une chaine de caractère de longeur n (le 0{n})
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            ans[i][j] = int(ans[i][j])
    return ans


def indices_depuis_tirage(tirage: list) -> list:
    """Renvoie la liste de tous les indices possibles à partir d'un tirage.

    Args:
        tirage (list): liste de lettres tirées au hasard

    Returns:
        list: liste de tous les indices possibles à partir d'un tirage
    """
    ans = []
    tirage.sort()
    for i in liste_binaire(len(tirage)):
        temp = ""
        for j in range(len(i)):
            if i[j] == 1:
                temp += tirage[j]
        ans.append(temp)
    return ans


def mot_le_plus_long(tirage: list, dico: dict) -> str:
    """Renvoie le mot le plus long à partir d'un tirage et d'un dictionnaire.

    Args:
        tirage (list): liste de lettres tirées au hasard
        dico (dict): dictionnaire avec comme clé l'indice d'un mot et comme valeur la liste des mots qui ont cet indice

    Returns:
        str: mot le plus long à partir d'un tirage et d'un dictionnaire
    """
    mots = []
    for i in indices_depuis_tirage(tirage):
        if i in dico:
            mots += dico[i]
    mots.sort(key=len, reverse=True)
    return mots[0]


with open(FILENAME, "r") as f:
    data = f.read().splitlines()
dico = dictionnaire_indices_mots(data)

tirage = tirage_lettres(10)
print(tirage)
print(mot_le_plus_long(tirage, dico))


def rechercheDichotomique(word: str, liste: list) -> int:
    """Vu que je ne l'utilise pas de tous le TP, le voila pour prouver que je peux le faire.

    Args:
        word (str): mot à chercher
        liste (list): liste triée dans laquelle chercher

    Returns:
        int: index du mot dans la liste ou -1 si le mot n'est pas dans la liste
    """
    deb = 0
    fin = len(liste) - 1
    while deb <= fin:
        milieu = (deb + fin) // 2
        if liste[milieu] == word:
            return milieu
        elif liste[milieu] > word:
            fin = milieu - 1
        else:
            deb = milieu + 1
    return -1 # -1 signifie que le mot n'a pas été trouvé (mieux que None)


print(rechercheDichotomique("DINOSAURES", data))
