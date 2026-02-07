# For döngüsü: Bir veri yapısının (liste, dictionary, tuple) veya belirli sayı arakığının üzerinde sıralı olarak gezinmeye yardım eden veri yapısıdır.
# Tekrarlı görevleri otomatikleştirmede kullanılır.
"""
Kullanım formatı şu şekildedir.
for degisken in koleksiyon:
    # Döngü içinde yapılacak işlemler...
"""
meyveler = ["elma", "armut", "muz", "kayısı", "çilek", "limon", "kavun", "karpuz", "ananas", "mango", "hindistan cevizi"]
print(meyveler[0])
print(meyveler[1])
print(meyveler[2])
print(meyveler[3])
print(meyveler[4])
print(meyveler[5])
print(meyveler[6])
print(meyveler[7]) # Şu an yine de yazılabilse de bu veri aşırı yüksek değerlere çıktığında, yazılamaz.
for meyve in meyveler:
    print("En sevdiğim meyvelerden,", meyve)
# range() fonksiyonu, bazı özel kurallar belirlememize yardımcı olur.
"""
range(stop): range(10) = 0,1,2,3,4,5,6,7,8,9
range(start, stop): range(2, 5) = 2,3,4
range(start, stop, step): range(2, 10, 2) = 2,4,6,8
"""
for sayi in range(0, 50, 5):
    print(sayi)