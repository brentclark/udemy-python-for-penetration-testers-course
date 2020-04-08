import requests

from bs4 import BeautifulSoup
import pprint
pp = pprint.PrettyPrinter()

page = requests.get('https://www.sharenet.co.za/v3/quickshare.php?scode=MSM')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.find_all('td'))
#    print(link.get('href'))
print(soup.prettify())
#print(soup.title)
#pp.pprint(page.text)
#soup = BeautifulSoup()