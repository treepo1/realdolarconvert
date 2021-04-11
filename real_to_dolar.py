from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
url = "https://www.google.com/search?q=cotacao+do+dolar&oq=cotacao+do+dolar&aqs=chrome..69i57j0i131i433l4j69i60l3.2159j0j9&sourceid=chrome&ie=UTF-8"

site = requests.get(url, headers = headers)
soup_content = site.content

soup = BeautifulSoup(soup_content, 'html.parser')

search_cotation = soup.find('span',class_ ='DFlfde SwHCTb')

cotation = search_cotation.text

valornum = float(cotation.replace(",","."))

real = float(input("Digite o valor em reais"))
print(f'{real} real(is) corresponde(m) a {real/valornum:.3f} dólar(es).')


