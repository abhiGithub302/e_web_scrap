import requests
from bs4 import BeautifulSoup
url = 'https://www.flipkart.com/'
r = requests.get(url)
print(r.status_code)
# print(r.text)
soup = BeautifulSoup(r.text, "lxml")
# tag = soup.body.div
# print(tag)
# atb = (tag.attrs)
# # print(atb)
# print(atb["class"])
# print(soup.div.p.string)


# use of find function in web scraping
print(soup.find_all("body.div",{"class":"_30jeq3 _1_WHN1"}))


