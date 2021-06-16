#bilmemkacv2/OPP(object-oriented-programing)
class Account:
    def init (self,isim,numara,bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye
    def hesapBilgileri(self):
        print('İsim: ',self.isim)
        print('Numara: ',self.numara)
        print('Bakiye: ',self.bakiye)
    def paraÇek(self,miktar):
        if (self.bakiye - miktar < 0):
            print('Yetersiz Baliye')
        else:
            self.bakiye -= miktar
            print('Yeni Bakiye: ',self.bakiye)
    def paraYatir(self,miktar):
        self.bakiye += miktar
        print('Yeni Bakiye: ',self.bakiye)
        
account = Account('Engin Ege ES',123456,1000)

account.hesapBilgileri()


        
 
