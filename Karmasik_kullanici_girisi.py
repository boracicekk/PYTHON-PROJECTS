print("Merhabalar Kullanıcı Giriş Ekranına Hoşgeldiniz!")
sys_kullanici_adi = "bbora"
sys_parola = "123456"
sifre_hakki = 3
while True:
    kullanici_adi = input("Kullanıcı adınızı giriniz:")
    parola = input("Parolanızı giriniz:")
    if (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanıcı adı ve şifreniz hatalı...")
        sifre_hakki -= 1
    elif (kullanici_adi != sys_kullanici_adi and parola == sys_parola):
        print("Kullanıcı adınız hatalı...")
        sifre_hakki -=1
    elif (kullanici_adi == sys_kullanici_adi and parola!= sys_parola):
        print("Parolanız yanlış...")
        sifre_hakki -=1
    else:
        print("Girişiniz Başarılı!")
        break
    if (sifre_hakki==0):
        print("Deneme Hakkınız Bitmiştir!!!")
