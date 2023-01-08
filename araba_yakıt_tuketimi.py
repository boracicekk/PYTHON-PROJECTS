"""Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın."""
Fuel = int(input("Aracınız km başına kaç litre benzin yakıyor:"))
Distance = int(input("Kaç km yol gideceksiniz :"))
PriceofFuel = 30
TotalPrice=Fuel*Distance*PriceofFuel
bilgiler = [Fuel,Distance,TotalPrice]
print("Aracinizin kilometre başına yaktığı benzin miktarı {}\nAracınızla toplam gideceğiniz mesafe:{}\nÖdeyeceğiniz ücret ={}".format(bilgiler[0],bilgiler[1],bilgiler[2]))