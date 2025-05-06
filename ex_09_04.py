# mbox-short.txt dosyasını aç ve oku
dosya_adi = 'mbox-short.txt'  # Dosya adı
try:
    dosya = open(dosya_adi)  # Dosyayı aç
except FileNotFoundError:
    print(f"{dosya_adi} dosyası bulunamadı.")
    exit()

# Gönderenlerin e-posta adreslerini ve kaç kez gönderdiklerini tutacak bir sözlük oluştur
gonderici_sayilari = {}

# Dosyayı satır satır oku
for satir in dosya:
    # Satır 'From ' ile başlıyorsa (boşluk dahil)
    if satir.startswith('From '):
        # Satırı boşluklara göre böl ve ikinci kelimeyi (e-posta adresi) al
        kelimeler = satir.split()
        if len(kelimeler) > 1:  # Eğer satırda yeterli kelime varsa
            eposta = kelimeler[1]  # İkinci kelime e-posta adresi
            # Sözlükte bu e-posta adresi varsa sayısını 1 artır, yoksa 1 olarak ekle
            gonderici_sayilari[eposta] = gonderici_sayilari.get(eposta, 0) + 1

# Dosyayı kapat
dosya.close()

# En çok e-posta gönderen kişiyi bul
en_cok_gonderici = None
en_cok_sayi = None

# Sözlükteki her e-posta adresi ve sayısı için döngü
for eposta, sayi in gonderici_sayilari.items():
    # Eğer bu e-posta adresi daha öncekilerden daha fazla gönderdi ise
    if en_cok_sayi is None or sayi > en_cok_sayi:
        en_cok_gonderici = eposta
        en_cok_sayi = sayi

# Sonucu yazdır
if en_cok_gonderici is not None:
    print(f"{en_cok_gonderici} {en_cok_sayi}")
else:
    print("Dosyada 'From ' ile başlayan bir satır bulunamadı.")