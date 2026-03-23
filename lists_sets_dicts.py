#fruits. append, remove, insert, sort, reverse, clear, index, count and pop
#sets zijn zowat hetzelfde maar het heeft geen volgorde
#keys zijn de countries hier en values de capitals

fruits = ["apple", "banana", "orange", "strawberry"]

print(fruits[0])
print(len(fruits))
print("pineapple" in fruits)

fruits[0] = "pineapple"

for fruit in fruits:
    print(fruit)

capitals = {"USA": "Washington D.C.", "India": "New Delhi", "China": "Beijing", "Russia": "Moscow"}

if capitals.get(input("name a country")):
    print("This country is in the dictionary")
else:
    print("This country isnt in the dictionary")

capitals.update({"Germany": "Berlin"})

print(capitals)

for key in capitals.keys():
    print(key)

for value in capitals.values():
    print(value)