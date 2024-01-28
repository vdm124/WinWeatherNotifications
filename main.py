from win11toast import toast
import requests
from bs4 import BeautifulSoup


url = 'https://pogoda.mail.ru/prognoz/krasnoyarsk/'
response = requests.get(url)
bso = BeautifulSoup(response.text, "lxml")

temp = bso.find('div', class_="information__content__temperature")
weatherInfo = temp.text
weatherCityParse = bso.find("h1", class_="information__header__left__place__city")
weatherInfo = temp.text
weatherCity = weatherCityParse.text
print(weatherCity, weatherInfo, end="")

toast(weatherCity, weatherInfo)

