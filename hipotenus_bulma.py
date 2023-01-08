"""Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın."""
a = int(input("Bir kenarını giriniz:\n"))
b = int(input("İkinci kenarını giriniz:\n"))
c = (a**2 + b**2)**(1/2)
print("Hipotenüs değeriniz:{}",c)