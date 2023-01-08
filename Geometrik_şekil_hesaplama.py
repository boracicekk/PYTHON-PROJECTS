"""Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
abs(-4)
4
abs(5)
5
"""
a=input("Üçgenin mi tipini bulmak istiyorsunuz Dörtgenin mi?")
if a=="Üçgen":
    kenar1 = int(input("1.kenarın değerini giriniz:\n"))
    kenar2 = int(input("2.kenarın değerini giriniz:\n"))
    kenar3 = int(input("3.kenarın değerini giriniz:\n"))
    kenar4 = int(input("4.kenarın değerini giriniz:\n"))
if kenar1==kenar2 and kenar2==kenar3:
    print("Üçgeniniz Eşkenar Üçgendir.")
elif kenar1==kenar2 or kenar1==kenar3 or kenar2==kenar3 :
    print("Üçgeniniz ikizkenar bir üçgendir.")
elif kenar1!=kenar2 and kenar1!=kenar3 and kenar2!=kenar3:
    print("Üçgeniniz Çeşitkenardır.")
else:
    print("Girdiğiniz kenarlar bir üçgen için uygun değildir.")
elif a=="Dörtgen":
if kenar1 == kenar3 and kenar2==kenar4:
        print("Şekliniz karedir.")
elif kenar1 == kenar3 or kenar2 == kenar4:
print("Şekliniz Dikdörtendir")
else:
print("Şekliniz Dörtgendir.")
else:
print("Geçersiz Şekil..")
