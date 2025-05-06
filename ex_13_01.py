import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

# Kullanıcıdan URL alma
url = input("Enter - ")  

# URL'den HTML verisini çekme
html = urllib.request.urlopen(url).read()  

# BeautifulSoup ile HTML ayrıştırma
soup = BeautifulSoup(html, 'html.parser')

# Tüm <span> etiketlerini bul
tags = soup('span')

# Sayıları toplayan değişken
total = 0

# <span> etiketlerindeki sayıları topla
for tag in tags:
    total += int(tag.text)  # <span> içindeki metni al ve sayıya çevir

# Sonucu ekrana yazdır
print("Toplam:", total)
