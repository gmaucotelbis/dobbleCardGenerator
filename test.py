import sys

def plan_projectif(modulo):
    """Generation d'un plan projectif Rel
    Il est compose d'un plan affine (une matrice) et
    des points a l'infini du plan reel.
    Des symboles uniques sont definis pour chaque
    points du plan affine et chaque point a l'infini.
    (ici un index de 0 a l'infini)
    plan_affine, pts_infini = plan_projectif(3)
    plan_affine == [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8]]
    pts_infini == [9, 10, 11, 12]
    """
    plan_affine = []
    pts_infini = []
    index = 0

    # Generation du plan affine 
    for i in range(modulo):
        plan_affine.append([])
        for j in range(modulo):
            plan_affine[i].append(index)
            index += 1

    # Generation des points a l'infini
    for i in range(modulo + 1):
        pts_infini.append(index)
        index += 1
    
    return {
        'plan_affine': plan_affine,
        'pts_infini': pts_infini,
    }


def droite(modulo, plan, a, b, f=None):
    """Trace une droite dans le plan projectif et retourne
    tous les points par laquelle elle est passee"""
    coords = []
    points = []

    # Calcul des coordonnes de tous les points
    for i in range(modulo):
        if f is None:
            # f(x) = ax + b
            # On applique l'operateur modulo parce que le resultat
            # n'est pas un nombre entier, mais un nombre modulo
            x = i % modulo
            y = (a * i + b) % modulo
        else:
            # f(0), f(1), f(2) ... f(modulo)
            x = f
            y = i % modulo

        coords.append({'x': x, 'y': y})

    # Recuperation des points dans le plan affine
    for c in coords:
        points.append(plan['plan_affine'][c['y']][c['x']])

    # Recuperation du dernier points dans les points a l'infini
    if f is None:
        points.append(plan['pts_infini'][a + 1])
    else:
        points.append(plan['pts_infini'][0])

    return points


def droites(modulo, plan):
    """Recupere toutes les droites possible d'un plan projectif"""
    liste = []

    # Lignes verticales
    for i in range(modulo):
        liste.append(droite(modulo, plan, 0, 0, f=i))

    # Lignes pour f(x) = ax + b
    for a in range(modulo):
        for b in range(modulo):
            liste.append(droite(modulo, plan, a, b))

    # Enfin, la ligne qui passe par tous les points a l'infini
    liste.append(plan['pts_infini'])

    return liste


if __name__ == '__main__':
    # Asmodee a choisi de generer un jeu de carte avec
    # huit symboles par carte, pour ca, il faut generer
    # un plan projectif avec un nombre entier modulo de 7
    # (le nombre choisi par Asmodee)
    #
    # C'est une constante, mais on peut calculer le modulo
    # Avec le nombre total de symboles, le nombre de carte
    # Et donc le nombre de symbole par carte. (non inclus)
    try:
        modulo = int(sys.argv[1])
    except (IndexError, ValueError):
        modulo = 11

    plan = plan_projectif(modulo)

    # Affiche une liste que l'on peut comparer a un deck
    # qui contient un nombre de 8 elements par carte, tout
    # comme Dobble (meme si Asmodee a volontairement choisi
    # de retirer deux cartes)
    # Qui possede les proprietes suivantes :
    # - Chaque carte est unique ;
    # - Chaque carte a le meme nombre de symbole que toutes
    #   les autres ;
    # - Chaque carte possede un et un seul element en commun
    #   avec toutes les cartes.
    deck = droites(modulo, plan)

    print('Nombre de cartes', len(deck))
    print('Toutes les cartes :')
    for i, carte in enumerate(deck):
        print('#{}'.format(i), carte)
