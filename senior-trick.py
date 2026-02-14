# 1'den 10'a kadar tüm sayıları içeren bir program.
kareler = []
for s in range(1, 11):
    kareler.append(s**2)
print(kareler)

# List comprehension
# kareler = [x**2 for x in range (1, 11)], print(kareler)

ciftSayilar = [x for x in range(1,11) if x % 2 == 0]

programLang = ["html", "sql", "css", "python", "typescript"]
upperProgram = [x.upper( ) for x in programLang]
print(upperProgram)

# break() ve continue()
for i in range(1,101):
    if i == 5:
        break
    print(i)

for i in range(1,101):
    if i == 1:
        continue # Koşulun içindeki yer hariç devam eder.
    print(i)