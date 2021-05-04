while True:
    print('Türkiye Cumhuriyeti Kimlik Numarası Doğrulama Sistemi Hizmete Hazırdır.')

    tcno = input('Türkiye Cumhuriyeti Kimlik Numarasını Giriniz: ')

    tcnotek = (int(tcno[0]) + int(tcno[2]) + int(tcno[4]) + int(tcno[6]) + int(tcno[8])) * 7
    tcnocift  = int(tcno[1]) + int(tcno[3]) + int(tcno[5]) + int(tcno[7])

    tcnofark = int(tcnotek) - int(tcnocift)

    tcnosonhane = int(tcnofark) % 10

    tcno10 = int(tcno[0]) + int(tcno[1]) + int(tcno[2]) + int(tcno[3]) + int(tcno[4]) + int(tcno[5]) + int(tcno[6]) + int(tcno[7]) + int(tcno[8]) + int(tcno[9])
    tcbolum = int(tcno10) % 10

    if len(tcno) != 11:
        print('Hatalı Giriş Yaptınız!\nEksik ya da fazla rakam girişi yaptınız.')

    elif tcno[0] == '0':
        print('Hatalı Giriş Yaptınız!\nTürkiye Cumhuriyeti Kimlik Numarası 0 (sıfır) Rakamıyla Başlamaz.')

    elif int(tcno[9]) != tcnosonhane:
        print('Hatalı Giriş Yaptınız!\nTekrar Deneyiniz.')

    elif int(tcno[10]) != tcbolum:
        print('Hatalı Giriş Yaptınız!\nTekrar Deneyiniz.')

    else:
        print('Türkiye Cumhuriyeti Kimlik Numarası Doğrulanmıştır!\nTeşekkür Ederiz.')
