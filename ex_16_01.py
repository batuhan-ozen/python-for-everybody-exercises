import urllib.request, urllib.parse, urllib.error
import json

# 1) Kullanıcıdan URL'yi al
url = input("Enter location: ")
print("Retrieving", url)

# 2) URL'den JSON verisini indir
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

# 3) JSON verisini parse et
info = json.loads(data)

# 4) 'comments' listesindeki tüm nesneleri alın
comments_list = info["comments"]

# 5) Listenin uzunluğu (toplam yorum sayısı)
print("Count:", len(comments_list))

# 6) 'count' değerlerini toplayın
total = 0
for item in comments_list:
    total += int(item["count"])

print("Sum:", total)
