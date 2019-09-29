import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.fr/dp/B07PHPXHQS/ref=gw_fr_desk_h1_aucc_cr_frd_34_0919?pf_rd_p=aa9a3be0-3e2d-49a7-9ef0-bb101c68d13c&pf_rd_r=8XABGGS832V0Z77BV621"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

title = soup.find(id="productTitle").get_text().strip()
price = soup.find(id="priceblock_dealprice").get_text().strip()
price = float(price[0:5])

print(title, price)
