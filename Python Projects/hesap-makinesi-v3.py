print('Hesap Makinesi Hizmete Hazırdır.')

while True:
    print('''
Toplama İşlemi İçin 1 Değeri Giriniz
Çıkarma İşlemi İçin 2 Değeri Giriniz
Çarpma İşlemi İçin 3 Değeri Giriniz
Bölme İşlemi İçin 4 Değeri Giriniz
    ''')

    try:

        islem = int(input('İşlem Seçiniz: '))

        sayi1 = int(input('1. Sayıyı Giriniz: '))
        sayi2 = int(input('2. Sayıyı Giriniz: '))

        def toplama(sayi1, sayi2):
            print('İşlem Sonucu:', sayi1 + sayi2)

        def cikarma(sayi1, sayi2):
            print('İşlem Sonucu:', sayi1 - sayi2)

        def carpma(sayi1, sayi2):
            print('İşlem Sonucu:', sayi1 * sayi2)

        def bolme(sayi1, sayi2):
            print('İşlem Sonucu:', sayi1 / sayi2)

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