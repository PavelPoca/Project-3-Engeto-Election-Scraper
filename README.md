# Project-3-Engeto-Election-Scraper

Třetí projekt 'Election Scraper' pro Engeto python akademii.

## Popis projektu

Tento projekt slouží k extrahování dat z parlametních voleb 2017. Odkaz k prohlédnutí [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Instalace knihoven

Knihovny použité v kódu jsou uloženy v `requirements.txt`. Pro instalaci knihoven doporučuji si vytvořit nové virtuální prostředí a pomocí manžeru 'pip3' spustit následovně:
```
pip3 --version`                      # oveřím verzi manažeru
pip3 install -r requirements.txt     # nainstaluju knihovny z requirements.txt
```
## Spuštění skriptu

Spouštění souboru `main.py` pomocí příkazového řádku.
Ke spuštění jsou povinné dva argumenty a to následovně.

`python main.py <odkaz_územního_celku> <název_výsledného_souboru>`

Následně se vám uloží výsledky do zadaného souboru s příponou `.csv`.

## Ukázka projektu

Výsledky pro okres Brno-venkov:

1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203
2. argument: vysledky_brno_venkov

Spuštění programu:

`python main.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203' 'vysledky_brno_venkov'`

Průběh programu:
```
Začínám zpracovávat data obcí pro
Okres: Brno-venkov

Data zpracována. Soubor uložen jako: 'vysledky_brno_venkov.csv'
```
Výstup v csv souboru:
```
Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně 
582794,Babice nad Svitavou,925,660,655,109,1,2,43,0,53,31,7,3,10,0,0,93,0,39,129,0,3,69,0,2,1,1,58,1,0
582808,Babice u Rosic,553,353,351,32,0,0,18,1,27,30,5,1,6,0,2,37,0,13,93,0,1,25,5,4,1,1,49,0,0
581321,Běleč,160,131,130,13,0,0,25,0,8,14,0,1,0,0,0,11,1,1,30,0,0,14,0,0,0,0,12,0,0
582824,Bílovice nad Svitavou,2 676,2 018,2 004,316,0,2,103,0,257,78,28,6,44,2,0,205,2,147,432,2,6,186,0,16,0,1,170,1,0
582832,Biskoupky,145,86,85,6,0,0,11,0,1,17,1,0,1,0,0,5,0,7,22,0,0,4,0,0,0,2,7,1,0
582841,Blažovice,924,725,724,64,0,0,54,0,49,44,12,2,7,3,1,53,1,34,133,0,1,193,1,2,0,0,70,0,0
582859,Blučina,1 749,1 099,1 091,126,2,0,62,2,42,52,15,11,20,0,1,108,0,23,326,5,1,100,1,8,7,2,174,2,1
595314,Borač,289,219,218,24,0,0,21,0,18,15,6,0,0,0,0,16,0,13,52,0,0,21,0,0,0,0,30,2,0
595331,Borovník,81,61,61,4,0,0,5,0,4,0,1,0,2,0,0,4,0,2,23,0,0,16,0,0,0,0,0,0,0
582875,Braníškov,147,96,96,17,0,0,4,0,11,5,1,0,2,1,0,4,0,2,21,0,0,11,0,0,0,0,17,0,0
593834,Branišovice,482,302,301,23,0,0,15,0,4,18,2,0,5,0,0,19,0,69,104,1,1,19,0,0,1,0,20,0,0
...
```
