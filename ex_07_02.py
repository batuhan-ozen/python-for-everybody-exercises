# Kullanıcıdan dosya adını al
dosya_adi = input("Dosya adını girin: ")

# Toplam değer ve sayacı başlat
toplam = 0
sayac = 0

# Dosyayı aç ve satır satır oku
with open(dosya_adi, 'r') as dosya:
    for satir in dosya:
        if satir.startswith("X-DSPAM-Confidence:"):
            # Sayısal değeri çıkar
            deger = float(satir.split()[-1])
            toplam += deger
            sayac += 1

# Ortalamayı hesapla ve yazdır
ortalama = toplam / sayac
print(f"Average spam confidence: {ortalama}")