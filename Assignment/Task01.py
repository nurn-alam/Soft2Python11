class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        Publication.__init__(self, name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print("Book Name:", self.name)
        print("Author:", self.author)
        print("Page Count:", self.page_count, "pages")
        print("------------------------")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        Publication.__init__(self, name)
        self.chief_editor = chief_editor

    def print_information(self):
        print("Magazine Name:", self.name)
        print("Chief Editor:", self.chief_editor)
        print("------------------------")

donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
compartment_no6 = Book("Compartment No. 6", "Rosa Liksom", 192)

donald_duck.print_information()
compartment_no6.print_information()
