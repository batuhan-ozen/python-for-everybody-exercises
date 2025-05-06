import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# 1) Kullanıcıdan URL'yi al
url = input("Enter location: ")
print("Retrieving", url)

# 2) URL'den XML verisini indir
uh = urllib.request.urlopen(url)
data = uh.read()
print("Retrieved", len(data), "characters")

# 3) XML'i parse et
tree = ET.fromstring(data)

# 4) .//count ifadesiyle tüm <count> etiketlerini bul
counts = tree.findall('.//count')

# 5) Bulunan count etiketlerinin sayısı
print("Count:", len(counts))

# 6) Tüm <count> değerlerini toplayalım
total = 0
for item in counts:
    total += int(item.text)

print("Sum:", total)
50