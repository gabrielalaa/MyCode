import json

class Address:
    def __init__(self, street: str, city: str, state: str, postalCode: int, country: str):
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country

    def __validate(self) -> bool:
        if not all([self.street, self.city, self.state, self.country]):
            return False
        if not isinstance(self.postalCode, int) or self.postalCode <= 0:
            return False
        return True

    def validate(self):
        return self.__validate()

    def outputAsLabel(self) -> str:
        if not self.__validate():
            return "Invalid Address"
        return f"Street {self.street}, City: {self.city}, State: {self.state}, Postal Code: {self.postalCode}, Country: {self.country}"


class Person:
    def __init__(self, name: str, phoneNumber: str, emailAddress: str):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.address = None
        self.parkingPass = False

    def purchaseParkingPass(self):
        self.parkingPass = True

    def lives_at(self, addr: Address):
        if not addr.validate():
            print("Invalid address provided!")
        else:
            self.address = addr


class Student(Person):
    def __init__(self, name: str, phoneNumber: str, emailAddress: str, studentNumber: int, averageMark: int):
        super().__init__(name, phoneNumber, emailAddress)
        self.studentNumber = studentNumber
        self.averageMark = averageMark
        self.professors = []
        self.seminars = []

    def isEligibleToEnroll(self) -> bool:
        return self.averageMark > 8

    def getSeminarsTaken(self) -> int:
        return len(self.seminars)

    def get_seminar(self, seminar_name, grade):
        if grade <= 4:
            self.seminars.append(seminar_name)


class Professor(Person):
    def __init__(self, name: str, phoneNumber: str, emailAddress: str, staffNumber: int, numberOfClasses: int, yearsOfService: int):
        super().__init__(name, phoneNumber, emailAddress)
        self._staffNumber = staffNumber
        self.numberOfClasses = numberOfClasses
        self.__yearsOfService = yearsOfService
        self.students = []

    @property
    def salary(self) -> int:
        return self._calculate_salary()

    def _calculate_salary(self) -> int:
        base_salary = 2000
        bonus = self.__yearsOfService * 1000
        return base_salary + bonus

    def supervises(self, student: Student):
        if len(student.professors) < 5 and self not in student.professors:
            student.professors.append(self)
            self.students.append(student)
        else:
            print(f"Student {student.name} has enough professors!")


# Custom JSON Encoder
class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Address):
            return obj.__dict__
        if isinstance(obj, Person):
            obj_dict = obj.__dict__.copy()
            obj_dict["__type__"] = obj.__class__.__name__
            return obj_dict
        return super().default(obj)


# Custom JSON Decoder
class PersonDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.person_convertor, *args, **kwargs)

    def person_convertor(self, jsonString):
        print("Got this to convert " + str(jsonString))
        if 'street' in jsonString:
            # Convert to Address
            return Address(jsonString['street'], jsonString['city'], jsonString['state'], jsonString['postalCode'], jsonString['country'])
        elif 'studentNumber' in jsonString:
            # Convert to Student
            return Student(jsonString['name'], jsonString['phoneNumber'], jsonString['emailAddress'], jsonString['studentNumber'], jsonString['averageMark'])
        elif '_staffNumber' in jsonString:
            # Convert to Professor, handling name mangling for __yearsOfService
            return Professor(
                jsonString['name'],
                jsonString['phoneNumber'],
                jsonString['emailAddress'],
                jsonString['_staffNumber'],
                jsonString['numberOfClasses'],
                jsonString['_Professor__yearsOfService']
            )
        return jsonString


# Example Usage
address = Address("123 Main St", "Springfield", "IL", 62704, "USA")
student1 = Student("Stefan", "012", "steph@gmail.com", 1, 9)
student2 = Student("Maria", "013", "maria@gmail.com", 2, 7)
professor1 = Professor("Matt", "1156", "matt@gmail.com", 2, 3, 2)

# Associate an address to all the persons
student1.lives_at(address)
student2.lives_at(address)
professor1.lives_at(address)

# Serialize objects to JSON
jsonString = json.dumps([professor1, student1, student2], cls=PersonEncoder)
print("Serialized JSON:", jsonString)

# Deserialize JSON back to objects
decoded_objects = json.loads(jsonString, cls=PersonDecoder)

print("Decoded Objects:")
for obj in decoded_objects:
    print(type(obj), obj.__dict__)