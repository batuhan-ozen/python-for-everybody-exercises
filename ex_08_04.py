# Dosyayı aç ve satır satır oku
f = open("romeo.txt", "r")  # Dosya adı romeo.txt

# Benzersiz kelimeleri depolamak için boş bir liste oluşturuyoruz
unique_words = []

# Dosyadaki her satırı teker teker işliyoruz
for line in f:
    # Satırın sağındaki veya solundaki boşluk karakterlerini (örn. '\n') kaldırıyoruz
    line = line.rstrip()
    # Satırı boşluklardan ayırarak kelimeler listesine dönüştürüyoruz
    words = line.split()
    
    # Her bir kelime için kontrol yapıyoruz
    for word in words:
        # Eğer kelime henüz unique_words listesinde yoksa, ekliyoruz
        if word not in unique_words:
            unique_words.append(word)

# Tüm kelimeler eklendikten sonra, listeyi sıralıyoruz.
# Python'un sort() metodu büyük harfleri küçük harflerden önce sıralar, bu nedenle çıktı istenildiği gibi olacaktır.
unique_words.sort()

# Sonuç listesini ekrana yazdırıyoruz.
print(unique_words)
