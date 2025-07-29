'''Täällä bottia opetetaan pelaamaan, botti tallentaa oppimansa sanakirjana JSON tiedostoon'''
'''
Pistetään botti pelaamaan itseään vastaan, haetaan robotti luokka ja luodaan olio X:lle ja O:lle
tehdään suuri while looppi, jossa pelataan anettu määrä pelejä
haetaan tiedot (arvot.json)

jokainen peli kulkee näin:
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

