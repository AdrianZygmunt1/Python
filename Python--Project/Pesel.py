#sprawdzanie numeru PESEL
def sprawdz_pesel(pesel):
    #czy numer Pesel ma 11 cyfr i czy składa się tylko z cyfr
    if len(pesel) != 11 or pesel == "" or pesel is None or not pesel.isdigit():
        print("Nieprawidłowy numer PESEL.")
        return None
    else:
        print("")
        
    rok = pesel[:2] # rok  
    miesiac = pesel[2:4] # miesiąc
    dzien = pesel[4:6] # dzień
    numer_seryjny = pesel[6:10] # numer seryjny
    plec = pesel[9] # płeć
    cyfra_kontrolna = pesel[10] # cyfra kontrolna
    m = int(miesiac)
    #sprawdzanie rocznika na podstawie miesiąca
    if 1<= m <= 12:
        print("rocznik: 1900-1999")
        miesiac = str(m)
        rok = "19" + rok
    elif 21<= m <= 32:
        print("rocznik: 2000-2099")
        m -= 20
        miesiac = str(m)
        rok = "20" + rok
    elif 41<= m <= 52:
        print("rocznik: 2100-2199")
        m -= 40
        miesiac = str(m)
        rok = "21" + rok
    elif 61<= m <= 72:
        print("rocznik: 2200-2299")
        m -= 60
        miesiac = str(m)
        rok = "22" + rok
    elif 81<= m <= 92:
        print("rocznik: 1800-1899")
        m -= 80
        miesiac = str(m)
        rok = "18" + rok
    else:
        print("Nieprawidłowy numer PESEL.")
        return None
    #sprawdzanie płci
    if int(plec) % 2 == 0:
        print("Płeć: Kobieta")
        plec = "Kobieta"
    else:        
        print("Płeć: Mężczyzna")
        plec = "Mężczyzna"
    
    
    print(f"Urodzony: {dzien}-{miesiac}-{rok}")
    print(f"Numer seryjny: {numer_seryjny}")
    print(f"Cyfra kontrolna: {cyfra_kontrolna}\n")  
    
while True:
    print("Podaj numer PESEL lub wpisz 'exit' aby zakończyć program:")
    pesel = input()
    if pesel.lower() == 'exit':
        break
    sprawdz_pesel(pesel)
