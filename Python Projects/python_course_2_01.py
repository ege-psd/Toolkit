'''
#1\data-types

#1.1\integer(int):
1, 3, 7, 93

#1.2\string(str):
'Ege', 'Merhaba', '1', '2'

#1.3\boolean(bool):
True, False

#1.4\float:
0.32, 1.645, 8.875

#2\variables

x = 3
c = 85.9
v = 'Ege'

print(x)
print(c)
print(v)

#basic-program
print('Merhaba! Seni görmek ne hoş. :D\nİsmin ne?')
isim = input('İsminiz: ')
print('Tanıştığıma memnun oldum!', isim)

q = 'engin'
w = 'ege'
e = 'es'
r = 'eymen'
print(len(q) + len(w) + len(e))

print(len(q) == len(r))

print(q[::2])

for x in range(0, 10, 1):
    print(x)

for q in range(0, 100, 5):
    print(q)

while True:
    print('ege')
    break

q = True
while q:
    print(type(q))

for x in range(0, 5):
    password = input('Password: ')
    if password != 'benimsifrem':
        print('Hop! Dur aslan parçası.')
    else:
        print('Aferin, bir işe yaradın.')


fruits = ['apple', 'banana', 3]
print(len(fruits))
print(fruits[1])
print(type(fruits[2]))


sınıf1 = ['ahmet', 'mehmet', 'ayşe', 'elif', 'ege', 'irem']
sınıf2 = ['mark', 'elon', 'zukerbag', 'musk']
print(sınıf1[2], sınıf2[1], 'ege')

sınıf1.append('ekleme')

print(sınıf1)

sınıf1[1] = 'çüşş'
print(sınıf1)

kisiler = ['ben', 'sen', 'o', 'biz', 'siz', 'onlar', 'i', 'you', 'it', 'we', 'you', 'they']
for kisi in kisiler:
    print(kisi)

kisiler = ['ben', 'sen', 'o', 'biz', 'siz', 'onlar', 'i', 'you', 'it', 'we', 'you', 'they']
for kisi in kisiler:
    if kisi != 'o':
        print(kisi)

kisiler = ['ben', 'sen', 'o', 'biz', 'siz', 'onlar', 'i', 'you', 'it', 'we', 'you', 'they']

for x in range(0, 12):
    if kisiler[x] == 'o':
        print(kisiler[x])
    else:
        print('o değil')

kisiler = ['ben', 'sen', 'o', 'biz', 'siz', 'onlar', 'i', 'you', 'it', 'we', 'you', 'they']

for x in range(len(kisiler)):
    if kisiler[x] == 'o':
        print(kisiler[x])
    else:
        print('o değil')

print('Dosya İsmi Oluşturucu Hazırdır.')

filename = input('Dosya İsmini Giriniz: ')
print(filename.strip())

q = '     '
print(len(q))

text = (input('Değer Giriniz: '))
print(len(text))

print('Dosya İsmi Oluşturucu Hizmetinizdedir.')
filename = input('Dosya İsmini Giriniz: ')
filenamelower = filename.lower()
filenamegapless = filenamelower.strip()
print(filenamegapless)


print('Başlık Yazıcı Hizmetinizdedir.')
title = input('Başlığı Giriniz: ')
print(title.upper())

list1 = input('Değer Giriniz: ')
print(list1.split('/'))

x = ('Bekleme Yapma Ticari!')
for x in range(0, 101, 10):
    print('Bekleme Yapma Ticari!')

while True:
    print('Hesap Makinesi Hizmetinizdedir.')
    try:
        print('Toplama İşlemi: 1\nÇıkarma İşlemi: 2\nÇarpma İşlemi: 3\nBölme İşlemi: 4')

        islem = int(input('İşlem Seçiniz: '))

        if islem == 1:

            sayi1 = int(input('1. Sayıyı Giriniz: '))
            sayi2 = int(input('2. Sayıyı Giriniz: '))

            def toplama(sayi1, sayi2):
                return sayi1 + sayi2

            toplam = toplama(sayi1, sayi2)
            print('Sonuç:', toplam)

        elif islem == 2:

            sayi1 = int(input('1. Sayıyı Giriniz: '))
            sayi2 = int(input('2. Sayıyı Giriniz: '))

            def cikarma(sayi1, sayi2):
                return sayi1 - sayi2

            toplam = cikarma(sayi1, sayi2)
            print('Sonuç:', toplam)

        elif islem == 3:

            sayi1 = int(input('1. Sayıyı Giriniz: '))
            sayi2 = int(input('2. Sayıyı Giriniz: '))

            def carpma(sayi1, sayi2):
                return sayi1 * sayi2

            toplam = carpma(sayi1, sayi2)
            print('Sonuç:', toplam)

        elif islem == 4:

            sayi1 = int(input('1. Sayıyı Giriniz: '))
            sayi2 = int(input('2. Sayıyı Giriniz: '))

            def bolme(sayi1, sayi2):
                return sayi1 / sayi2

            toplam = bolme(sayi1, sayi2)
            print('Sonuç:', toplam)

        else:
            print('Geçersiz İşlem!')

    except ValueError:
        print('Hatalı Giriş Yaptınız! Tekrar Deneyiniz.\nSadece Sayı Giriniz.')

while True:
    print('Selam! Hoşgeldin.')
    name = input('İsminizi Giriniz: ')
    surname = input('Soyisminizi Giriniz: ')
    age = (input('Yaşınızı Giriniz: '))

    if int(age) >= 18:
        kayıt

    else:
        gulegule

    if int(age) >= 18:
        file = open('kisiler-veriler-v2.txt', 'w')
        file.write('\nİsim: ')
        file.write(name)

        file.write('\nSoyisim: ')
        file.write(surname)

        file.write('\nYaş:')
        file.write(age)

        file.close()

        print('Kayıt Tamamlanmıştır!\nTeşekkür Ederiz.')
    else:
        print('Yaşınız Sınırı Karşılamamaktadır!\nKayıt olamazsınız.')

yorum = input('Yorumunuzu Giriniz: ')
q = yorum.find('küfür' or 'küfür2' or 'küfür3')
if q > 0:
    print('Yorum Giremezsiniz! Küfür ve hareket içeren mesajlar girmek yasaktır.')

yorum = input('Yorumunuzu Giriniz: ')
if yorum.find('küfür' or 'küfür2' or 'küfür3') >= 0:
    print('Yorum Giremezsiniz! Küfür ve hareket içeren mesajlar girmek yasaktır.')

import math

print(math.degrees(10))

import myModule

print('Hesap Makinesi Hizmete Hazırdır.')

while True:

    print('Toplama için giriniz: 1\nÇıkarma için giriniz: 2\nÇarpma için giriniz: 3\nBölme için giriniz: 4')

    islem = input('İşlem Seçiniz: ' )

    number1 = int(input('1. Sayıyı Giriniz: '))
    number2 = int(input('2. Sayıyı Giriniz: '))

    if islem == '1':
        print(myModule.toplama(number1, number2))

    elif islem == '2':
        print(myModule.cikarma(number1, number2))

    elif islem == '3':
        print(myModule.carpma(number1, number2))

    elif islem == '4':
        print(myModule.bolme(number1, number2))

    else:
        print('Hatalı Giriş Yaptınız\nTekrar Deneyiniz.')

print('Hesap Makinesi Hizmete Hazırdır.')

while True:
    print('Toplama İşlemi İçin 1 Değeri Giriniz.\nÇıkarma İşlemi İçin 2 Değeri Giriniz.\nÇarpma İşlemi İçin 3 Değeri Giriniz.\nBölme İşlemi İçin 4 Değeri Giriniz.')

    try:

        islem = int(input('İşlem Seçiniz: '))

        sayi1 = int(input('1. Sayıyı Giriniz: '))
        sayi2 = int(input('2. Sayıyı Giriniz: '))

        def toplama(sayi1, sayi2):
            print('{} + {} = {}'.format(sayi1, sayi2, sayi1+sayi2))

        def cikarma(sayi1, sayi2):
            print('{} - {} = {}'.format(sayi1, sayi2, sayi1-sayi2))

        def carpma(sayi1, sayi2):
            print('{} * {} = {}'.format(sayi1, sayi2, sayi1*sayi2))

        def bolme(sayi1, sayi2):
            print('{} / {} = {}'.format(sayi1, sayi2, sayi1/sayi2))

        if islem == 1:
            toplama(sayi1, sayi2)

        elif islem == 2:
            cikarma(sayi1, sayi2)

        elif islem == 3:
            carpma(sayi1, sayi2)

        elif islem == 4:
            bolme(sayi1, sayi2)

        else:
            print('Hatalı Giriş Yaptınız! Tekrar Deneyiniz.\nYanlış İşlem Numarası Girişi Yaptınız.')

    except ValueError:
        print('Hatalı Giriş Yaptınız! Tekrar Deneyiniz.\nSadece Sayı Giriniz.')

'''

