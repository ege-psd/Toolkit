while True:
    print('Not Dönüşüm Aracı Hizmetinizdedir.')
    try:
        note = float(input('Notu Giriniz: '))
        '''
        #alternatif-kod
        if note > 100 or note < 0:
            print('Hatalı Not Girdiniz! Tekrar Deneyiniz.\nSadece 0 ile 100 Aralağında Sayılar Giriniz.')
        '''
        if note >= 90 and note <= 100:
            print('Notun Karşılığı= AA')

        elif note >= 80 and note <= 89:
            print('Notun Karşılığı= BB')

        elif note >= 70 and note <= 79:
            print('Notun Karşılığı= CC')

        elif note >= 60 and note <= 69:
            print('Notun Karşılığı= DD')

        elif note >= 50 and note <= 59:
            print('Notun Karşılığı= EE')

        elif note >=0 and note  <= 49:
            print('Notun Karşılığı= FF')
        else:
            print('Hatalı Not Girdiniz! Tekrar Deneyiniz.\nSadece 0 ile 100 Aralağında Sayılar Giriniz.')

    except ValueError:
        print('Hatalı Giriş Yaptınız! Tekrar Deneyiniz.\nSadece Sayı Giriniz.')
