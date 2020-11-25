def testeVictoireDiagonale (grille):
	if (grille[compteur]!="_" and grille[4] == grille[0] and grille [4] == grille[8]):
		return True
	elif (grille[compteur]!="_" and grille[4] == grille[2] and grille [4] == grille[6]):
		return True
	return False