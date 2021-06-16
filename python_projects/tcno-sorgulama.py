#TC kimlik no kuralları:#

#TC kimlik no 11 haneli rakamlardan oluşur.#
#İlk rakam sıfır (0) olamaz.#
#1, 3, 5, 7 ve 9. hanelerin toplamının 7 katı ile 2, 4, 6 ve 8. hanelerin toplamı çıkartılır, sonucun 10’a bölümünden kalanı 10. haneyi verir.#
#İlk 10 hanenin toplamının 10’a bölümünden kalan, son haneyi verir.#
#Ayrıca çeşitli hatalı kabul edilen TC kimlik numaraları vardır.#
#Kontrol sorgusu yapılabilir, bazı istisnalara sahiptir.#

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