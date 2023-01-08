print("""*******************
Gireceğiniz bir sayının faktöriyelini bulacağım programa hoşgeldin!
Çıkmak için 'q' ya basınız.
*******************""")
while True:
    sayi = input("Sayiyi giriniz:")
    if (sayi=='q'):
        break
    else:
        sayi = int(sayi)
        faktoriyel = 1
    for i in range(2,sayi+1):
        faktoriyel *= i
        i +=1
        if(i>sayi):
            print("Faktoriyel:",faktoriyel)