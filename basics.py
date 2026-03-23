name = "Djano van Eijk"
age = int(input("Hoe oud is Djano"))
countdown = "321"

print("Hallo, mijn naam is " + name + " en ik ben " + str(age) + " jaar oud!")

if age >= 67:
    print("Oh my god bruh")

elif age >= 18:
    print("Djano is volwassene")

else:
    print("Djano is niet volwassene")

for x in range(0,6,2):
    print("looping")

for x in countdown:
    print(x)
