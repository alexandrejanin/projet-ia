#!/usr/bin/env python
# -*- coding: utf-8 -*-

def initialiseJeu():
    plateau = [[4] * 6 for x in range(2)]
    
    joueur = 1
    coups_possibles = None
    coups_joues = []
    scores  = [0, 0]

    return [plateau,
            joueur,
            coups_possibles,
            coups_joues,
            scores
            ]

def getCoupsValides(jeu):
    plateau = jeu[0]
    
    joueur = jeu[1]

    coups = [(joueur - 1, x) for x in range(6) if plateau[joueur - 1][x] != 0]

    return coups
