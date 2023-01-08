"""Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)"""

print("Gireceğiniz verilere göre sizin vücut kütle endeksinizi hesaplayacağım")
Boy = int(input("Boyunuzu giriniz(m):"))
Kilo = int(input("Kilonuzu giriniz(m):"))
Endeks = (Kilo/Boy)*Boy
print("Vücut kitle endeksiniz:{}".format(Endeks))
