# Aritmetik operaratörler
"""
+ ---> Toplar.
- ---> Çıkarır.
* ---> Çarpar.
/ ---> Böler.
% ---> Kalanı alır (mod)
** ---> Üs alır.
"""
# İşlem önceliği şu sekildedir:
"""
1) Parantez içi
2) Üs alma
3) Çarpma, Bölme, Tam Bölme, Mod Alma (Soldan sağa)
4) Toplama Çıkarma (Soldan sağa)
"""
sonuc = 7 + 3 * 2 ** 2 - (10 // 3) % 2
 # 7 + 3 * 2 ** 2 - 3 % 2
 # 7 + 12 - 3 % 2
 # 7 + 12 - 1
 # 18
print(f"Sonuç: {sonuc}")
sayi1 = 12
sayi2 = 3
sayi3 = 5
toplam = sayi1 + sayi2
toplam = toplam + sayi3
print(toplam)
toplam += sayi3 # toplam = toplam + sayi3
toplam -= sayi3 # toplam = toplam - sayi3
toplam *= sayi3 # toplam = toplam * sayi3
toplam /= sayi3 # toplam = toplam / sayi3

isim = input("Lütfen adınızı giriniz:\n")
metin = "Kişinin Adı :" + isim
print(type(metin))

num1 = float(input("Lütfen ilk sayıyı giriniz:\n"))
num2 = float(input("Lütfen ikinci sayıyı giriniz:\n"))
foo = num1 + num2
print("Toplam: ", foo)
