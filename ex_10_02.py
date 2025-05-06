# mbox-short.txt dosyasını aç ve oku
dosya_adi = 'mbox-short.txt'  # Dosya adı
try:
    dosya = open(dosya_adi)  # Dosyayı aç
except FileNotFoundError:
    print(f"{dosya_adi} dosyası bulunamadı.")
    exit()

# Saatleri ve kaç kez gönderildiklerini tutacak bir sözlük oluştur
saat_sayilari = {}

# Dosyayı satır satır oku
for satir in dosya:
    # Satır 'From ' ile başlıyorsa (boşluk dahil)
    if satir.startswith('From '):
        # Satırı boşluklara göre böl ve zaman bilgisini al
        kelimeler = satir.split()
        if len(kelimeler) > 5:  # Eğer satırda yeterli kelime varsa
            zaman = kelimeler[5]  # Zaman bilgisi (örnek: '09:14:16')
            # Zaman bilgisini ':' ile böl ve saat kısmını al
            saat = zaman.split(':')[0]
            # Sözlükte bu saat varsa sayısını 1 artır, yoksa 1 olarak ekle
            saat_sayilari[saat] = saat_sayilari.get(saat, 0) + 1

# Dosyayı kapat
dosya.close()

# Saatleri sıralı bir şekilde yazdır
for saat in sorted(saat_sayilari):
    print(f"{saat} {saat_sayilari[saat]}")