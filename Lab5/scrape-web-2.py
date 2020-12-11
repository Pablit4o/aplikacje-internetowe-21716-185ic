from bs4 import BeautifulSoup
import requests

source = requests.get('http://tibia.pl/exp-table').text

soup = BeautifulSoup(source, 'html5lib')

for search in soup.find_all('tr'):
    info = search.text.split()
    lvl = info[0]
    exp = info[1]
    if lvl.isnumeric() and exp.isnumeric():
        print("Poziom: ",lvl,", Doświadczenie: ", exp)