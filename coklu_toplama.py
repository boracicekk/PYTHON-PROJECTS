"""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.
"""
print("İstediğiniz kadar sayi girin hepsini toplayalım.DİPNOT:Programı bitirip sonucu görmek istediğiniz zaman 'q' tuşuna basınız.")
toplam = 0

while True:
    sayi= input("Sayi giriniz:")
    if(sayi=="q"):
        break
    sayi= int(sayi)
    toplam += sayi
print(toplam)