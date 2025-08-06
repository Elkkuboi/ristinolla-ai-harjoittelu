'''Täällä bottia opetetaan pelaamaan, botti tallentaa oppimansa sanakirjana JSON tiedostoon'''
'''
Pistetään botti pelaamaan itseään vastaan, haetaan robotti luokka ja luodaan olio X:lle ja O:lle
tehdään suuri for looppi, jossa pelataan anettu määrä pelejä
haetaan tiedot (arvot.json)

jokainen peli kulkee näin while loopin sisällä:
tyhjä pelikenttä
valitaan siirto
pelataan siirto
annetaan palautetta
tarkistetaan päättyikö peli, jos päättyi anna palautetta
vaihda vuoroa

kun pelit on pelattu, niin tallennetaan tulokset
ilmoitus
'''



from peli import robotti, luo_lauta, hae_mahdolliset_siirrot, tee_siirto, tarkista_voitto, tarkista_tasapeli

def kouluta_bottia(pelien_maara = 10):
    '''kouluttaa bottia pelaamaan itseään vastaan anettu määrä pelejä'''

    # Luodaan botti-olio. Tämä botti pelaa sekä X:sää että O:ta.
    botti = robotti()
    botti.lataa_arvot() # Ladataan aiempi koulutus

    pelaaja_X = 1
    pelaaja_O = -1

    print(f"Aloitetaan kouluttaminen, pelataan {pelien_maara} peliä...")

    
    ''' Pääsilmukka koulutusfunktiolle'''
