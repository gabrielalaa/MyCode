# Create class attributes
class Newspaper:
    count = 0
    # always IMC
    # exists on the level of the classes
    publisher = 'IMC'

    def __init__(self, name):
        self.name = name
        Newspaper.count += 1

    def read(self):
        print(self.name)

    # Only part of the class
    # cls - points to the class
    # decorator:
    @classmethod
    def getNewspaperCount(cls):
        print(cls)
        return Newspaper.count


n1 = Newspaper('Times')
n1.read()
Newspaper('Times')
Newspaper('Times')
Newspaper('Times')
Newspaper('Times')

n2 = Newspaper('Times 2')
n2.read()

print(Newspaper.count)  # 06

print(Newspaper.getNewspaperCount())