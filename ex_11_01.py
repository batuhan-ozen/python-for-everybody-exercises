import re
import requests

# Dosyayı URL'den oku
url = 'http://py4e-data.dr-chuck.net/regex_sum_2140849.txt'
response = requests.get(url)
text = response.text

# Tüm tam sayıları bul
numbers = re.findall(r'\d+', text)

# Sayıları integer'a dönüştür ve topla
total = sum(int(num) for num in numbers)

# Sonucu yazdır
print("Toplam:", total)