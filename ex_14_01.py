import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Kullanıcıdan gerekli bilgileri al
url = input("Enter URL: ")          # Başlangıç URL'sini giriniz
count = int(input("Enter count: ")) # Kaç kez link takip edilecek
position = int(input("Enter position: ")) # Her sayfadaki kaçıncı link takip edilecek

for i in range(count):
    # 1) HTML içeriğini indir
    html = urllib.request.urlopen(url).read()
    
    # 2) BeautifulSoup ile parse et
    soup = BeautifulSoup(html, 'html.parser')
    
    # 3) Tüm <a> etiketlerini (anchor) bul
    tags = soup('a')
    
    # 4) İlgili pozisyondaki linkin 'href' değerini al
    #    (Dikkat: listeler 0'dan başladığı için position-1)
    link = tags[position - 1].get('href', None)
    
    print("Retrieving:", link)
    
    # Sonraki döngüde kullanmak için url'yi güncelle
    url = link

# Döngü tamamlandıktan sonra en son linki yazdır
print("Last URL:", url)

# İsterseniz son linkin içindeki ismi (örneğin known_by_XXXX.html'deki XXXX) ayıklayabilirsiniz:
name = url.split('_')[-1].split('.')[0]
print("Son İsim:", name)
