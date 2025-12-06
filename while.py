print("Ehliyet alabilme yeteneğini ölçmek için basit bir Python programı ")
name = input("İsmini gir:\n")
age = input("Bir de yaşını gir reis:\n")
while name == "":
    print("İsim girmedin ki")
    input("İsmini gir (emir):\n")
else:
    print(f"Merhaba {name}!")
while age == "":
    print("Yaşını girmedin ki")
    input("Yaşını gir (emir):\n")
else:
    print(f"Merhaba {age} yaşındaki {name}!")
if age >= 18:
    print("Ehliyet alma hakkın var, git sınava gir!")
elif age >= 85:
    print("Çok yaşlısın be reis!")
else:
    print("Yaşın uygun değil, çık git!")