'''
Tänne tulee pelimoottori ristinollaan.
'''




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







''' Luodaan luokka botille ja alustetaan botin toiminta '''
import random
import json

class robotti:
    def __init__(self, oppimisnopeus = 0.1, epsilon = 0.1):
        """
        Alustetaan robotti ja sen muuttujat
        """

        self.arvot = {} # (tila, arvo) parit. Tila tarkoittaa siis laudan asentoa, ja kenen vuoro tuplea
        self.oppimisnopeus = oppimisnopeus # kuinka paljon uusi opittu vaikuttaa vanhaan tietoon?
        self.epsilon = epsilon             # kuinka paljon botti kokeilee jotain uutta?


    def lataa_arvot(self, tiedostonimi = "arvot.json"):
        """ lataa opitut arvot JSON tiedostosta"""
        try:
            with open(tiedostonimi) as tiedosto:
                ladatut_arvot = json.load(tiedosto)
                # HUOM, avaimet merkkijonoja!

                # muutettaan merkkijonoavaimet takaisin tupleiksi
                # k tarkoittaa avainta ja v arvoa
                # eval muuttaa merkkijonon takaisin osoittamaansa muotoon (eli tupleksi)
                self.arvot = {eval(k): v for k, v in ladatut_arvot.items()}
                print("Arvot ladattu")
            
        except FileNotFoundError:
            # jos tiedostoa ei löydy, aloitetaan tyhjällä
            print("tiedostoa ei löytynyt, aloitetaan tyhjällä")
            pass


    def hae_arvot(self, tila_tupple):
        """
        Hakee tilan arvon ja palauttaa 0.5 jos uusi
        """
        return self.arvot.get(tila_tupple, 0.5) 
    # tupleen kuuluu siis laudan asento, ja kenen vuoro on
    # (sanakirjan avain ei voi olla "muuttuva", joten käytämme tupleja)       


    def valitse_siirto(self, lauta, pelaaja, mahdolliset_siirrot):
        """ Valitsee siirron, satunnaisesti välillä botti kokeilee jotain uutta"""
        
        # kokeileeko botti jotain uutta?
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(mahdolliset_siirrot)
        

        # jos ei, mennään parhaalla tiedolla
        paras_arvo = -1
        paras_siirto = mahdolliset_siirrot[0]

        for siirto in mahdolliset_siirrot:
            # simuloidaaan siirto tekemällä kopioimalla lauta ja pelaamalla siirto
            tuleva_lauta = lauta[:]
            tuleva_lauta[siirto] = pelaaja

            # tallennetaan tupleksi, vaihdetaan siirto ja haetaan arvo
            tuleva_tila_tuple = (tuple(tuleva_lauta), -pelaaja)
            # meidän pitää ottaa 1 - vastustajan arvo seuraavassa tilanteessa
            # koska vuoro vaihtuu ja emme halua että arvo kertoo vastustajan arvoa 
            arvo = 1 - self.hae_arvot(tuleva_tila_tuple)

            # arvoidaan onko siirto paras
            if arvo > paras_arvo:
                paras_arvo  = arvo
                paras_siirto = siirto
        
        return paras_siirto
    
    def paivita_arvot(self, edellinen_tila, nykyinen_tila, palkinto = None):
        """ tilat ovat tupleja tilanteesta (eli lautatuple ja kenen vuoro)"""
        """ Funktio päivittää edellisen tilan arvon uuden tiedon perusteella"""
        """ Funktiossa varaudutaan siihen, että treenatessa botille annetaan tietynlaisia palkintoja"""
        vanha_arvo = self.hae_arvot(edellinen_tila)

        # tarkastetaan, tuliko palkintoa ja päivitetään arvo
        if palkinto:
            tuleva_arvo = palkinto

        # jos ei palkintoa, niin
        # hae arvot kysyy: kuinka hyvä tilanne on sille kenen vuoro on?
        # koska vuoro vaihtuu, niin meidän on vähennettävä tämä arvo yhdestä
        else:
            tuleva_arvo = 1 - self.hae_arvot(nykyinen_tila)

        """    
        Oppimiskaava muuttaa arvoa epsilonin osuuden verran nykyisen ja menneen tilanteen arvon eroituksesta.
        Eli botti kysyy mikä on nykyinen tilanne vastustajalle. (eli botille 1 - vastustajan tilanne)
        Jos meidän nykyinen tilanne on parempi kuin äskeinen, niin äskeinen tilanne onkin hieman parempi, koska
        voimme pelata tämän siirron joka parantaa tilannettamme. Tällä tavalla botin tieto leviää alkua kohti
        """

        uusi_arvo = vanha_arvo + self.oppimisnopeus * (tuleva_arvo - vanha_arvo)
        self.arvot[edellinen_tila] = uusi_arvo

    def tallenna_arvot(self, tiedostonimi = "arvot.json"):
        """Tallentaa opitut arvot JSON-tiedostoon, päällekirjoitetaan kokonaan uudella tiedolla"""
        with open(tiedostonimi, "w") as tiedosto:
            # muutetaan tuple-avaimet merkkijonoksi
            # k tarkoittaa avainta ja v arvoa, se muuttaa siis vain avaimen eli tilan tuplen merkkijonoksi
            json_arvot = {str(k): v for k, v in self.arvot.items()}
            json.dump(json_arvot, tiedosto)
        


'''botti-luokka on nyt määritelty, seuraavaksi teemme robotille koulutusohjeet'''
