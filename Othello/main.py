#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import othello
import sys
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain

jeu = game.initialiseJeu()
game.affiche(jeu)

print("coups valides pour le joueur", jeu[1], ":", game.getCoupsValides(jeu))

