from bs4 import BeautifulSoup

with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

for search in soup.find_all('book'):
    print("Tytuł: ", search.title.text)
    print("Autor: ",search.author.text)
    print("Rok wydania: ",search.year.text)
    print()