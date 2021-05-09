print('Hesap Makinesi Hizmetinizdedir.')

while True:

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
