A = int(input("İlk sayiyi giriniz:\n"))
B =  int(input("İkinci sayiyi giriniz:\n"))
C = input("Hangi işlemi yapmak istiyorsanız karşılık gelen sayıyı seçiniz:")
if C == "1":
    print("Cevabınız:{}", A+B)
elif C == "2":
    print("Cevabınız:{}", A-B)
elif C== "3":
    print("Cevabınız:{}", A*B)
elif C == "4":
    print("Cevabınız:{}", A/B)
else:
    print("Lütfen geçerli bir sayı giriniz!")