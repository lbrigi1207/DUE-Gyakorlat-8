#import jelszo
#jelszo.jelszo_ellenorzese()
'''
from jelszo import *

#print('A megadott jelszó:', jelszo_ellenorzese(3, True))

szam = input('Kérek egy számot: ')
while szamjegy(szam, True,'Nem szám!'):
    szam = input('Kérek egy számot: ')
'''
from osztaly import *

dolg0 = Dolgozo('Kata', 23, 'kata@gmail.com')
dolg1 = Dolgozo('Karcsi', 21, 'karcsi@gmail.com')

print(dolg0.nev)
print(dolg0.kor)
print(dolg0.email)
print(dolg0.jelszo)

print(dolg1.nev)
print(dolg1.kor)
print(dolg1.email)
print(dolg1.jelszo)