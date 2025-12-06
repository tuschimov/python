# String (str)-Metin Veri Tipi
isim = "Yusuf"
isimType = (type(isim)) # <class 'str'>
print(f"{isim} isminin veri tipi: {isimType}")
# Class, var olan sınıflardan biridir.

ad = "Yusuf"
soyad = "Bitgi"
tam_ad = ad + " " + soyad
ikili = tam_ad * 2
print(ikili) # String çoğaltma işi
karakter = "🌹" # Char olayı Python dilinde yoktur!

# Integer (int)-Tam Sayı Veri Tipi
yas = +15 # Eksi ve artı işaretleri kullanılabilir.
yas2 = "15"
para = 123_456_789 # Sayılarda alt çizgi kullanılabilir, okunulabilirlii arttırır.
yasType = (type(yas)) # <class 'int'>
yas2Type = (type(yas2)) # <class 'str'>
print(f"{yas} yaşının veri tipi: {yasType}")
print(f"{yas2} yaşının veri tipi: {yas2Type}")

# Float (float)-Ondalıklı Sayı Veri Tipi
pi = 3.1416
piType = (type(pi)) # <class 'float'>
deger = 10.5
deger2 = 3.8
print(f"{pi} sayısının veri tipi: {piType}")
print(deger + deger2) # Float veri tipinde toplama işlemi yapılabilir.
# Float veri tipinde de artı ve eksi işaretleri kullanılabilir.

# Boolean (bool)-Mantıksal Veri Tipi
dogruMu = True
print(type(dogruMu)) # <class 'bool'>
print(10>5) # True
print(10>80) # False

# Pratik yapalım!
x = 10
print(f"x'in veri tipi: {type(x)}") # <class 'int'>
x = "Meeerhaba"
print(f"x'in veri tipi: {type(x)}") # <class 'str'>

a = 5
b = "5"
c = 5.0
print(type(a)) # <class 'int'>
print(type(b)) # <class 'str'>
print(type(c)) # <class 'float'>


d = 50
e = "5"
print(d + int(e)) # int() fonksiyonu string ifadeyi integer'a çevirir.

f = 20
g = "60"
print(f + int(g)) # int() fonksiyonu string ifadeyi integer'a çevirir.
h = 10
i = 2.5
topl = h + i
print(f"Toplam: {topl}, Veri tipi: {type(topl)}") # <class 'float'>

j = "250"
k = int(j)
print(k + 150)