class Newspaper:
    def __init__(self, name):
        # Hide it:
        self.__name = name
        # __ -> ment to be private
        # by default, all are public


n1 = Newspaper('Times')

# Convention __ to protect
# It renames the var. internally
# print(n1.__name)
# Now I can access the name:
# print(n1._Newspaper__name)

# print(n1.__dict__)
# {'_Newspaper__name': 'Times'}

########################################

class Exam:
    def __init__(self, name):
        self.name = name

        self.__participants = []

    def addParticipant(self, std):
        self.__participants.append(std)


e1 = Exam("")
e1.addParticipant('Kretes')
print(e1.name)
# print(e1.__participants)  # Error