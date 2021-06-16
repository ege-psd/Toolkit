#1/ekrana-yazdirma, format-fonksiyonu
print('engin\nege\nes')

print('08.02.2006', sep = '/')

print('{} + {} = {}' .format(2,3,2 + 3))

#2/veri-tipleri, degiskenler
a = 3 # integer

b = 3.14 # float

c = 'python' # string

d = [1,2,3,4,5,'python'] # list

e = (1,2,3,4,5,'python') # tuple

f = {'elma':3, 'armut':4, 'kiraz':5} # dict

g = True #boolean

h = False #boolean

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

print(a,b,c)

#3/matematik-operatorleri 
print (3 + 4)
print (10 - 3)
print (10 * 3)
print (10 / 4)

print (10 // 4)
print (10 % 4)

a = 5
b = 10

c = a + 2 * b

print(c)

a = 'python '
b = 'programlama '
c = 'dili'

d = (a + b + c)

print(d)

a = 'python'

print(a * 5)

a = 'python '

print(a * 5)

#3.1/ucgen-cizme

print('o ' * 1)
print('o ' * 2)
print('o ' * 3)
print('o ' * 4)
print('o ' * 5)
print('o ' * 6)
print('o ' * 7)
print('o ' * 8)
print('o ' * 9)

#4/indexleme
a = 'python'
b = [1,2,3,4,5,6,7]

print(a[0])
print(a[2]) # verinin belirtilen siradaki degerini yazdirir
print(len(a)) # verinin uzunlugunu yazdirir
print(len(b))
print(a[len(a)-1])
print(b[len(b)-1])


print(a[0:2]) # veriden yazilan ilk degerden son degere kadar olan kısmı yazıdr
print(a[2:])

q = a[0:2]
e = a[2:]

print(q + e)

print(a[:])
print(a[:4])

print(b[2:])
print(b[:5])

print(b[::2])

a = {'elma':3, 'armut':4, 'kiraz':5}

print(a['elma']) 
print(a['armut'])
print(a['kiraz'])

print((a['elma']) + (a['armut']) + (a['kiraz']))

r = (a['elma']) + (a['armut']) + (a['kiraz'])

print(type(r))

#5/input-alma

yas = input('Yaşınızı Giriniz: ')
print('Yaşınız:', yas)

a = input('a: ')
b = input('b: ')
c = input('c: ')

print('Toplam' ,a+b+c)

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

print('Toplam' ,a+b+c)

#6/kosullu-durumlar(if-elif-else)
yas = int(input('Yaşınızı Gİriniz: '))

if yas < 18:
    print('Giriş Sağlayamazsınız.')

print('Selam,Hoşgeldin') # first-program

isim = input('İsminizi Giriniz: ')
soyisim = input('Soyisminizi Giriniz: ')
yas = input('Yaşınızı Giriniz: ')

print('İsminiz: ', isim)
print('Soyisminiz: ' ,soyisim)
print('Yaşınız:' ,yas)

#ucgen-cizme
num = int(input('Şeklin Yüksekliğini Giriniz: '))
for i in range(0,num):
      for j in range(0,num-i-1):
            print(end=' ')
      for j in range(0,2*i+1):
            print('*',end='')
      print()

