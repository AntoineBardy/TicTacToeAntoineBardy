def testeVictoireHorizontale (grille):
	compteur = 0
	while (compteur < 3):
		if (grille[compteur]!='_' and grille[compteur*3]== grille[compteur*3+1] and grille[compteur*3] == grille[compteur*3+2]):
			return True
	return False