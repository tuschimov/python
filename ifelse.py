# Kullanıcıdan vücut ısı verisini ondalıklı (float) olarak iste.
vucutIsi = float(input("Lütfen vücut ısınızı giriniz\n"))
if vucutIsi > 37:
    print("Yüksek ateş! Doktora görün.")
    print("Dikkatli olun!")
else:
    print("Normal ateş, iyisin he.")
    print("Sağlıklı günler!")

sayi = float(input("Bir sayı gir:\n"))
if sayi > 0:
    print("Sayınız pozitif!")
elif sayi < 0:
    print("Sayınız negatif")
else:
    print("Sayı 0")
print("Sayı nötrdür.")
