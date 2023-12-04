import periodictable

Atomic_No = int(input("Enter Element Atomic number: "))
element = periodictable.elements[Atomic_No]

print("Atomic number: ", element.number)
print("Symbol: ", element.symbol)
print("Name: ", element.name)
print("Atomic mass: ", element.mass)
print("Density: ", element.density)
