#functie om te kijken of iemand een boete verdient en zo ja hoe hoog
def hoogteBoete (snelheid):
    if snelheid < 55:
        return "ok" 
    elif snelheid < 60:
        return 10

    elif snelheid < 65:
        return 20

    elif snelheid < 70:
        return 30

    elif snelheid < 75:
        return 40

    elif snelheid < 80:
        return 50

    elif snelheid == 80:
        return 60

    if snelheid > 80:
        return "rijbewijs kwijt"

