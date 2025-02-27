import csv

# Passenger Survival
class Passenger:
    def __init__(self, name, age, sex, passengerid, survived):
        self.name = name
        self.age = age
        self.sex = sex
        self.passengerid = passengerid
        self.survived = survived


class Titanic:
    def __init__(self):
        self.passengers = []

    def addPassenger(self, p):
        if p not in self.passengers:
            self.passengers.append(p)

    def averageAge(self):
        # To avoid division by 0:
        if len(self.passengers) == 0:
            return 0

        # Calculate the overall sum
        s = sum([passenger.age for passenger in self.passengers])
        # Return the average
        return s / len(self.passengers)


class Test_Titanic:
    def __init__(self, filename):
        self.filename = filename

        # Create a common Titanic object
        self.t = Titanic()

        # for test purpose
        self.count_len_file = 0

        with open(filename, 'r') as file:
            # Read the content. The delimiter is not necessary here
            passenger_reader = csv.reader(file)

            # Ignore the first part (the header)
            next(passenger_reader)

            for row in passenger_reader:
                # Keep track of how many rows the file has
                self.count_len_file += 1

                # Extract all the data
                ID = int(row[0])  # convert it into an integer
                Survived = int(row[1])
                # Pclass = int(row[2])
                Name = row[3]
                Sex = row[4]
                # ! The Age can be ''
                if row[5]:
                    Age = float(row[5])
                else:
                    Age = 0
                # SibSp = row[6]
                # Parch = row[7]
                # Ticket = int(row[8])
                # Fare = row[9]
                # Cabin = row[10]
                # Embarked = row[11]

                # Create a new passenger object for every person
                # Take only the name, age, sex, passengerid and survived
                person = Passenger(Name, Age, Sex, ID, Survived)
                self.t.addPassenger(person)


def test_addPassenger():
    class_test = Test_Titanic('passengers.csv')
    assert len(class_test.t.passengers) == class_test.count_len_file

def test_averageAge():
    # Create two passengers objects
    p1 = Passenger('p1', 10, 'male', 1, 1)
    p2 = Passenger('p2', 10, 'female', 1, 1)

    # Create a titanic object
    t = Titanic()
    t.addPassenger(p1)
    t.addPassenger(p2)

    assert t.averageAge() > 0
    assert t.averageAge() == 10
    # We can also test the case with age 0