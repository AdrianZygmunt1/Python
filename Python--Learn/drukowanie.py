print("My favorite color is " , "blue", "yellow", "red")#print z wieloma argumentami, oddzielonymi przecinkiem
print("hello", "world") #domyślnie print oddziela argumenty spacją
print("Python", "is", "awesome", sep="-") #sep pozwala na zmian
names = """
Alice
Bob
Charlie
"""#trzy cudzysłowy pozwalają na wielolinijkowe teksty
print(names)

msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
print(msg)#drukowanie tekstu z apostrofem i cudzysłowem, używając znaków ucieczki
print(quote)
print(msg + " " + quote) #łączenie tekstów za pomocą operatora +
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
print(msg)#drukowanie tekstu z apostrofem i cudzysłowem, używając znaków ucieczki
print(quote)
print("a" in msg) #sprawdzenie czy znak "a" jest w tekście msg
print("z" in msg) #sprawdzenie czy znak "z" jest w tekście msg
print(len(msg)) #długość tekstu msg
print(msg.upper()) #zamiana tekstu msg na wielkie litery
print(msg.lower()) #zamiana tekstu msg na małe litery
print(msg.replace("sunny", "rainy")) #zamiana słowa "sunny" na "rainy" w tekście msg
print(msg.split()) #podzielenie tekstu msg na listę słów
print(msg.strip()) #usunięcie białych znaków z początku i końca tekstu msg
print(msg.startswith("It's")) #sprawdzenie czy tekst msg zaczyna się od "It's"
print(msg.endswith("day")) #sprawdzenie czy tekst msg kończy się na "day"
print(msg.find("sunny")) #znalezienie indeksu pierwszego wystąpienia słowa "sunny" w tekście msg
print(msg.count("a")) #zliczenie ile razy występuje znak "a" w tekście msg
print(msg.capitalize()) #zamiana pierwszej litery tekstu msg na wielką
print(msg.title()) #zamiana pierwszej litery każdego słowa w tekście msg na wielką
print(msg.isupper()) #sprawdzenie czy wszystkie litery w tekście msg są wielkie
print(msg.islower()) #sprawdzenie czy wszystkie litery w tekście msg są ma
list = ["apple", "banana", "cherry"]
print(", ".join(list)) #łączenie elementów listy w jeden tekst, oddzielając je przecinkiem i spacją
print(msg[1:4]) #wypisanie znaków od indeksu 1 do 3 (indeks 4 jest wyłączony)
print(msg[:5]) #wypisanie pierwszych 5 znaków
print(msg[5:10]) #wypisanie znaków od indeksu 5 do 9
print(msg[-4:]) #wypisanie ostatnich 4 znaków
print(msg[0:11:2]) #wypisanie co drugiego znaku od indeksu 0 do 10
print(msg[::-1]) #odwrócenie tekstu msg
int_var = 42
name = "Alice"
print(name + str(int_var)) #łączenie tekstu z liczbą, trzeba zamienić liczbę na tekst za pomocą str()
print(f"{name} has {int_var} apples") #f-string pozwala na łatwe łączenie tekstu z wartościami zmiennych (nowoczesna alternatywa dla str.format())
