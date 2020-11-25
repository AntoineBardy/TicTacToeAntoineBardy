def testeVictoireVertical (grille):
	compteur = 0
	while (compteur < 3):
		if (grille[compteur]!="_" and grille[compteur] == grille[compteur+3] and grille[compteur+6]):
			return True
	return False