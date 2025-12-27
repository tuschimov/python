print("Python'da ateş sıcaklığı ölçmek için basit bir utility.")
atesSicakligi = float(input("Ateşinizi giriniz:\n"))
if atesSicakligi <= 36.0:
    print("Düşük ateşin var, bir an önce acile gitmen önerilir")
elif atesSicakligi <= 37.2:
    print("Ateşin normal, yat kalk dua et.")
elif atesSicakligi <= 38.0:
    print("Garip, ateşin birazcık yüksek. Ama dert edilecek kadar değil.")
elif atesSicakligi <= 39.0:
    print("Ateşin var, bir doktora görünme vakti gelmiş gibi.")
elif atesSicakligi <= 40.0:
    print("Harbi ciddi ateşin var, 112'yi ara veya acile görün.")
else:
    print("Helak olacaksın. 🔥🔥🔥🔥🔥🔥🔥🔥")
print('Eyi günler!')