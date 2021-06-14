
# corona_ep = {grad:[broj_zarazenih, broj_oporavljenih, broj_umrlih]}

print("PODACI O CORONA EPIDEMIJI")
print(" ")
class Grad:
    corona_baza = {'Sarajevo': [10, 8, 1], 'Zenica': [8, 5, 0],'Konjic':[21, 4, 2]}   #Formiramo rječnik sa gradovima i podacima o corona epidemiji unutar klase

    def __init__(self, naziv_grada=0, br_zarazenih=0, br_oporavljenih=0, br_umrlih=0):
        self.naziv_grada = naziv_grada
        self.br_zarazenih = br_zarazenih                    #Kreiramo varijable (podatke) unutar klase, i oni su nam postavljeni na defaultnu vrijednost = 0
        self.br_oporavljenih = br_oporavljenih
        self.br_umrlih = br_umrlih

    def azuriraj_arhivu(self):                             #Kreiramo funkciju koja će nam omogućiti ažuriranje podataka za grad koji već postoji unijet
        if self.naziv_grada in Grad.corona_baza:
            podatak = input(
                "Koji podatak zelite ažurirati?\n1) Broj zaraženih\n2) Broj oporavljenih\n3) Broj umrlih\nIzbor: (unesi odgovarajući broj)\n ")

            if int(podatak) == 1:
                self.br_zarazenih = int(input("Unesite broj zaraženih: "))
                Grad.corona_baza[self.naziv_grada][0] = self.br_zarazenih         #Biramo opciju, u zavisnosti od toga koji podatak ažuriramo, koristeći se klasom (tj. objektima)
            elif int(podatak) == 2:                                               #Broj j 
                self.br_oporavljenih = int(
                    input("Unesite broj oporavljenih: "))
                Grad.corona_baza[self.naziv_grada][1] = self.br_oporavljenih
            elif int(podatak) == 3:
                self.br_umrlih = int(input("Unesite broj umrlih: "))
                Grad.corona_baza[self.naziv_grada][2] = self.br_umrlih

        else:
            Grad.corona_baza.update({self.naziv_grada: [0, 0, 0]})
            data = input(
                "Da li želite da unesete vrijednosti za trenutni grad?[Da/Ne]: ")     #Unosimo novi grad, pa su podaci o tom gradu postavljeni na defaultnu 0
            if data.lower() == 'da':
                self.br_zarazenih = int(input("Broj zaraženih: "))
                self.br_oporavljenih = int(input("Broj oporavljenih: "))       #Unosimo podatke o zarazenim, oporavljenim i umrlim
                self.br_umrlih = int(input("Broj umrlih: "))
                Grad.corona_baza[self.naziv_grada] = [self.br_zarazenih,        #Novi grad smještamo u bazu (odnosno u rječnik)
                                                      self.br_oporavljenih, self.br_umrlih]
                print("Unijet je novi grad u bazu:")


state = True

while state:
    for k, v in Grad.corona_baza.items():
        print(
            f"{k}: Broj zaraženih - {v[0]}, Broj oporavljenih - {v[1]}, Broj umrlih - {v[2]}")    #Ispisujemo stanje gradova koji su već u bazi
    question = input("Da li želite da ažurirate stanje?[Da/Ne]: ")
    while (question.isalpha() == False):  # Način na koji se provjerava da li je unos ispravan (da li su unijeta slova)
        question = input(
            "Unijeli ste nedozvoljene simbole. Samo slova su mogući unos. Da li želite uraditi ažuriranje stanja po gradovima? ")
    if question.lower() == 'da':

        grad = input("Unesite naziv grada: ").capitalize()        #Grad će nam biti unijet u bazu pod velikim slovom
        obj = Grad(grad)
        obj.azuriraj_arhivu()                                     #Ažurira se baza prema već ispisanoj funkciji
    else:
        for k, v in Grad.corona_baza.items():                #Ukoliko je odgovor ne, odnosno ukoliko se ne želi ažurirati baza, ispisuje nam se već postojeće stanje baze
            print(
                f"{k}: Broj zaraženih - {v[0]}, Broj oporavljenih - {v[1]}, Broj umrlih - {v[2]}")
        print("Doviđenja!")              #Na kraju se pozdravlja korisnik
        state = False
