a = int(input("İlk sayıyı giriniz:\n"))
b = int(input("İkinci sayıyı giriniz:"))
temp = a
a = b
b = temp
yerdegistirme = [a,b]
print("Artık İlk sayiniz = {}\n\nİkinci sayiniz ={}\n".format(yerdegistirme[0],yerdegistirme[1]))

