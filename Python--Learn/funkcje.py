#wbudowane funkcje
print("Hello World") #wypisuje tekst na ekranie
len("Hello") #zwraca długość tekstu, w tym przypadku 5
type(3.14) #zwraca typ danych, w tym przypadku <class '
input("Podaj swoje imię: ") #pobiera dane od użytkownika i zwraca je jako string
int("123") #konwertuje string na liczbę całkowitą, w tym przypadku 123
def moja_funkcja():
    print("To jest moja funkcja") #definiuje funkcję o nazwie moja_funkcja, która wypisuje tekst na ekranie
moja_funkcja() #wywołuje funkcję moja_funkcja, co powoduje wypisanie tekstu na ekranie
def dodaj(a, b):
    return a + b #definiuje funkcję dodaj, która przyjmuje dwa argumenty a i b, i zwraca ich sumę
wynik = dodaj(5, 10) #wywołuje funkcję dodaj z argumentami 5 i 10, i przypisuje wynik do zmiennej wynik
print("Wynik dodawania:", wynik)

def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    
    if price <= 0:
        return "The price should be greater than 0"
    
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    return price - (price * (discount / 100))
apply_discount(100, 20) # returns 80.0