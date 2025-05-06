# 1.
# s = 'Monty Python'
# print (s[0:4])
# print (s[6:7])
# print(s[6:20])
# print(s[:2])
# print(s[8:])
# print(s[:])


# 2.
# a = 'Hello'
# b = a + 'There'
# print(b)

# a = 'Hello'
# c = a + ' ' + 'There'
# print(c)


# 3.
# fruit = 'banana'
# print ('n' in fruit)

# fruit = 'banana'
# print ('m' in fruit)

# fruit = 'banana'
# if 'a' in fruit :
    # print('Found it!')
    

# 4. 
# greet = 'Hello Bob'
# zap = greet.lower()
# print(zap)

# print('Hi There'.lower())



# String İşlemleri - Büyük/Küçük Harf Kontrolü
# ---------------------------------------------
# capitalize(): İlk harfi büyük, diğerlerini küçük yapar. Örnek: "hello" → "Hello"
# lower(): Tüm harfleri küçültür. Örnek: "HELLO" → "hello"
# upper(): Tüm harfleri büyütür. Örnek: "hello" → "HELLO"

# String Temizleme ve Biçimlendirme
# ---------------------------------
# strip(): Baş ve sondaki boşlukları siler. Örnek: "  hello  " → "hello"
# lstrip(): Sadece baştaki karakterleri siler. Örnek: "##hello" → "hello"
# rstrip(): Sadece sondaki karakterleri siler. Örnek: "hello!!" → "hello"
# center(width, fillchar): Stringi ortalar. Örnek: "hi".center(5, "-") → "--hi--"

# Arama ve Değiştirme
# -------------------
# find(sub): Alt stringin indeksini bulur. Bulamazsa -1 döner. Örnek: "apple".find("p") → 1
# replace(old, new): Belirtilen kısmı değiştirir. Örnek: "Hello".replace("H", "J") → "Jello"

# Koşul Kontrolü
# --------------
# endswith(suffix): String belirtilen ifadeyle bitiyor mu kontrol eder. Örnek: "file.txt".endswith(".txt") → True
# startswith() = string belirtilen ifadeyle başlıyor mu kontrol eder

# Örnek Kullanım
# text = "  MerHaBa Dünya!  "
# temizlenmis = text.strip().lower()
# print(temizlenmis)  # Çıktı: "merhaba dünya!"

# 5.
# fruit = 'banana'
# pos = fruit.find('na')
# print(pos)

# aa = fruit.find('z')
# print(aa)


# greet = 'Hello Bob'
# nnn = greet.upper()
# print(nnn)

# www= greet.lower()
# print(www)


# greet = 'Hello Bob'
# nstr= greet.replace('Bob','Batuhan')
# print(nstr)

# nstr = greet.replace('o','X')
# print(nstr)

# greet = '  Hello Bob   '
# greet.lstrip()
# print(greet)

# greet.rstrip()
# print(greet)
 
# greet.strip()
# print(greet)


# line = 'Please have a nice day'
# print(line.startswith('Please'))

#print(line.startswith('p'))


# data = 'From stephen.marquard@uct.ac.za  Sat Jan  5 09:14:16  2025'
# atpos = data.find('@')
# print(atpos)

# sppos = data.find(' ',atpos)
# print(sppos)

# host = data[atpos+1 : sppos]
# print(host)

















































