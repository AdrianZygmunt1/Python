cities = ['London','Tokyo','Los Angeles']
print(cities[0])#pierwszy elelment
print(cities[-1])#pobiera od tylu 
print(len(cities))#Wynik 3
cities[0]='Warsaw'#zmiana London na Warsaw
del cities[2]#kasuje element 3 z tablicy 
print('Warsaw' in cities)
print(cities)
name = "Jessica"
nameList = list(name)#Robie ze str liste J e s s ...
print(nameList)
Person = ['Max',20,['happy','nervous','sad']]#tablica w tablicy
print(Person[2][1])
nameR ,age ,mood = Person#Przypisawanie wartosci z listy do zmiennych 
print(nameR)
print(age)
print(mood)
nameR, *rest = Person #* przypisuje reszte z listy do zmiennej
print(nameR)
print(rest)
Color = ['Blue','Red','Black','Brown']
print(Color[0:len(Color)])#przedial calej listy 
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1::2])
numbers.append(7)# dodaje wartosc do tablicy
numery = [8,9,10]# zagniezdza cala liste 
numbers.append(numery)
numery1 = [11,12,13]
numbers.extend(numery1)#dzieki neij możesz dodać wiele elementów z jednej listy do drugiej
numbers.insert(2,2.5)#dodaje w dane miejsce
numbers.insert(2,2)
print(numbers)
numbers.remove(1)#ususwa wyznaczony elelment pierwszy dalsze juz nie
numbers.pop(1)#Aby usunąć element o określonym indeksie na liście
numbers.pop()#jesli pop bedzie puste to usunie ostatni element
print(numbers)
numbers.clear()#czysci szytko
print(numbers)
numbers = [2, 1, 3, 5, 4, 2.5]
numbers.sort()#sortuje elementy na miesjcu czyli w tej samej liscie
print(numbers)
numbers.reverse()#odwraca liste
print(numbers)
numbers = [2, 1, 3, 5, 4, 2.5]
sorted_numbers = sorted(numbers)# zwraca nową posortowaną listę zamiast modyfikować oryginalną listę
print(sorted_numbers)
Color = ['Blue','Red','Black','Brown']
print(Color.index('Black'))#łuży to do znalezienia pierwszego indeksu, w którym można znaleźć element na liście
developer = ('Alice', 34, 'Rust Developer')#Krotka zawiera mieszany zestwa typow
developer[1] # 34
numbers[-2] # 34
developer = 'Jessica'
tuple(developer) # ('J', 'e', 's', 's', 'i', 'c', 'a')
languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
'C++' in languages #True
developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']
print(languages[0:4])#wyznacza cala krotke
print(languages.count('C++'))#liczy ile jest takiego stringu
print(languages.index('Java'))#1
print(languages.index('Python', 3))#tu kazemy gdzie rozpocząć wyszukiwanie ciągu Python
print(languages.index('Python', 2, 5))
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
print(sorted(numbers))# [2, 3, 7, 13, 18, 45, 67, 78]
print(sorted(languages, key=len))#przykład użycia key argument do sortowania elementów w krotce według długości
#oglonie krotka jest stala nie mozna nia operowac jak lista jedynie odczytywac
