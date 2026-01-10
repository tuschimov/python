# Listeler (List)
# Birden fazla veinin olduğu (sınav notları, kişiler ve benzeri) için teker teker değere atamak saçma olur (ogrenci1, ogrenci2, ogrenci3) gibi yazılması, özellikle veritabaları ve bayağı zor olur.
# Index (Dizin): sinav = [78, 90, 65] kısmında 3 veri vardır ama 0, 1 ve 2 olarak adlandırılır. Son değerimiz iki olmasına rağmen üç değerimiz vardır. Bir bina gibi zemin kattan başlamasına rağmen katları sayarken zemin kat ta bir kat olarak sayılır.
sinav1 = 50
sinav2 = 70
sinav3 = 85
# Yerine basitçe:
sinavNotlari = [80, 70, 85]
print(sinavNotlari) #denilebilir.

# Birden fazla veriyi aynı anda teker teker değiştirmeden rahatlıkla değiştirebiliriz
print(sinavNotlari[0])
sinavNotlari[1] = 90
print(sinavNotlari[2])
sinavNotlari[2] = 20
print(sinavNotlari[2])
print(type(sinavNotlari[1])) # List te boolean, string, integer gibi bir veri tipidir. Aramıza hoşgeldin list!

ogrenci = ["Yusuf", 16, "Konya", 70]
print(type(ogrenci[1]))

sehirler = ["Ankara", "Istanbul", "Izmir"]
print("Önceki durum", sehirler)
sehirler[1] = "Konya"
print("Yeni durum:", sehirler)
print(len(sehirler)) # 3, çünkü 3 değerimiz var
# Bazı yardımcı fonsiyonlarımız var:

# append(): Listenin **sonuna** veri ekler.
sehirler.append("Yozgat")
# insert(): İstediğimiz index'e ekleme yapar.
sehirler.insert(0, "Antalya")
# extend(): Listenin **sonuna** liste ekler.
sehirler.extend(["Adana", "Mersin"])
# remove(): Listede istenilen veriyi siler.
sehirler.remove("Konya")
# pop(): Özellikle belirtilmedikçe son veriyi siler.
gidenSehir = sehirler.pop()
print("Adaya veda eden şehir:", gidenSehir)
# index(): Bir verinin kaçıncı satırda buluduğunu belirtir.
print(sehirler.index("Izmir"))
# count(): Listede kaç değer olduğunu yazar.
print(sehirler.count)
# sort(): Listeyi A'dan Z'ye sıralar.
print(sehirler.sort)
# reverse(): Listeyi tersine çevirir.
print(sehirler.reverse)
print(sehirler)

isim = "Yusuf"
print("İsmin harf uzunluğu:", len(isim))
