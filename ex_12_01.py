import socket

# Bağlantı ayarları
host = "data.pr4e.org"  # URL'nin domain kısmı
port = 80               # HTTP standart portu
path = "/intro-short.txt"  # İstenen dosyanın yolu

try:
    # Soket oluştur ve bağlan
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    # HTTP GET isteği hazırla
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    sock.send(request.encode())

    # Yanıtı al
    response = b""
    while True:
        data = sock.recv(4096)
        if not data:
            break
        response += data

    sock.close()

    # Başlıkları ve gövdeyi ayır
    headers, _, body = response.partition(b"\r\n\r\n")
    headers = headers.decode()

    # Başlıkları yazdır
    print("HTTP Yanıt Başlıkları:")
    print(headers)

    # İstenen başlıkları bul
    header_lines = headers.split("\r\n")
    target_headers = {
        "Last-Modified": "",
        "ETag": "",
        "Content-Length": "",
        "Cache-Control": "",
        "Content-Type": ""
    }

    for line in header_lines:
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key in target_headers:
                target_headers[key] = value

    # Sonuçları göster
    print("\nİstenen Başlıklar:")
    for key, value in target_headers.items():
        print(f"{key}: {value}")

except socket.gaierror as e:
    print(f"Hata: Host adresi çözümlenemedi. Lütfen internet bağlantınızı ve host adresini kontrol edin. Hata detayı: {e}")
except Exception as e:
    print(f"Beklenmeyen bir hata oluştu: {e}")