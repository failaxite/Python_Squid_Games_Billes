#CONSIGNES

#Créer un jeu RPG en Python style Squid Game

#le but est d'affronter une serie de joueur aux billes , au jeu du 'pair' ou 'impair'. Pour terminer le jeu vivant ,
# vous devez terminer toutes les parties en gardant au moins une bille en votre posséssion a la fin du jeu.

#Le jeu doit comporter 3 niveaux de difficultés :
#● Facile : 5 niveaux
#● Difficile : 10 niveaux
#● Impossible : 20 niveaux

#Le joueur doit choisir un niveau de difficulté.

#Lorsque vous démarrez le programme, vous devez saisir votre Personnage :
#● Seong Gi-hun
#○ Commence le jeu avec 15 billes
#○ Perd 2 billes en plus si une partie est perdue ! (malus)
#○ Gagne 1 bille en plus si une partie est gagnée ! (bonus)

#● Kang Sae-byeok
#○ Commence le jeu avec 25 billes
#○ Perd 1 billes en plus si une partie est perdue ! (malus)
#○ Gagne 2 billes en plus si une partie est gagnée ! (bonus)

#● Cho Sang-woo
#○ Commence le jeu avec 35 billes
#○ Perd 0 bille en plus si une partie est perdue ! (malus)
#○ Gagne 3 billes en plus si une partie est gagnée ! (bonus)

#Les caractéristiques des 3 joueurs doivent être enregistrées dans un tuple qui contient 3
#dictionnaires (les 3 personnages) avec leurs propriétés :
#● name - string (nom du Joueur)

#Liste chiffres pair et impaireee
from random import randrange

marblesSeong = 15  # number of marbles when playing with Seong
marblesKang = 25  # number of marbles when playing with Kang
marblesCho = 35  # number of marbles when playing with Cho

numberOfMarbles = 0
randomPlayer = randrange(1, 3)


def jouer(player, ennemy):
    print("{0} a {1} billes".format(player['name'], player['marbles']))
    print("player : ", player) # Trace pour mettre au point le programme. Une fois que c'est bon, tu peux le retirer
    print("ennemy : ", ennemy) # Trace pour mettre au point le programme. Une fois que c'est bon, tu peux le retirer
    numberOfMarbles = ennemy['marbles']
    userAnswer = input("Devine si le nombre de billes de {} est pair ou impair ".format(ennemy['name'])).lower()

    if ((numberOfMarbles % 2) == 0 and userAnswer == "pair") or ((numberOfMarbles % 2) == 1 and userAnswer == "impair"): #si la réponse du joueur est pair ou impaire
        gain = ennemy['marbles'] + player['gain'] # gain du tours = billes de l'ennemy + le gain du joueur qu'on a choisis
        player['marbles'] = player['marbles'] + gain # billes du joueur = bille du joueur + gain du tours
        print("Felicitation ! Le nombre de billes de {} etait pair.".format(player['name'])) # si le tour est gagné alors print le message de victoire du tour
        print("{} a gagné {} billes".format(player['name'], gain)) #print le résultat du tour

    else:
        loss = ennemy['marbles'] + player['loss'] # loss = billes de l'ennemy + billes du joueur
        player['marbles'] = player['marbles'] - loss # billes du joueur = bille du joueur - loss
        print("Mauvaise reponse.") # print que le joueur a mal répondu
        print("{} a perdu {} billes".format(player['name'], loss)) #print le résultat du tour

# liste des personnages qu'on peut choisir (3 au total)
characters_list = (
    {'name': 'Seong', 'marbles': 15, 'loss': 2, 'gain': 1},
    {'name': 'Kang', 'marbles': 25, 'loss': 1, 'gain': 2},
    {'name': 'Cho', 'marbles': 35, 'loss': 0, 'gain': 3},
)

# liste  de joueurs a affronter (20 au total)

