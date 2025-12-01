from bs4 import BeautifulSoup
import requests
import os

url = "https://www.google.com/finance/quote/TSLA:NASDAQ?window=MAX"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

classes = set()

for tag in soup.find_all(class_=True):
    for c in tag.get("class"):
        classes.add(c)

#print(classes)

#elements = soup.find_all(class_= "ds:5")
#for el in elements:
    print(el.attrs)

#os.remove("teslaFile.txt")
#with open("teslaFile.txt", "w") as f:
#    f.write(str(elements))

#os.remove("teslaFile.txt")
#with open("classes.txt", "w") as f:
#    f.write(str(classes))