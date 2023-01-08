""""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
"""""
print("Harf notunuzu hesaplayan program:\n")
Vize1= int(input("İlk vizenizin notunu giriniz:\n"))
Vize2= int(input("İkinci vizenizin notunu giriniz:\n"))
Final= int(input("Final notunuzu giriniz:\n"))
print("HARF NOTUNUZ HESAPLANIYOR........")
HarfNotu= Vize1 * 30/100 + Vize2 * 30/100 + Final * 40/100
if HarfNotu<55:
    print("FF")
elif 55>=HarfNotu>60:
    print("FD")
elif 60>=HarfNotu>65:
    print("DD")
elif 65>=HarfNotu>70:
    print("DC")
elif 70>=HarfNotu>75:
    print("CC")
elif 75>=HarfNotu>80:
    print("CB")
elif 80>=HarfNotu>85:
    print("BB")
elif 85>=HarfNotu>90:
    print("BA")
else:
    print("AA")