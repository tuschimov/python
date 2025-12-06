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
karakter = "🌹" # Char olayı Python 🐍 dilinde yoktur!

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
print(f"{pi} sayısının veri tipi: {piType}")