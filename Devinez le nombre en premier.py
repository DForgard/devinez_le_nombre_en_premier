# Le but est de jouer contre l'ordinateur.

import random

# Choisir un chiffre aléatoire entre 0 et 100
int_guess: int = random.randint(0,100)

print("Bienvenue ! Un chiffre à été choisi de façon aléatoire entre 0 et 100. Peux-tu le deviner avant l'ordinateur ?")

# Compter le nombre de tentatives du joueurs.
attempt_count: int = 0

# Les possibilités de l'ordinateur.
computer_options: list = list(range(101))

# Booléen pour savoir à qui c'est le tour de jouer.
my_turn: bool = True

# Faire une boucle qui va demander au joueur de deviner le chiffre.
# On lui demande autant de fois qu'il faut jusqu'à ce qu'il trouve.
while True:

    if my_turn:
        # Demander un chiffre au joueur.
        user_guess: str = input("Ta suggestion: ")

        # Incrementer le compteur de tentatives.
        attempt_count += 1

        # Vérifier que le joueur a entré un chiffre.
        if not user_guess.isdigit():
            print("Je n'ai pas reconnu ta suggestion. Essai encore en entrant un chiffre entre 0 et 100.")
            continue
        
        # Convertir la suggestion du joueur en int.
        user_guess: int = int(user_guess)
    
    else:
        mid_index = len(computer_options) // 2
        user_guess: int = computer_options[mid_index]
        print("L'ordinateur choisi:", user_guess)

    # Vérifier que c'est le bon chiffre.
    if user_guess == int_guess:
        print(f"Bien joué ! Le bon chiffre était {int_guess}.")
        break
    # Si ce n'est pas le bon chiffre, donné un indice au joueur.
    elif user_guess < int_guess:
        print("Trop petit !")

        # Vérifier que la suggestion fait partie des possibilité restantes.
        if user_guess in computer_options:
            user_guess_index = computer_options.index(user_guess) + 1
            computer_options = computer_options[user_guess_index:]

    elif user_guess > int_guess:
        print("Trop grand !")

        if user_guess in computer_options:
            user_guess_index = computer_options.index(user_guess)
            computer_options = computer_options[:user_guess_index]
    
    # Donner le tour au prochain joueur.
    my_turn = not my_turn

# Afficher le nombre de tentatives nécessaires pour avoir trouvé le chiffre.
if my_turn:
    print("Bien joué ! Tu as trouvé le bon chiffre en", attempt_count, "coups et avant l'ordinateur !")
else:
    print(f"L'ordinateur gagne ! Il as trouvé le bon chiffre en", attempt_count, "coups et avant toi !")
