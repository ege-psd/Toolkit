
print('Merhaba\nHoşgeldin!')

yas = int(input('Yaşınızı Giriniz: '))

if yas < 18:
    print('Giriş Sağlayamazsın.')
    print('18 Yaşından Küçüksünüz.')

else:
    print('Giriş Onaylandı')

#Basit Hesap Makinesi#
print('Toplama: 1\nÇıkarma: 2\nÇarpma: 3\nBölme: 4')

islem = int(input('İşlemi Giriniz: '))

if islem == 1:
    print('Toplama İşlemini Seçtiniz.')
    sayi1 = int(input('1. Sayıyı Giriniz: '))
    sayi2 = int(input('2. Sayıyı Giriniz: '))
    print(sayi1 + sayi2)

elif islem == 2:
    print('Çıkarma İşlemini Seçtiniz.')
    sayi1 = int(input('1. Sayıyı Giriniz: '))
    sayi2 = int(input('2. Sayıyı Giriniz: '))
    print(sayi1 -
          sayi2)
    
elif islem == 3:
    print('Çarpma İşlemini Seçtiniz.')
    sayi1 = int(input('1. Sayıyı Giriniz: '))
    sayi2 = int(input('2. Sayıyı Giriniz: '))
    print(sayi1 * sayi2)
    
elif islem == 4:
    print('Bölme İşlemini Seçtiniz.')
    sayi1 = int(input('1. Sayıyı Giriniz: '))
    sayi2 = int(input('2. Sayıyı Giriniz: '))
    print(sayi1 / sayi2)


else:
    print('Geçersiz İşlem!')    


a = 3
b = 4

if a == 3 and b == 4:
    print('Evet.')

else:
    print('Hayır.')

        
sayi1 = input('1. Sayıyı Giriniz: ')
sayi2 = input('2. Sayıyı Giriniz: ')

if sayi1 == 3 and sayi2 == 4:
    print('Evet.')

else:
    print('Hayır.')

#-----------------------------------------#

sayi1 = int(input('1. Sayıyı Giriniz: '))
sayi2 = int(input('2. Sayıyı Giriniz: '))

if sayi1 == 3 and sayi2 == 4:
    print('Evet.')

else:
    print('Hayır.')

#-----------------------------------------#

sayi1 = (input('1. Sayıyı Giriniz: '))
sayi2 = (input('2. Sayıyı Giriniz: '))

if sayi1 == '3' and sayi2 == '4':
    print('Evet.')

else:
    print('Hayır.')


a = 2
b = 3

if a == 3 or b == 4:
    print('Yeah!')

else:
    print('Fuck!\nKomik misin?:D')



if (not (3 == 4)):
    print('Evet!')

if (not(4 < 3)):
    print('Ne Saçmalayıp duruyon sen?')
