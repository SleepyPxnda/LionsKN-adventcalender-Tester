import requests
from bs4 import BeautifulSoup
import os

page_url = "https://lionskn-adventskalender.de/gewinnnummern/"


def main():
    page = requests.get(page_url)
    soup = BeautifulSoup(page.text, "html.parser")
    win_list = []

    win_table = soup.find("table")

    win_rows = win_table.findAll("tr")

    for index, row in enumerate(win_rows):
        entries = row.findAll("td")

        winner = entries[1].text
        sponsor = entries[2].text
        win = entries[3].text

        win_list.append({"winner": winner, "sponsor": sponsor, "win": win})

    win_list.pop(0)

    own_numbers = os.environ.get("NUMBERS").split(",")
    print("Registered Numbers: " + str(own_numbers))
    win_elements = []

    for element in win_list:
        if element["winner"] in own_numbers:
            win_elements.append(element)

    if len(win_elements) == 0:
        print("No Winners found ... Try again tommorrow ...")
    else:
        for win_element in win_elements:
            print(str("'" + win_element["winner"]) + "' won '" + str(win_element["win"]) + "' from '" + str(
                win_element["sponsor"] + "'"))


if __name__ == "__main__":
    main()
