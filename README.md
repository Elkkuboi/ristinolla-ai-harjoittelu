## Projektin tavoitteet

- Harjoitella git-versionhallinnan käyttöä
- Toteuttaa ristinollan pelimoottori Pythonilla
- Kehittää AI-botti, joka oppii pelaamaan ristinollaa tallentamalla ja arvioimalla pelitilanteita

## Tiedostojen kuvaus

- **`peli.py`**: Sisältää pelin peruslogiikan (laudan luonti, siirtojen tekeminen, voiton tarkistus) sekä `robotti`-luokan, joka määrittelee botin toiminnan.
- **`treenaa.py`**: Skripti, jolla koulutetaan bottia laittamalla se pelaamaan itseään vastaan. Koulutuksen tulokset tallennetaan `arvot.json`-tiedostoon.
- **`pelaa.py`**: Skripti, jonka avulla voit pelata ihmisenä bottia vastaan.
- **`arvot.json`**: Automaattisesti generoitu tiedosto, joka sisältää botin arviot eri pelitilanteiden arvoista.

## Käyttöohjeet

1. Kloonaa projekti:
    ```bash
    git clone https://github.com/kayttaja/ristinolla-ai-harjoittelu.git
    ```
2. Siirry projektihakemistoon:
    ```bash
    cd ristinolla-ai-harjoittelu
    ```
3. Avaa projektin näkymä (jos käytät vscodea):
    ```bash
    code peli.py # jotta voit säätää oppimisnopeutta ja muuta (alkuun kannattaa olla suuremmat)
    code treenaa.py # Aja treenaamisfunktio omilla parametreilla
    code pelaa.py # jotta voit pelata bottia vastaan ! Keskeytä pelaaminen antamalla vuorollasi "10"
    ```

## Riippuvuudet

- Python 3.x

## Lisätietoja

Projektia kehitetään oppimismielessä. Kaikki palaute ja kehitysehdotukset ovat tervetulleita.