"""
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
"""
liste1 = range(1,11)
liste2 = range(1,11)
for i in liste1:
    print("\n")
    for x in liste2:
        sonuc = i * x
        print("{0} x {1} = {2}".format(i,x,sonuc))