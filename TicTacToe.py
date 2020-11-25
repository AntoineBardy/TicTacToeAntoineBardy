#TicTacToe Fonction
def initialiseGrille (grille):
	compteur = 0
	for compteur in range (0, 9):
		grille[compteur] = "_"
	return

def affichegrille (grille):
	i=0
	for i in range (0,3):
		print(grille[3*i], grille[3*i+1], grille[3*i+2], "\n")
	return

def ajouteSymbole(grille, joueur):
	i=0
	j=0
	choixIncorrect = True
	while (choixIncorrect):
		print("Sou ki liy ou vle jwe 0,1 ou 2?")
		i= int(input())
		print("Sou ki kolòn ou vle jwe 0, 1 ou 2?")
		j= int(input())
		if (grille[3*i+j]=="_"):
			grille[3*i+j]=joueur
			choixIncorrect= False
	return

def testeVictoireHorizontale (grille):
	compteur = 0
	while (compteur < 3):
		if (grille[compteur]!='_' and grille[compteur*3]== grille[compteur*3+1] and grille[compteur*3] == grille[compteur*3+2]):
			return True
	return False

def testeVictoireVertical (grille):
	compteur = 0
	while (compteur < 3):
		if (grille[compteur]!="_" and grille[compteur] == grille[compteur+3] and grille[compteur+6]):
			return True
	return False

def testeVictoireDiagonale (grille):
	if (grille[compteur]!="_" and grille[4] == grille[0] and grille [4] == grille[8]):
		return True
	elif (grille[compteur]!="_" and grille[4] == grille[2] and grille [4] == grille[6]):
		return True
	return False

def testJeuNul(gagnantTrouvé,tour):
	if(tour == 9 and gagnantTrouvé == False):
		return True
	return False

#Variables
tableau = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
initialiseGrille(tableau)
affichegrille(tableau)
while () :

ajouteSymbole(tableau,"O")
affichegrille(tableau)
ajouteSymbole(tableau,"X")
affichegrille(tableau)
ajouteSymbole(tableau,"O")
affichegrille(tableau)
ajouteSymbole(tableau,"X")
affichegrille(tableau)
ajouteSymbole(tableau,"O")
affichegrille(tableau)
ajouteSymbole(tableau,"X")
affichegrille(tableau)
ajouteSymbole(tableau,"O")
affichegrille(tableau)
ajouteSymbole(tableau,"X")
affichegrille(tableau)
ajouteSymbole(tableau,"O")
affichegrille(tableau)
testeVictoireHorizontale(tableau)
testeVictoireVertical(tableau)
testeVictoireDiagonale(tableau)
testJeuNul(False, 0)
input()