print("Gireceğiniz 3 sayi arasından en büyüğünü bulacağım!")
A= int(input("İlk sayıyı giriniz:\n"))
B= int(input("İkinci sayıyı giriniz: \n"))
C= int(input("Üçüncü sayıyı giriniz:\n"))
if (A>=B and A>=C):
    print("En büyük sayi",A)
elif (B>=A and B>=C):
    print("En büyük sayi",B)
else:
    print("En büyük sayi",C)
