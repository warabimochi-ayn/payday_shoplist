import requests
from bs4 import BeautifulSoup

url="https://paypay.ne.jp/shop/"
res=requests.get(url)
bs=BeautifulSoup(res.text, "html.parser")
#print(bs)
shoplist=[]
#shop_name_list=bs.select("span.storeList__caption")
shop_name_list=bs.select("span.storeList__caption")
#print(shop_name_list[0])
for shop_name in shop_name_list:
    name_tags=shop_name.contents
    name_tag=name_tags[0]
    shoplist.append(name_tag)

for shop in shoplist:
    print(shop)