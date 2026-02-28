# Belirtilen bir koşul doğru olduğu sürece çalışmaya devam eder.
# Koşul yanlış olduğunda döngü sona erer.
# Kullanımı:
# while koşul:
#       Koşul doğru olduğu sürece çalışacak kodlar

# While döngüsünün döngü sayısı belli değilse veya koşula bağlı tekrar eden işlemler için kullanılır.
# For döngüsü, genelde belirli bir sayıda işlem tekrar ettiğinde kullanılır. Bir liste veya range() ile kullanılır.
toplam = 0

for x in range (0,10):
    toplam += x
print(toplam)

sayi=0
toplam=0
while sayi < 10:
    toplam += sayi
    sayi += 1
print(toplam)

while True:
        istenenSayi = int(input("Lütfen bir sayı giriniz (Programdan çıkmak için -1 giriniz):\n"))
        if istenenSayi == -1:
             print("Programdan çıkılıyor...")
             break
        print(istenenSayi**2)

while True:
    kullanici = "Yusuf"
    dogruSifre = "123456"
    sifre = str(input("Merhabalar, " + kullanici + "şifrenizi giriniz:\n"))
    if sifre == dogruSifre:
        print("Giriş başarılı, yönlendiriliyorsunuz...")
        break
    print("Şifreniz hatalı, tekrar deneyiniz:\n")

toplam = 0
while True:
    sayi = int(input("Sayı giriniz (Bitirdiğiniz zaman 0 yazınız): "))
    toplam += sayi
    if sayi == 0:
        print(f"Sayıların toplamı:{toplam}")
        break

alisverisSepeti = []
while True:
    urun = str(input("Listeye hangi ürün eklensin? (Listeyi görmek için bitti yazınız.)\n"))
    if urun == "bitti":
        print("Alışveriş listeniz hazır", alisverisSepeti)
        break
    alisverisSepeti.append(urun)
    print("Ürün listeye eklendi!")

while True:
    yas = str(input("Yaşınızı giriniz: "))
    if yas == "" or "-":
        print("Yaşınız hatalı, tekrardan yazınız.")
    print(f"Teşekkürler! Yaşınız {yas} olarak kaydedildi!")

kullaniciAdi = "tuschimov"
while True:
    print("---Ana Menü---")
    print("[1] Merhaba De!\n[2] Havadan sudan konuş.\n[3] Çıkış yap.\n")
    tercih = int(input("Birini seçiniz(1,2,3): "))
    if tercih == 1:
        print(f"Merhabalar, {kullaniciAdi}!")
    elif tercih == 2:
        print("Bugün hava biraz soğuk, değil mi?")
    elif tercih == 3:
        break
    else:
        print("1, 2 ve 3 arasından seçim yapınız...")

while True:
    print("---Hesap Makinesi---")
    print("[1] Toplama\n[2] Çıkarma\n[3] Çarpma\n[4] Bölme\n[5] Çıkış")
    islem = str(input("Birini seçiniz: "))
    ilkSayi = int(input("İlk sayıyı giriniz: "))
    ikinciSayi = int(input("İkinci sayıyı giriniz: "))
    if islem == "5":
        break
    elif islem == "1":
        print(ilkSayi+ikinciSayi)
    elif islem == "2":
        print(abs(ilkSayi - ikinciSayi))
    elif islem == "3":
        print(ilkSayi * ikinciSayi)
    elif islem == "4":
        print(ilkSayi/ikinciSayi)
    else:
        print("Ne yazdın lan?")