class MEB:

    def __init__(self, okul_adi, isim, soyisim, sinif):
        self.okul_adi = okul_adi
        self.isim = isim
        self.soyisim = soyisim
        self.sinif = int(sinif)

        if self.sinif == 9:
            file = open('9-bilgiler.txt', 'w')
            file.write('\nOkul: ')
            file.write(self.okul_adi)

            file.write('\nİsim: ')
            file.write(self.isim)

            file.write('\nSoyisim: ')
            file.write(self.soyisim)

        if self.sinif == 10:
            file = open('10-bilgiler.txt', 'w')
            file.write('\nOkul: ')
            file.write(self.okul_adi)

            file.write('\nİsim: ')
            file.write(self.isim)

            file.write('\nSoyisim: ')
            file.write(self.soyisim)

        if self.sinif == 11:
            file = open('11-bilgiler.txt', 'w')
            file.write('\nOkul: ')
            file.write(self.okul_adi)

            file.write('\nİsim: ')
            file.write(self.isim)

            file.write('\nSoyisim: ')
            file.write(self.soyisim)

        if self.sinif == 12:
            file = open('12-bilgiler.txt', 'w')
            file.write('\nOkul: ')
            file.write(self.okul_adi)

            file.write('\nİsim: ')
            file.write(self.isim)

            file.write('\nSoyisim: ')
            file.write(self.soyisim)

while True:
    kayit_sistemi = MEB(input('Okul Adı Giriniz: '), input('İsim Giriniz: '), input('Soyisim Giriniz: '), input('Sınıf Giriniz: '))