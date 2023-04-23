import random
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import time


FILENAME = "./repertoire_francais_tout.txt"

labels = []


def timeit(func):
    """Décorateur qui calcule le temps d'exécution d'une fonction."""
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


def indices(mot: str) -> str:
    """Calcule l'indice d'un mot.

    Args:
        mot (str): mot à calculer l'indice

    Returns:
        str: indice du mot
    """
    indice = list(mot.upper()) # upper() permet de mettre en majuscule comme cela on ne se soucie pas de la case
    indice.sort()
    return "".join(indice)


@timeit
def dictWordIndices(listes: list) -> dict:
    """Crée un dictionnaire avec comme clé l'indice d'un mot et comme valeur la liste des mots qui ont cet indice.

    Args:
        listes (list): Liste de mots

    Returns:
        dict: Dictionnaire avec comme clé l'indice d'un mot et comme valeur la liste des mots qui ont cet indice
    """
    ans = {}
    for x in listes:
        if indices(x) not in ans:
            ans[indices(x)] = [x]
        else:
            ans[indices(x)].append(x)
    return ans


def drawLetters(n: int) -> list:
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


@timeit
def longestWord() -> str:
    """Cette fonction répond à l'entièreté de l'activité 4. Elle renvoie des mots possibles à partir d'un tirage (d'une longueur maximale).
    Elle ne donnera pas des mots possédant des lettres différents entre eux pour être la plus rapide possible.

    Returns:
        list: liste de mots possibles à partir d'un tirage de longueur maximale
    """
    start_time = time.perf_counter()
    global dico
    tirage = indices(lettersVar.get()) # lettersVar est une variable de type StringVar qui contient la valeur de l'Entry
    if "dico" not in globals(): # Si le dictionnaire n'existe pas encore
        with open(FILENAME, "r") as f:
            data = f.read().splitlines()
            dico = dictWordIndices(data)
    binary_counts = sorted([(f"{i:0{len(tirage)}b}", bin(i).count("1")) for i in range(2 ** len(tirage))], key=lambda x: x[1], reverse=True) # On trie les nombres binaires par ordre décroissant de 1
    for binary, count in binary_counts: # On parcourt les nombres binaires
        temp = [tirage[x] for x in range(len(tirage)) if binary[x] == "1"] # On récupère les lettres du tirage qui sont à 1 en binaire
        if indices("".join(temp)) in dico:
            return " ".join(dico[indices("".join(temp))]) + f" {time.perf_counter() - start_time:.4f}s"
    return "Pas de mot possible" + f" {time.perf_counter() - start_time:.4f}s"


# ### GUI ### #

@timeit
def addWord() -> None:
    """Ajouter le résultat en label"""
    global labels
    while len(labels) * 75 > window.winfo_height(): # Tant que les labels prennent plus de place que la fenêtre, on enlève le premier label
        labels[0].destroy()
        labels.pop(0)
    label = tk.Label(ansFrame, text=longestWord(), font=("Arial", 25), bg="#334756", fg="white")
    labels.append(label)
    label.pack(pady=10)


def changeDict() -> None:
    """Permet de changer le dictionnaire"""
    global dico
    global FILENAME
    if "dico" in globals(): # Si le dictionnaire existe, on le supprime
        del dico
    filename = filedialog.askopenfilename(initialdir=".", title="Selectionner un fichier", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    FILENAME = filename


window = tk.Tk()
window.iconphoto(False, tk.PhotoImage(file="images/icon.png")) # Icone de la fenêtre
window["bg"] = "#2C394B"
window.geometry("1000x500")
window["pady"] = 10
lettersVar = tk.StringVar()
window.title("Mot le plus long")

entryFrame = tk.Frame(window, highlightthickness=2, highlightbackground="#082032", bg="#2C394B")
ansFrame = tk.Frame(window, bg="#2C394B")
lettersEntry = tk.Entry(entryFrame, bg="#334756", fg="white", textvariable=lettersVar, width=75)

# ## Images ## #

send = Image.open("./images/paper-plane-border.png") # On ouvre l'image
send = send.resize((30, 30), Image.ANTIALIAS) # On redimensionne l'image
send = ImageTk.PhotoImage(send) # On convertit l'image en format utilisable par tkinter
rnd = Image.open("./images/dice-border.png")
rnd = rnd.resize((30, 30), Image.ANTIALIAS)
rnd = ImageTk.PhotoImage(rnd)
dictionary = Image.open("./images/spell-check-border.png")
dictionary = dictionary.resize((50, 50), Image.ANTIALIAS)
dictionary = ImageTk.PhotoImage(dictionary)

# ## Boutons ## #

submitBtn = tk.Button(entryFrame, command=addWord, width=30, height=30, image=send, borderwidth=0, bg="#2C394B", activebackground="#2C394B", highlightthickness=0, relief="flat")
randomBtn = tk.Button(entryFrame, image=rnd, command=lambda: lettersVar.set("".join(drawLetters(9))), bg="#2C394B", activebackground="#2C394B", borderwidth=0, highlightthickness=0, relief="flat")
changeBtn = tk.Button(window, image=dictionary, command=lambda: changeDict(), bg="#2C394B", activebackground="#2C394B", highlightthickness=0, relief="flat", width=50, height=50, borderwidth=0)

# ## Affichage ## #

entryFrame.pack()
ansFrame.pack()
lettersEntry.grid(row=0, column=0, padx=10, pady=10)
submitBtn.grid(row=0, column=1, padx=10, pady=10)
randomBtn.grid(row=0, column=2, padx=10, pady=10)
changeBtn.place(rely=1.0, relx=1.0, x=-10, y=0, anchor=tk.SE) # On place le bouton en bas à droite

window.bind("<Return>", lambda e: addWord()) # Permet d'appuyer sur entrée pour ajouter un mot

tk.mainloop()
