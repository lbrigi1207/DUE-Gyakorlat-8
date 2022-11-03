class Dolgozo():
    nev = ''
    kor = None
    email = ''
    jelszo = ''

    #automatikus függvény = Konstruktor
    def __init__(self, nev, kor, email, jelszo=''):
        self.nev = nev
        self.korkerdes()
        self.email = email
        self.jelszo = '123'

    def korertek(self, ertek): #self-> önmagára mutató érték (dolg0-ra vonatkozik)
        self.kor = ertek

#Objektum létrehozása,
#dolg0 = Dolgozo() nemcsak tulajdonságai hanem metódusai is lehetnek, ez esetben -> értékadó metódus

    def korkerdes(self):
        kor = input('Hány éves vagy: ')
        hiba = True
        for i in range(len(kor)):
            if kor[i].isnumeric():
                hiba = False
                break
        if hiba:
            print('Nem érvényes kor')
            self.kor=0
        else:
            self.kor = kor