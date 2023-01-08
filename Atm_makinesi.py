print("""*****************************
Atm makinesi programima hoşgeldiniz!
1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
Programdan çıkmak için 'q' ya basınız.
*****************************
""")
Bakiye = 1000
Miktar = 0
while True:
    islem = input("İşlemi giriniz:")
    if(islem == 'q'):
        print("Yeniden Bekleriz...")
        break
    elif(islem=="1"):
        print("Bakiyeniz:",Bakiye)
    elif(islem=="2"):
        Miktar = int(input("Miktarı giriniz:"))
        Bakiye += Miktar

    elif(islem=="3"):
        Miktar = int(input("Miktarı giriniz:"))
        Bakiye -= Miktar
    else:
        print("Lütfen eşleşen bir işlem giriniz...")
