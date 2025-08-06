# Tänne tulee koodi jolla pelataan bottia vastaan
from peli import robotti, luo_lauta, tulosta_lauta, tee_siirto, hae_mahdolliset_siirrot, tarkista_voitto, tarkista_tasapeli

botti = robotti()
botti.lataa_arvot()

# Pelataan peliä niin kauan kunnes koodin suorittaminen lopetetaan, ensin aloittaa pelaaja, sitten vuorotellen.

pelaaja_X = 1
pelaaja_O = -1

aloittaja = -1


while True:
    '''
    Alustetaan lauta, pelaajan aloitus, ja tulostetaan aloittaminen.
    Tätä silmukkaa jatkuu kunnes peli keskeytetään
    '''

    # Alustetaan arvo
    pelaaja_lopetti = False



    lauta = luo_lauta()
    aloittaja = -aloittaja
    vuoro = aloittaja


    aloittaja_nimi = "Pelaaja" if aloittaja == 1 else "Botti"
    print(f"Peli alkaa, nyt aloittaa {aloittaja_nimi}")
    tulosta_lauta(lauta)
    
    
    
    # Yhden pelin silmukka
    while True:
        '''
        Tämä on yhden pelin silmukka, aluksi tarkistetaan kenen vuoro on, sitten botti pelaa parhaan siirron, tai
        kysytään pelaajalta mitä hän haluaa pelata, tämän jälkeen (kun annettiin pelattava siirto) tulostetaan lauta,
        tarkistetaan voitto tai tasapeli ja vaihdetaan vuoro. Tätä jatketaan kunnes joku voittaa tai tulee tasapeli 
        '''

        # botin vuoro
        if vuoro == -1:
            print("robotti pelaa...")
            siirrot = hae_mahdolliset_siirrot(lauta)
            paras_siirto = botti.valitse_siirto(lauta, -1, siirrot)
            tee_siirto(lauta, paras_siirto, -1)
            print(f"Robotti pelasi {paras_siirto + 1}.")
            

            
        # pelaajan vuoro
        elif vuoro == 1:
            print("pelaajan vuoro")
            while True:
                try:
                    siirto = int(input("Anna siirto (1-9) tai 10: "))
                    if siirto == 10:
                        pelaaja_lopetti = True
                        break

                    siirto = siirto - 1
                    
                    if tee_siirto(lauta, siirto, 1):
                        break
                    else:
                        print("\n Ruutu on varattu tai virheellinen numero. Yritä uudelleen")
                except:
                    print("\n Virheellinen syöte")
            
        
        if pelaaja_lopetti:
            break

        # jokaisen siirron jälkeen (botti tai pelaaja)
        tulosta_lauta(lauta)
        voittaja = tarkista_voitto(lauta)
        if voittaja != 0:
                voittaja_nimi = "Pelaaja" if voittaja == 1 else "Botti"
                print(f"Peli päättyi {voittaja_nimi} voitti.")
                break
        elif tarkista_tasapeli(lauta):
            print("Tasapeli.")
            break

        vuoro = -vuoro

    if pelaaja_lopetti:
        print("Heippa")
        break




    