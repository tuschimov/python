# Görev: Kullanıcıdan sayılar al ve aralarındaki tek sayıların toplamını al.
"""baslangic = int(input("İlk sayıyı giriniz: "))
bitis = int(input("Son sayıyı giriniz: "))
if baslangic % 2 == 0:
    baslangic = baslangic + 1
if bitis % 2 == 0:
    bitis = bitis - 1
toplam = 0
for j in range(baslangic, bitis, 2):
    toplam = toplam + j
print("Tek sayıların toplamı:", toplam)"""
# TODO: Tek - çift kontrolünü for döngüsünün içinde yap!

basSayi = int(input("İlk sayıyı giriniz: "))
sonSayi = int(input("Son sayıyı giriniz: "))
cevapSayi = 0
for i in range(basSayi, sonSayi, 2):
    if basSayi % 2 == 0:
        basSayi += 1
    elif sonSayi % 2 == 0:
        sonSayi -= 1
    cevapSayi += i
print("Tek sayıların sonucu:", cevapSayi,'!')