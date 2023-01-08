"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""
sayi= int(input("Sayi girin ve mükemmel sayi olup olmadığını bulalım:"))
bolen=0
liste = range(1,sayi)
for i in liste:
    if (sayi % i == 0):
        bolen +=i
        i+=1
    else:
        i+=1

if (bolen==sayi):
    print("Sayınız Mükemmel Sayıdır!")
else:
    print("Sayiniz Mükemmel Sayi Değildir!")