while True:

    print('Selam! Hoşgeldin.')

    isim = input('İsminizi Giriniz: ')
    soyisim = input('Soyisminizi Giriniz: ')
    yas = (input('Yaşınızı Giriniz: '))

    if int(yas) >= 18:
        file = open('kisiler-veriler-v2.txt', 'w')

        file.write('\nİsim: ')
        file.write(isim)

        file.write('\nSoyisim: ')
        file.write(soyisim)

        file.write('\nYaş:')
        file.write(yas)

        file.close()

        print('Kayıt Tamamlanmıştır!\nTeşekkür Ederiz.')

    else:
        print('Yaşınız Sınırı Karşılamamaktadır!\nKayıt olamazsınız.')
