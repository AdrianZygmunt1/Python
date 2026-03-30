#zmienne
x = 5
y = 10
print(x + y)
imie = "Jan"
print("Cześć, " + imie + "!")
#zmienne mogą być różnego typu
wiek = 25
print("Mam " + str(wiek) + " lat.")
#zmienne mogą być nadpisywane
wiek = 30
print("Mam " + str(wiek) + " lat.")
float_var = 3.14
print("Liczba Pi to " + str(float_var))
#zmienne mogą być używane do przechowywania wyników obliczeń
a = 10
b = 20
c = a + b
print("Wynik dodawania to " + str(c))
char_var = 'A'
print("Pierwsza litera alfabetu to " + char_var)
#Jezyk python jest dynamicznie typowany, więc możemy przypisać różne typy danych do tej samej zmiennej
zmienna = 42
print("Zmienna ma wartość: " + str(zmienna))
zmienna = "Teraz jestem tekstem"
print("Zmienna ma wartość: " + zmienna+"\n")
#wszytkie typy danych w Pythonie
my_int = 10 #liczba całkowita
my_float = 3.14 #liczba zmiennoprzecinkowa
my_str = "Hello, World!" #łańcuch znaków
my_bool = True #wartość logiczna
my_set = {1, 'B', 3} #zbiór
my_dict = {"key1": "value1", "key2": "value2"} #słownik
my_tuple = (1, "B", 3) #krotka
my_range = range(5) #zakres
my_list = [1, 2, 3, "A", "B", "C"] #lista
my_none = None #brak wartości
print("Integer: " + str(my_int))
print("Float: " + str(my_float))
print("String: " + my_str)
print("Boolean: " + str(my_bool))
print("Set: " + str(my_set))
print("Dictionary: " + str(my_dict))
print("Tuple: " + str(my_tuple))
print("Range: " + str(my_range))
print("List: " + str(my_list))
print("None: " + str(my_none))
#sprawdzenie typu danych
print(type(my_int)) #int
print(type(my_float)) #float
print(type(my_str)) #str
print(type(my_bool)) #bool
print(type(my_set)) #set
print(type(my_dict)) #dict
print(type(my_tuple)) #tuple
print(type(my_range)) #range
print(type(my_list)) #list
print(type(my_none)) #NoneType
#isinstance - sprawdzenie czy zmienna jest określonego typu
print(isinstance(my_int, int)) #True
print(isinstance(my_float, float)) #True
print(isinstance(my_str, int)) #false
