def function(name, age):
    print("Fijne verjaardag " + name)
    print("Je wordt " + str(age) + " jaar oud")

function("Djano", 16)
function("Jan", 6)

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("djano", "eijk")
print(full_name)

#modules zijn preset functions en variabelen die je kunt gebruiken
#je kunt ze gebruiken door import te doen (soms met een nickname of met from als je iets specifieks wilt)

print(help("modules"))