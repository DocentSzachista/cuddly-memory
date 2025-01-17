from bs4 import BeautifulSoup
import requests


def scrap_webpage(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find(id="w0")
    dates = table.find_all("tr")

    to_return = []

    for date in dates:
        termin = date.find("td", class_="col-main")
        wolne_miejsca = date.find("td", class_="col-free-places")
        if termin == None or wolne_miejsca == None:
            continue
        data = termin.text.split("/")
        places = [ int(x) for x in wolne_miejsca.text.split("/")]


        if places[0] != 0 or places[1] != 0 :
            info = f" {data[0]} Wolne miejsca Kobiety: {places[0]}, Faceci: {places[1]}"
            to_return.append(info)
        else:
            continue
    return to_return

if __name__ == "__main__":
    url = "https://kursant.nolimits.net.pl/activity/view?id=f8467607c9a12f11"
    content  = scrap_webpage(url)
    if len(content) == 0:
        raise ValueError("Nic nie znaleziono")
    else:
        for instance in content:
            print(instance)