# Operatory logiczne w Pythonie
print(3>4) # False
print(5<10) # True
print(7>=7) # True
print(2<=1) # False
print(3==3) # True
print(4!=4) # False
if 5 > 3:# warunek jest prawdziwy, więc kod wewnątrz bloku if zostanie wykonany
    print("5 jest większe niż 3")
    
if 5==5:
    pass # instrukcja pass jest używana jako placeholder, nie wykonuje żadnej akcji

if 10 < 5:
    print("10 jest mniejsze niż 5")
else:    
    print("10 nie jest mniejsze niż 5") # ten blok else zostanie wykonany, ponieważ warunek if jest fałszywy


if 8 > 10:
    print("8 jest większe niż 10")
elif 8 == 10:
    print("8 jest równe 10")# ten blok elif zostanie pominięty, ponieważ warunek if jest fałszywy, a 8 nie jest równe 10
else:
    print("8 jest mniejsze niż 10") # ten blok else zostanie wykonany, ponieważ oba poprzednie warunki są fałszywe


#Fałszywe wartości w Pythonie: False, None, 0, 0.0, ''.
print(bool(False)) # False
print(bool(None)) # False
print(bool(0)) # False
print(bool(0.0)) # False
print(bool('')) # False
print(bool(1)) # True
print(bool(-1)) # True
print(bool('Hello')) # True

# Operatory logiczne: and, or, not
print(True and False) # False
print(True or False) # True
print(not True) # False
print(not False) # True
if 5 > 3 and 2 < 4:
    print("Oba warunki są prawdziwe") # ten blok if zostanie wykonany, ponieważ oba warunki są prawdziwe
if 5 > 3 or 2 > 4:
    print("Przynajmniej jeden z warunków jest prawdziwy") # ten blok if zostanie wykonany, ponieważ pierwszy warunek jest prawdziwy