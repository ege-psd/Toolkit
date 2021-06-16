'''
#1\data-types

#1.1\integer(int):
1, 3, 7, 93

#1.2\string(str):
'Ege', 'Merhaba', '1', '2'

#1.4\float:
0.32, 1.645, 8.875

#1.3\boolean(bool):
True, False

#1.5\list
['apple', 35, 74,8]

#1.6\dictionaries(dict)
{'bir': '1', 'iki': '2', 'uc': '3'}

#2\variables

x = 3                                                       # <class'int'>
v = 'Ege'                                                   # <class'str'>
c = 85.9                                                    # <class'float'>
b = False                                                   # <class'bool'>
n = ['car', 83, 63,2]                                       # <class'list'>
m = {'izmir': '35', 'eskisehir': '26', 'istanbul': '34'}    # <class'dict'>

print(type(m)) # print the type of variables

#3\input

q = input('Değişken Giriniz: ') # input data from user

#4\.format


#5\sample-program

print('Welcome the Registry Page')

name = input('Enter Your Name: ')

sname = input('Enter Your Surname: ')

age = int(input('Enter Your Age: '))

print("Name: {}\nSurname: {}\nAge: {}".format(name, sname, age))


#6\sample-program-2

while True:

    faktoriyel = 1

    sayi = int(input('Faktoriyeli Alınmasını İstediğiniz Sayıyı Girin: '))

    if sayi > 0:
        for i in range(1, sayi+1):
            faktoriyel = faktoriyel * i

    else:
       print('Hatalı İşlem Yaptınız!\nSadece Pozitif Sayı Girişi Yapınız.')

    print(faktoriyel)

#6\sample-program-3

while True:

    try:
        def faktoriyel(sayi):

            faktoriyel = 1

            if sayi > 0:
                for i in range(1, sayi + 1):
                    faktoriyel = faktoriyel * i

            else:
                print('Hatalı İşlem Yaptınız!\nSadece Pozitif Sayı Girişi Yapınız.')

            print('Faktoriyel: {}'.format(faktoriyel))

        faktoriyel(int(input('Faktoriyeli Hesaplanmasını İstediğiniz Sayıyı Giriniz: ')))

    except ValueError:
        print('Hatalı İşlem Yaptınız!\nSadece Sayı Girişi Yapınız.')

#6\sample-program-3

while True:

    import urllib.request

    url = input("Dosya URL'sini Giriniz: ")

    urllib.request.urlretrieve(url, 'image.png')

    print('Dosya Bulunduğunuz Dizine Başarıyla İndirildi.')

print("Faruk'un Sinemasına Hoşgeldiniz.")

class Dusman:
    kalan_can = 3
    def saldir(self):
        print('Hücum')
        self.kalan_can -= 1
    def hayatta_mi(self):
        if (self.kalan_can <= 0):
            print('Mefta')
        else:
            print(str(self.kalan_can) + ' Canım Kaldı.')

dusman1 = Dusman()

dusman1.saldir()
dusman1.saldir()
dusman1.hayatta_mi()


print('Hesap Makinesi Kullanıma Hazırdır.')

class Calculator:

    def __init__ (self, islem, sayi1, sayi2):
        self.islem = int(islem)
        self.sayi1 = int(sayi1)
        self.sayi2 = int(sayi2)

        if self.islem == 1:
            print('İşlem Sonucu: ', self.sayi1 + self.sayi2)

        if self.islem == 2:
            print('İşlem Sonucu: ', self.sayi1 - self.sayi2)

        if self.islem == 3:
            print('İşlem Sonucu: ', self.sayi1 * self.sayi2)

        if self.islem == 4:
            print('İşlem Sonucu: ', self.sayi1 / self.sayi2)

while True:

    print("""
    Toplama için tuşlayınız:    1
    Çıkarma için tuşlayınız:    2
    Çarpma için tuşlayınız:     3
    Bölme için tuşlayınız:      4
    """)

    calculator = Calculator(input('İşlem Seçiniz: '), input('1. Sayıyı Giriniz: '), input('2. Sayıyı Giriniz: '))

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


class MEB:

    def __init__(self, okul_adi, isim, soyisim, sinif_duzeyi):
        self.okul_adi = okul_adi
        self.isim = isim
        self.soyisim = soyisim
        self.sinif_duzeyi = sinif_duzeyi

        file = open(self.okul_adi + '.js', 'w')
        file.write(self.isim)
        file.write(self.soyisim)
        file.write(self.sinif_duzeyi)

while True:
    kayit_sistemi = MEB(input('Okul Adı Giriniz: ') , input('İsminizi Giriniz: ') , input('Soyisminizi Giriniz: ') , input('Sınıf Seviyenizi Giriniz: '))

'''

import random

word = random.choice(['win', 'lose', 'draw'])

print(word)