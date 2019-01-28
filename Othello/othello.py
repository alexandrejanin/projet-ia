#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1 = noir, 2 = blanc

def initialiseJeu():
    # etat initial du plateau
    plateau = [[0] * 8 for x in range(8)]
    plateau[3][3] = 2
    plateau[3][4] = 1
    plateau[4][3] = 1
    plateau[4][4] = 2
    
    joueur = 1

    coups_possibles = None
    coups_joues = []

    scores = [2, 2]

    return [plateau,
            joueur,
            coups_possibles,
            coups_joues,
            scores
            ]

    
def getCoupsValides(jeu):
    joueur = jeu[1]
    joueur_adverse = 3 - joueur

    plateau = jeu[0]
    nb_lignes = len(plateau)
    nb_colonnes = len(plateau[0])

    coups = []

    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):
            if plateau[ligne][colonne] == joueur:
                for coup in coupsValides(jeu, (ligne, colonne), joueur):
                    if not coup in coups:
                        coups.append(coup)


    return coups



def coupsValides(jeu, case, joueur):
    ligne, colonne = case

    plateau = jeu[0]
    nb_lignes = len(plateau)
    nb_colonnes = len(plateau[0])

    joueur_adverse = 3 - joueur

    coups = []

    for y_dir in [-1, 0, 1]:
        for x_dir in [-1, 0, 1]:
            y = ligne + y_dir
            x = colonne + x_dir
            
            while y >= 0 and y < nb_lignes and x >= 0 and x < nb_colonnes:
                if plateau[y][x] == joueur:
                    break
                elif plateau[y][x] == 0:
                    if plateau[y-y_dir][x-x_dir] == joueur_adverse:
                        coups.append((y,x))
                    break

                y += y_dir
                x += x_dir

    return coups

def compterScore(jeu, joueur):
    """int -> int
    joueur = 1 ou 2
    """
    score = 0

    for ligne in jeu[0]:
        for case in ligne:
            if case == joueur:
                score += 1

    return score

