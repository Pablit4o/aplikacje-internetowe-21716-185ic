from bs4 import BeautifulSoup
import json
import requests

source = requests.get('https://jsonplaceholder.typicode.com/users/1')

json_text = source.json()
print("url = ", source.url)
print("json_text = ", json.dumps(json_text, indent=4, separators=(". ", " = ")))