ennemies_list = (
    {'name': '001', 'marbles': randrange(1, 20), 'age': 30},
    {'name': '002', 'marbles': randrange(1, 20), 'age': 18},
    {'name': '003', 'marbles': randrange(1, 20), 'age': 45},
    {'name': '004', 'marbles': randrange(1, 20), 'age': 27},
    {'name': '005', 'marbles': randrange(1, 20), 'age': 16},
    {'name': '006', 'marbles': randrange(1, 20), 'age': 25},
    {'name': '007', 'marbles': randrange(1, 20), 'age': 55},
    {'name': '008', 'marbles': randrange(1, 20), 'age': 22},
    {'name': '009', 'marbles': randrange(1, 20), 'age': 70},
    {'name': '010', 'marbles': randrange(1, 20), 'age': 63},
    {'name': '011', 'marbles': randrange(1, 20), 'age': 36},
    {'name': '012', 'marbles': randrange(1, 20), 'age': 27},
    {'name': '013', 'marbles': randrange(1, 20), 'age': 21},
    {'name': '014', 'marbles': randrange(1, 20), 'age': 30},
    {'name': '015', 'marbles': randrange(1, 20), 'age': 54},
    {'name': '016', 'marbles': randrange(1, 20), 'age': 31},
    {'name': '017', 'marbles': randrange(1, 20), 'age': 50},
    {'name': '018', 'marbles': randrange(1, 20), 'age': 25},
    {'name': '019', 'marbles': randrange(1, 20), 'age': 25},
    {'name': '020', 'marbles': randrange(1, 20), 'age': 25},
)

choix_difficulte = 0 #on défini la variable du choix de difficulté a 0
choix_joueur = 0 #on défini la variable du choix du joueur a 0

while choix_joueur not in  ['1', '2', '3']: #si le choix du joueur n'est pas 1 , 2 ou 3
    choix_joueur = input('Entre le nom du joueur que tu veux utiliser pour commencer la partie (1 , 2, 3) ')  #selection du joueur pour le jeu

choix_joueur = int(choix_joueur)
player = characters_list[choix_joueur - 1] # choix du personnage
print('Vous avez choisi de jouer avec {}'.format(player['name'])) # on print le choix du joueur

while choix_difficulte not in ['facile', 'moyen', 'difficile']: #si le choix du joueur n'est pas facile , moyen ou difficile
    choix_difficulte = input('Choisis la difficulté du jeu : Facile , Moyen , Difficile ').lower() #selection de la difficulté du jeu
print('Vous avez choisi ' + choix_difficulte) #on print le choix de la difficulté

if choix_difficulte == 'facile': #si le choix de difficulté est facile
    levels_dificulte = 5 #set le nombre de niveaux a 5
    print('Vous allez faire face a 5 adversaires') #print au joueur le nombre d'opposants qu'il va affronter

elif choix_difficulte == 'moyen': #si le choix de difficulté est moyen
    levels_dificulte = 10 #set le nombre de niveaux a 10
    print('Vous allez faire face a 10 adversaires') #print au joueur le nombre d'opposants qu'il va affronter

elif choix_difficulte == 'difficile': #si le choix de difficulté est difficile
    levels_dificulte = 20 #set le nombre de niveaux a 20
    print('Vous allez faire face a 20 adversaires') #print au joueur le nombre d'opposants qu'il va affronter

numberOfRounds = 0 # definition de la variable du nombre des rounds
while numberOfRounds < levels_dificulte:
    # Récuper l'adversaire suivant (solution simple)
    ennemy = ennemies_list[numberOfRounds]

    jouer(player, ennemy)

    if player['marbles'] <= 0: # si le nombre de billes du joueur est inférieur a 0
        print("{} a perdu. Il n'a plus de bille.".format(player['name'])) # print la phrase de défaite du joueur
        break

    numberOfRounds = numberOfRounds + 1

if player['marbles'] > 0: # si le nombre de billes du joueur est superieur a 0
    print("Felicitation ! ", "{} a gagné 45.6 milliards de Won !".format(player['name'])) # print la phrase de victoire du joueur





