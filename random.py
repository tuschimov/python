import random as rd
uretim = rd.randint(2,100)
print(uretim)
isimler=["Ali", "Atilla", "Yalın", "Tuna", "Tahsin"]
rd.shuffle(isimler)
print(isimler)

isimler = ["Ali", "Ece", "Kaan", "Mete", "Batu", "Veli" "Ayse"]

numara = [910, 147, 458, 163, 1979, 505, 894]
enKucukNum = min(numara)
enYuksekNum = max(numara)
indYuksek = numara.index(enYuksekNum)
inDus = numara.index(enKucukNum)