#Author : amazing.python

import requests
from bs4 import BeautifulSoup

#cityName = input("City name:")
#search = "weather in {cityName}"

search = "weather in istanbul"
url = f"https://www.google.com/search?q={search}"

r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")

update = s.find("div", class_="BNeawe").text
print(update)