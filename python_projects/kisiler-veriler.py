file = open('kisiler-veriler.txt','a')

while True:
    file = open('kisiler-veriler.txt','a')

    print('Selam,Hoşgeldin.')

    isim = input('İsminizi Giriniz: ')
    soyisim = input('Soyisminizi Giriniz: ')
    yas = input('Yaşınızı Giriniz: ')

    file.write('\nİsminiz: ')
    file.write(isim)
    file.write('\nSoyisminiz: ')
    file.write(soyisim)
    file.write('\nYaşınız: ')
    file.write(yas)

    print('Teşekkürler!\nKayıt Başarılı.')

    file.close()
