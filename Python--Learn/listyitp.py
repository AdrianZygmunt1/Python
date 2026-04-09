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
numbers = [2, 1, 3, 5, 4, 2.5]
sorted_numbers = sorted(numbers)# zwraca nową posortowaną listę zamiast modyfikować oryginalną listę
print(sorted_numbers)