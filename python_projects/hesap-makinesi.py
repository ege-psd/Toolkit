while True:
    print('Hesap Makinesi İşleme Hazırdır.')
    try:
        print('Toplama: 1\nÇıkarma: 2\nÇarpma: 3\nBölme: 4\nÜs Alma: 5')

        islem = int(input('İşlem Seçiniz: '))

        if islem == 1:
            print('Toplama İşlemini Seçtiniz.')
            sayi1 = int(input('1. Sayıyı Giriniz: '))
            sayi2 = int(input('2. Sayıyı Giriniz: '))
            print('İşlemin Sonucu: ',sayi1 + sayi2)

        elif islem == 2:
            print('Çıkarma İşlemini Seçtiniz.')
            sayi1 = int(input('1. Sayıyı Giriniz: '))
            sayi2 = int(input('2. Sayıyı Giriniz: '))
            print('İşlemin Sonucu: ',sayi1 - sayi2)

        elif islem == 3:
            print('Çarpma İşlemini Seçtiniz.')
            sayi1 = int(input('1. Sayıyı Giriniz: '))
            sayi2 = int(input('2. Sayıyı Giriniz: '))
            print('İşlemin Sonucu: ',sayi1 * sayi2)

        elif islem == 4:
            print('Bölme İşlemini Seçtiniz.')
            sayi1 = int(input('1. Sayıyı Giriniz: '))
            sayi2 = int(input('2. Sayıyı Giriniz: '))
            print('İşlemin Sonucu: ',sayi1 / sayi2)

        elif islem == 5:
            print('Üs Alma İşlemini Seçtiniz.')
            sayi1 = int(input('Üssünü Alınmasını İstediğiniz Sayıyı Giriniz: '))
            sayi2 = int(input('Üssü Giriniz: '))
            print('İşlemin Sonucu: ',sayi1 ** sayi2)

        else:
            print('Geçersiz İşlem!')

    except ValueError:
        print('Hatalı Giriş Yaptınız! Tekrar Deneyiniz.\nSadece Sayı Giriniz.')