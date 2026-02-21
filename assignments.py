# Bir uzay oyununda roket
from typing import DefaultDict


for i in range(11, 0, -1):
    print(i)
print("Ateş")

karakter=["Jett", "Mario", "Ghost", "Trevor"]
for i in karakter:
    print(i)

# Bir oyunda sadece çift sayılara basarak ilerlenilebildiğini varsayalım. Birden yirmiye kadar olan çift sayıları ekrana yazdırlım.
for x in range(2, 21, 2):
    print(x)

# Gizli bir mesajı (örneğin: yusuf)  dikey olarak yazdırmamız gerekmekte.
isim="Yusuf"
for q in isim:
    print(q)

# Sınav not ortalaması.
sinavNotlari = [75, 80, 95, 60, 100]
sifir = 0
for w in sinavNotlari:
    sifir += w
print(sifir/len(sinavNotlari))

# Geçen veya kalan notlar.
sinavSonuclari = [45, 88, 32, 70, 95, 49]
for i in sinavSonuclari:
    if i >= 50:
        print("Geçen notlar:", i)

# 1'den 10'a kadar kazanılan puanlar için karesini hesaplayan bir program
for o in range(1, 11, 1):
    print(f"Seviye {o} - Kazanılan XP: {o**2}")

# Bir oyuncu listesinde "Faker" isimli bir oyuncuyu arıyoruz.
oyuncuListesi = ["Woot", "Omen", "Skay", "TenZ", "cNed", "Faker", "Alfajer"]
for u in oyuncuListesi:
    print("Kontrol ediliyor:", u)
    if u == "Faker":
        break
print("Faker bulundu. Aramaya gerek kalmadı.")

# Sohbetteki kelimeleri ekrana yazdırırken aradaki "spam" yazılı mesajları atlayayıp devam ettir (list.remove veya continue)
mesajlar = ["Selamlar", "Napıyon?", "spam", "Müsait misin", "He tmm", "Oyuna gel"]
for v in mesajlar:
    if v == "spam":
        continue
    print(f"Gönderdiğin mesaj:{v}")

# Kullanıcıdan istenilen bir kendini tanıtma metninde kaç tane 'a' harfi bulunduğunu yazdıralım!
tanitimMetni = input("Kendini tanıt!\n")
sayac = 0
for b in tanitimMetni:
    if b == "a" or b == "A":
        sayac += 1
        print(f"A harfi sayısı: {sayac}")
