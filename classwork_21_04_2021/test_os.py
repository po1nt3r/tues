import os
import requests
from bs4 import BeautifulSoup

folder_source = requests.get("https://github.com/AlekoGeorgiev/tues").text
link = "https://github.com/AlekoGeorgiev/tues/tree/main/"
soup = BeautifulSoup(folder_source, "html.parser")
folders = []

os.mkdir("github_repo")

def get_folders(link, soup):
    div = soup.find('div', class_="Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item")
    j = 0
    extension = ['.py', '.md']
    for _ in range(len(soup.find_all("div", {"class": "Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item"}))):
        item = div.find('a', class_="js-navigation-open Link--primary").text
        if item[-3::] not in extension:
            folders.append(item)
            os.mkdir(f"github_repo/{folders[j]}")
            get_files(link, folders[j], extension=extension)
            j += 1
        else:
            get_files(link, item=item)
        div = div.find_next_sibling()
        
def get_files(link, folder=None, item=None, extension=None):
    if folder:
        file_link = link + folder
    elif item:
        file_link = link + item
    file_source = requests.get(file_link).text
    file_soup = BeautifulSoup(file_source, "html.parser")
    
    try:
        div = file_soup.find('div', class_ = "Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item")
        for _ in range(len(soup.find_all("div", {"class": "Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item"}))):
            if folder:
                filename = div.find('a', class_="js-navigation-open Link--primary").text 
                location = folder + "/" + filename
                if filename[-3::] not in extension:
                    continue
                file_link = "https://raw.githubusercontent.com/AlekoGeorgiev/tues/main/" + location
            elif item:
                location = item
                file_link = "https://raw.githubusercontent.com/AlekoGeorgiev/tues/main/" + item
            print(file_link)
            r = requests.get(file_link)
            with open(f"github_repo/{location}", "wb") as f:
                for i in r.iter_content(chunk_size=8192):
                    f.write(i)
            div = div.find_next_sibling()
    except AttributeError:
        pass

def check_link(file_link, r):
    check_soup = BeautifulSoup(r, "html.parser")
    if check_soup.find('pre'):
        return "folder"
        
get_folders(link, soup)