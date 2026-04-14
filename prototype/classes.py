class Menu:
    def __init__(self):
        self.notes = []

    def show_menu(self):
        while True:
            print("Notitie App")
            print("1. Notitie maken")
            print("2. Notitie bekijken")
            print("3. Notitie verwijderen")
            print("4. Notitie bewerken")
            print("5. Notitie opslaan")
            print("6. Afsluiten")
            answer = input("Wat wil je doen? (1-6)")
            self.answer_check(answer)

    def close_menu(self):
        print()
        print("Tot ziens!")
        print()
        exit()
        
    def answer_check(self, answer):
        if answer == "1":
            self.create_note()
        elif answer == "2":
            self.view_note()
        elif answer == "3":
            self.delete_note()
        elif answer == "4":
            self.edit_note()
        elif answer == "5":
            self.save_note()
        elif answer == "6":
            self.close_menu()
        else:
            print()
            print("Ongeldige keuze")
            print()
            self.show_menu()
    
    def create_note(self):
        print()
        print("Notitie maken")
        print()
        title = input("Titel: ")
        content = input("Inhoud: ")
        self.notes.append({"title": title, "content": content})
        print()
        print("Notitie " + title + " is gemaakt!")
        print()

    def view_note(self):
            if not self.notes:
                print()
                print("Er zijn nog geen notities.")
                print()
                self.show_menu()
            else:
                print()
                print("Alle notities:")
                for note in self.notes:
                    print(note["title"])
                print()
                title = input("Welke notitie wil je bekijken? ")
                found = False
                for note in self.notes:
                    if note["title"] == title:
                        print()
                        print(note["content"])
                        print()
                        found = True
                        self.show_menu()
                if not found:
                    print()
                    print("Deze notitie bestaat niet.")
                    print()
                    self.show_menu()

    def delete_note(self):
        if not self.notes:
            print()
            print("Er zijn nog geen notities.")
            print()
            self.show_menu()
        else:
            print()
            print("Alle notities:")
            for note in self.notes:
                print(note["title"])
            print()
            title = input("Welke notitie wil je verwijderen? ")
            found = False
            for note in self.notes:
                if note["title"] == title:
                    self.notes.remove(note)
                    print()
                    print("Notitie " + title + " is verwijderd!")
                    print()
                    found = True
                    self.show_menu()
            if not found:
                print()
                print("Deze notitie bestaat niet.")
                print()
                self.show_menu()

    def edit_note(self):
        if not self.notes:
            print()
            print("Er zijn nog geen notities.")
            print()
            self.show_menu()
        else:
            print()
            print("Alle notities:")
            for note in self.notes:
                print(note["title"])
            print()
            title = input("Welke notitie wil je bewerken? ")
            found = False
            for note in self.notes:
                if note["title"] == title:
                    new_content = input("Nieuwe inhoud: ")
                    note["content"] = new_content
                    print()
                    print("Notitie " + title + " is bijgewerkt!")
                    print()
                    found = True
                    self.show_menu()
            if not found:
                print()
                print("Deze notitie bestaat niet.")
                print()
                self.show_menu()

    def save_note(self):
        if not self.notes:
            print()
            print("Er zijn nog geen notities.")
            print()
            self.show_menu()
        else:
            print()
            print("Alle notities:")
            for note in self.notes:
                print(note["title"])
            print()
            title = input("Welke notitie wil je opslaan? ")
            found = False
            for note in self.notes:
                if note["title"] == title:
                    with open(title + ".txt", "w") as file:
                        file.write(note["content"])
                    print()
                    print("Notitie " + title + " is opgeslagen!")
                    print()
                    found = True
                    self.show_menu()
            if not found:
                print()
                print("Deze notitie bestaat niet.")
                print()
                self.show_menu()
