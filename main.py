from bs4 import BeautifulSoup
import requests

def currency_input(in_cur , out_cur):
  url = f"https://www.x-rates.com/calculator/?from={in_cur}&to={out_cur}&amount=1"
  content = requests.get(url).text
  soup= BeautifulSoup(content , 'html.parser')
  currency = float(soup.find('span' , class_ = "ccOutputRslt").get_text()[:-4])

  #789e428cfd49454497cbea3b73bef84a
  
  return currency

currency_input('EUR','USD')