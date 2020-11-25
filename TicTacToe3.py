def ajouteSymbole(grille, joueur):
	i=0
	j=0
	choixIncorrect = True
	while (choixIncorrect):
		print("Sur quelle ligne voulez-vous jouer ?")
		i= int(input())
		print("Sur quelle colonne voulez-vous jouer?")
		j= int(input())
		if (grille[3*i+j]!='_'):
			grille[3*i+j]!=joueur
			choixIncorrect= False
	return