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



from peli import robotti, luo_lauta, hae_mahdolliset_siirrot, tee_siirto, tarkista_voitto, tarkista_tasapeli, tulosta_lauta
import time

def kouluta_bottia(pelien_maara, nayta_laudat = False, n = 0):
    '''
    kouluttaa bottia pelaamaan itseään vastaan anettu määrä pelejä
    Mikäli haluat nähdä kun laudat vilisee, valitse näytä_laudat = True
    '''

    # Luodaan botti-olio. Tämä botti pelaa sekä X:sää että O:ta.
    botti = robotti()
    botti.lataa_arvot() # Ladataan aiempi koulutus

    pelaaja_X = 1
    pelaaja_O = -1

    print(f"Aloitetaan kouluttaminen, pelataan {pelien_maara} peliä...")
    alkuaika = time.time()
    
    ''' Pääsilmukka koulutusfunktiolle'''

    for peli_nro in range(1, pelien_maara + 1):


        '''pelin alustus'''

        lauta = luo_lauta()
        nykyinen_pelaaja = pelaaja_X

        # sanakirja johon tallennetaan viimeisin tila, jotta voimme päivittää arvoja emmekä unohda mikä tilanne oli
        edellinen_tila = {} # Avaimena toimii 1 tai -1
        
        # tulostetaan tyhjä lauta jos ominaisuus on päällä
        if nayta_laudat:
            tulosta_lauta(lauta)
            time.sleep(n)

        '''pelisilmukka'''
        while True:
            # Muodostetaan tila-tuple, jota käytetään avaimena arvot kirjassa
            tila_tuple = (tuple(lauta), nykyinen_pelaaja)

            # Tallennetaan tila
            edellinen_tila[nykyinen_pelaaja] = tila_tuple

            # Haetaan mahdolliset siirrot
            mahdolliset_siirrot = hae_mahdolliset_siirrot(lauta)

            # Valitaan siirto (HUOM SATUNNAISUUS ON MUKANA VALITSE SIIRTO FUNKTIOSSA)
            siirto = botti.valitse_siirto(lauta, nykyinen_pelaaja, mahdolliset_siirrot)

            # Tehdään siirto
            # huom, lauta muuttuu kun tämä ajetaan
            tee_siirto(lauta, siirto, nykyinen_pelaaja)
            
            # tulostetaan lauta jos ominaisuus on päällä
            if nayta_laudat:
                tulosta_lauta(lauta)
                time.sleep(n)
            
            # Oppimisvaihe kesken pelin
            vastustaja = -nykyinen_pelaaja
            if vastustaja in edellinen_tila: # tarkistaa onko vastustaja vielä pelannut mitään
                botti.paivita_arvot(edellinen_tila[vastustaja], tila_tuple)
                '''
                Päivitämme siis vastustajan tilan ennen heidän siirtoa ja verrataan sitä heidän siirron jälkeiseen
                '''

            # Tarkistetaan loppuiko peli?
            voittaja = tarkista_voitto(lauta)
            haviaja = -voittaja
            if voittaja != 0:
                # Annetaan palkinto voittajalle ja piiskataan häviäjää
                botti.paivita_arvot(edellinen_tila[voittaja], None, palkinto = 1)
                botti.paivita_arvot(edellinen_tila[haviaja], None, palkinto = 0)
                # poistutaan pelisilmukasta
                break

            # Tarkistetaan, onko peli tasapeli
            elif tarkista_tasapeli(lauta):
                # annetaan molemmille arvo 0.5
                botti.paivita_arvot(edellinen_tila[nykyinen_pelaaja], None, palkinto=0.5)
                botti.paivita_arvot(edellinen_tila[vastustaja], None, palkinto=0.5)
                break
            # Jos peli ei loppunut, vaihdetaan vuoroa
            nykyinen_pelaaja = vastustaja
        
        # Tulostetaan edistymistä
        if peli_nro % 1000 == 0:
            print(f"pelattu {peli_nro}/{pelien_maara} peliä...")
    
    # kun pelit pelattu niin tallenetaan
    botti.tallenna_arvot()
    loppuaika = time.time()

    print("\n Koulutus valmis!")
    print(f"Opitut arvot on tallennettu tiedostoon 'arvot.json'.")
    print(f"Koulutukseen kului aikaa: {loppuaika - alkuaika:.2f} sekuntia.")


kouluta_bottia(100, True, 0.01)
