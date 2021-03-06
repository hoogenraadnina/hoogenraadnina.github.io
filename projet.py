import turtle
turtle.tracer(0,0)            # accélération du tracé
turtle.screensize(2000,2000)  # taille fenêtre graphique
turtle.pu()
turtle.goto(-500,0)
turtle.pd()

def dessiner(courbe, longueur, angle):    
    """ réalise une représentation graphique d'une courbe donnée par des chaines de caractères """
    for caractere in courbe:
        if caractere == '+': turtle.left(angle)
        elif caractere == '-': turtle.right(angle)
        elif caractere in ['F', 'G']: turtle.forward(longueur)


#dessiner('F', 50, 60)

def regleKoch(chaine):
    nouvelleChaine = ''    # on crée une nouvelle chaine de caractères VIDE
    for lettre in chaine:  # on épelle la chaine de caractères donnée en paramètres
        if lettre == 'F':  # si dans l'ancienne chaine, il y a un 'F'
            nouvelleChaine = nouvelleChaine + 'F-G+F+G-F'  # alors, on écrit F+F--F+F dans la nouvelle chaine
        elif lettre == 'G' :
            nouvelleChaine = nouvelleChaine + 'GG'
        else :
            nouvelleChaine = nouvelleChaine + lettre
    return nouvelleChaine


def courbeKoch(motifInitial, niter):
    """ 
        appelle niter fois regleKoch pour créer la courbe de Koch
    """
    courbe = motifInitial # on part du motif initial donné par l'utilisateur en paramètres
    for i in range(niter):
        nouveauMotif = regleKoch(courbe)  # on trouve le nouveau Motif à partir du motif de départ
        courbe = nouveauMotif # on dit que le nouveau Motif est maintenant le motif de départ
    return courbe



#courbe = courbeKoch('F',3)
#dessiner(courbe,50, 60)

def triangle(motifInitial, niter):
    courbe = courbeKoch(motifInitial, niter)
    carre = ''
    for _ in range(3):
        triangle += courbe
        triangle += '--' 
    return triangle

longueur = 2
angle = 60
niter = 6
dessiner(courbeKoch('F-G-G',3),40,120)


turtle.update()      # accélération du tracé
turtle.exitonclick() # permet la fermeture de la fenêtre graphique
