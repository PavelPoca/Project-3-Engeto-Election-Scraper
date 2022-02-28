from csv import writer
import requests
from bs4 import BeautifulSoup
import sys

def main(url: str, soubor):
    print(f"Začínám zpracovávat data obcí pro {okres(url)}")
    soup = zpracovat_url(url)
    make_csv(soup, soubor, url)
    print(f"Data zpracována. Soubor uložen jako: '{soubor}.csv'")

def make_csv(soup, soubor, url):
    tabulka = soup.find_all('tr')
    with open(soubor+".csv", "w", encoding='utf-8', newline="") as f:
        thewriter = writer(f)
        zahlavi = header(url)
        thewriter.writerow(zahlavi)
        for i in tabulka:
            try:
                pomocna = i.find('td', class_='cislo')
                cislo = pomocna.find('a').string
                url_obce = pomocna.find('a', href=True)
                data_url_obce = "https://volby.cz/pls/ps2017nss/"+url_obce['href']
                obec = i.find('td', class_='overflow_name').string
                soup_2 = zpracovat_url(data_url_obce)
                tds_1 = soup_2.find_all('td', class_='cislo')
                volici = tds_1[3].string
                vydane_obalky = tds_1[4].string
                platne_hlasy = tds_1[7].string
                data = [cislo, obec, volici, vydane_obalky, platne_hlasy]
                table_2 = soup_2.find_all('table', class_='table')
                tds_2 = table_2[1].find_all('td', attrs={'class': ['cislo'], 'headers': ['t1sa2 t1sb3']})
                for td in tds_2:
                    hlasy = td.string
                    data.append(hlasy)
                tds_3 = table_2[2].find_all('td', attrs={'class': ['cislo'], 'headers': ['t2sa2 t2sb3']})
                for td in tds_3:
                    hlasy = td.string
                    data.append(hlasy)
                thewriter.writerow(data)
            except AttributeError:
                continue


def header(url):
    soup = zpracovat_url(url)
    obec = soup.find('td', attrs= {'class': 'cislo', 'headers': 't1sa1 t1sb1'}).a
    url_obce = "https://volby.cz/pls/ps2017nss/"+obec['href']
    soup_2 = zpracovat_url(url_obce)
    strany = soup_2.find_all('tr')
    zahlavi = ["Kód obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"]
    for i in strany:
        try:
            strana = i.find('td', class_='overflow_name').string
            zahlavi.append(strana)
        except AttributeError:
            continue
    return list(zahlavi)

def okres(url):
    soup = zpracovat_url(url)
    div = soup.find('div', id='publikace', class_='topline').find_all('h3')
    nazev_okresu = div[1].string
    return nazev_okresu

def zpracovat_url(url):
    odpoved = requests.get(url)
    return BeautifulSoup(odpoved.text, "html.parser")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])