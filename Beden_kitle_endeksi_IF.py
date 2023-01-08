""""Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""
print("Beden kitle endeksi hesaplama programı!")
Boy = float(input("Boyunuzu giriniz (m) :\n"))
Kilo = int(input("Kilonuzu giriniz(kg) :\n"))
Endeks = Kilo/Boy**2
if Endeks<18.5:
    print("Zayıf")
elif 18.5<=Endeks<25:
    print("Normal")
elif 25<=Endeks<30:
    print("Fazla kilolu")
else:
    print("Obez")
