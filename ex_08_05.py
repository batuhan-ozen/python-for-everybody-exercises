# Dosyayı açıyoruz (dosyanın ismi mbox-short.txt)
f = open("mbox-short.txt", "r")

# "From " ile başlayan satırların sayısını tutmak için bir sayaç oluşturuyoruz.
count = 0

# Dosyadaki her bir satırı sırayla okuyarak işliyoruz.
for line in f:
    # Satır sonundaki boşluk ve yeni satır karakterlerini temizliyoruz.
    line = line.rstrip()
    
    # Eğer satır "From " ile başlamıyorsa, o satırı atlıyoruz.
    if not line.startswith("From "):
        continue
    
    # Satırı boşluk karakterlerinden bölerek kelimeler listesine dönüştürüyoruz.
    words = line.split()
    
    # Elde edilen kelimeler listesinin 2. elemanı (index 1) e-posta adresidir.
    print(words[1])
    
    # "From " ile başlayan bir satır bulduğumuz için sayaç değerini artırıyoruz.
    count += 1

# Döngü tamamlandıktan sonra, toplam "From " satırı sayısını ekrana yazdırıyoruz.
print("There were", count, "lines in the file with From as the first word")
