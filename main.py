from bs4 import BeautifulSoup
import requests


def get_group_place_webpage(url):
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


def find_buttons(url):
    page = requests.get(url)

    soupl = BeautifulSoup(page.content, "html.parser")
    buttons = soupl.find("div", class_="form-block form-space text-center")
    return buttons.text.replace("\n", "").replace(" ", "")

def find_table(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find("table", class_="table table-hover")
    if table:
        if len(table.text) > 40:
            # Jest
            return "Jest tabelka"
    return ""

if __name__ == "__main__":
    url = "https://kursant.nolimits.net.pl/activity/view?id=f8467607d800b994"
    # content  = get_group_place_webpage(url)
    guziki = find_buttons(url)
    tabela = find_table(url)
    if len(guziki) == 0 and len(tabela) == 0:
        raise ValueError("Nic nie znaleziono")
    else:
        for instance in [guziki, tabela]:
            print(instance)