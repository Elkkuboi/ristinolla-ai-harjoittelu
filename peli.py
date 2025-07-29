'''
Tänne tulee pelimoottori ristinollaan.
'''

import random
import json



def luo_lauta():
    """Luo uuden pelilaudan."""
    return [0] * 9



def tulosta_lauta(lauta):
    """Tulostaa pelilaudan."""
    symbolit = {0: " ", 1: "X", -1: "O"}
    for i in range(3):
        rivi = [symbolit[lauta[3 * i + j]] for j in range(3)]
        print(" | ".join(rivi))
        if i < 2:
            print("----------")
    



def hae_mahdolliset_siirrot(lauta):
    """Palauttaa listan mahdollisten siirtojen indekseistä."""
    pelattavat = []
    for i in range(9):
        if lauta[i] == 0:
            pelattavat.append(i)
    return pelattavat



def tee_siirto(lauta, siirto, pelaaja):
    """Pelaa siirron JOS se on laillinen"""
    if 0 <= siirto < 9 and lauta[siirto] == 0:
        lauta[siirto] = pelaaja
        return True
    else:
        return False



def tarkista_voitto(lauta):
    """Tarkistaa onko pelaaja voittanut"""

    voittokuviot = [
        [0,1,2], [3,4,5], [6,7,8], # vaakarivit
        [0,3,6], [1,4,7], [2,5,8], # pystyrivit
        [0,4,8], [2,4,6]           # vinorivit
    ]
    for kuvio in voittokuviot:
        a, b, c = kuvio
        # Tarkistetaan ovatko ruudut epätyjät ja saman arvoiset
        if lauta[a] != 0 and lauta[a] == lauta[b] == lauta[c]:
            return lauta[a]
    return 0
                


def tarkista_tasapeli(lauta):
    """Tarkistaa onko peli tasapeli"""
    if 0 in lauta:
        return False
    
    if tarkista_voitto(lauta) != 0:
        return False
    
    return True




