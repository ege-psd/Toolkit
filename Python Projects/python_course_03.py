''' 
#bilmemkac/while-dongusu
i = 0

while i < 10:
    print('i:',i)
    i = i + 1

i = 0

while i <= 10:
    print('i:',i)
    i = i + 1

i=0

while i <= 10:
    print('i:',i)
    i += 1


i = 0

while i <= 10:
    print('i:',i)
    i += 2


i = 1

while(i <= 1024):
    print('i:',i)
    i *= 2
'''

'''
#bilmemkac2/break-continue
i = 0

while (i < 10):
    if i == 5:
        break
    print('i:',i)
    i += 1

i = 0

while (i < 10):
    if i == 3 or i == 5:
        continue
    print('i:',i)
    i += 1


i = 0

while (i < 10):
    if i == 5:
        i += 1
        continue
    print('i:',i)
    i += 1

'''

#bilmemkac3/for-dongusu-range-fonksiyonu
a = [1,2,3,4,5,6]

for eleman in a:
    print(eleman)

b = 'Python'

for karakter in b:
    print(karakter)

for sayi in range(10,100,2):
    print(sayi)
