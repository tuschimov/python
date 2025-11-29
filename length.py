print(len(input("Bana ismini ver, sana kaç harf olduğunu söyleyeyim\n"))) # 1. Yol olarak bu kullanılabilir.

uzunlukDeger = len(input("Bana ismini ver, sana kaç harf olduğunu söyleyeyim\n"))
print(uzunlukDeger)
if uzunlukDeger < 2:
    print("İsmin çok kısa olamaz lan, yalancı!")
if uzunlukDeger >= 25:
    print("Kanka, biraz kısaymış ismin, uzatsana")
else:
    print("Helal lan, adamakıllı bir ismin var he") # 2. yol olarak bu kullanılabilir.
