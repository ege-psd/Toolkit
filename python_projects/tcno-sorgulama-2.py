'''
while True:
    print('Türkiye Cumhuriyeti Kimlik Numarası Doğrulama Sistemi Hizmete Hazırdır.')
    tcno = input('Türkiye Cumhuriyeti Kimlik Numarasını Giriniz: ')
    if len(tcno) != 11:
        print("Eksik ya da fazla karakter girdiniz!")
        continue
    tcnotek = (int(tcno[0]) + int(tcno[2]) + int(tcno[4]) + int(tcno[6]) + int(tcno[8])) * 7
    tcnocift = int(tcno[1]) + int(tcno[3]) + int(tcno[5]) + int(tcno[7])

    tcnofark = tcnotek - tcnocift
    tcnosonhane = tcnofark % 10

    tcbolum = 0
    for rakam in tcno:
        tcbolum += int(rakam)

    tcbolum = (tcbolum - int(tcno[10])) % 10

    if int(tcno[9]) == tcnosonhane and int(tcno[10]) == tcbolum:
        print('TCNO dogru!')

    else:
        print("TCNO hatali!\nTekrar deneyin...")
'''
while True:
    idno = int(input("kimlik no giriniz"))
    teklist = [0, 2, 4, 6, 8]
    tektoplam = 0
    çiftlist = [1, 3, 5, 7]
    çifttoplam = 0
    toplam3 = 0
    if len(str(idno)) == 11:
        if str(idno)[0] != 0:
            for i in teklist:
                tektoplam += int(str(idno)[i])
            for a in çiftlist:
                çifttoplam += int(str(idno)[a])
            if (tektoplam * 7 - çifttoplam) % 10 == int(str(idno)[9]):
                for x in range(10):
                    toplam3 += int(str(idno)[x])
                    if toplam3 % 10 == int(str(idno)[10]):
                        print("TC.no doğru")
    else:
        print("TC.no hatalı")

