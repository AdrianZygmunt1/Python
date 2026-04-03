#+=, -=, *=, /= - operatory przypisania
num13 = 5
num13 += 2 # num13 = num13 + 2
print("num13 po dodaniu 2:", num13) # 7
num13 -= 3 # num13 = num13 - 3
print("num13 po odjęciu 3:", num13) # 4
num13 *= 4 # num13 = num13 * 4
print("num13 po mnożeniu przez 4:", num13) # 16
num13 /= 2 # num13 = num13 / 2
print("num13 po dzieleniu przez 2:", num13) # 8.0
#//= , %= ,**= ,- operator przypisania dzielenia całkowitego , reszty z dzielenia , potęgowania
num14 = 10
num14 //= 3 # num14 = num14 // 3                
print("num14 po dzieleniu całkowitym przez 3:", num14) # 3
num14 %= 3 # num14 = num14 % 3
print("num14 po podzieleniu przez 3:", num14) # 1
num14 **= 2 # num14 = num14 ** 2
print("num14 po potęgowaniu do 2:", num14) # 1  
#stringi również obsługują operatory przypisania
my_string = "Hello"
my_string += " World" # my_string = my_string + " World"
print("my_string po dodaniu ' World':", my_string) # "Hello World"
my_string *= 2 # my_string = my_string * 2
print("my_string po powtórzeniu 2 razy:", my_string) # "Hello WorldHello World"  