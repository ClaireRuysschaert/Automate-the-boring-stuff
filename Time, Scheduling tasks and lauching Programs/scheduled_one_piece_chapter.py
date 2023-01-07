# python
# This program checks once a day if there is a new chapter
# of one piece in japcan website
# If there is an update since the next visit, this program
# creates a shortcut of the new chapter on the desktop

import os
import time
from pathlib import Path

import bs4
import requests
import schedule
import winshell

THIS_FILE = Path(__file__).parent / "last_chapter_file.txt"


# Store the previous updated link to THIS_FILE
with open(THIS_FILE, "r") as f:
    previous_chapter_link = f.read()

url = "https://www.japscan.me/manga/one-piece/"


def get_the_new_link(url: str):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    # Parse to find the chapter number
    chapter_looking_elements: bs4.element.ResultSet = soup.find_all(
        attrs={"class": ["chapters_list", "text-truncate"]}
    )
    last_chapter_div: bs4.element.Tag = chapter_looking_elements[3]
    last_chapter_a_tag: bs4.element.Tag = last_chapter_div.find("a")
    new_chapter_link: str = last_chapter_a_tag.attrs.get("href")

    # Save the new link in the text file
    if previous_chapter_link != new_chapter_link:
        with open(THIS_FILE, "w") as f:
            f.write(new_chapter_link)
        print("the link has changed!")

    # The final link
    the_most_recent_link = url + new_chapter_link
    return the_most_recent_link


the_most_recent_link = get_the_new_link(url)

# Create the shortcut of the last chapter on the desktop
desktop = winshell.desktop()
path = os.path.join(desktop, "new_chapter_one_piece.url")

with open(path, "w") as shortcut:
    shortcut.write("[InternetShortcut]\n")
    shortcut.write(f"URL={the_most_recent_link}")

schedule.every().day.do(get_the_new_link, url)
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
