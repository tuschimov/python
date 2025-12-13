operator = str(input("İşlem giriniz (+ - * /)\n"))
number1 = float(input("İlk sayıyı giriniz: "))
number2 = float(input("İkinci sayıyı giriniz: "))
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("Şu dört işlemden birini gir:(+ - / *)")
    operator = str(input("İşlem giriniz (+ - * /)\n")) 