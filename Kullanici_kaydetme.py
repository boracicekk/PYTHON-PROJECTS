"""Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın."""
Ad = input("Adınızı giriniz:")
Soyad = input("Soyadınızı giriniz:")
Numara = int(input("Numaranizi giriniz:"))
print("Bilgileriniz Kaydediliyor...\n")
bilgiler = [Ad,Soyad,Numara]
print("Kullanıcının Adı:{}\nKullanıcının Soyadı:{}\nBKullanıcının Numarası:{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))