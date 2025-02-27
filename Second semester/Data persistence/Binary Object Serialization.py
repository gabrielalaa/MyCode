import pickle

# Define the Person class
class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

# Create an instance of a Person
p1 = Person("Matt")

# Define the file name for pickling/serialization/marshalling/flattening
filename = 'person.pkl'

# Serialize the object to a file
with open(filename, 'wb') as outfile:
    pickle.dump(p1, outfile)

# Deserialize the object from the file
with open(filename, 'rb') as infile:
    p2 = pickle.load(infile)

# Check if p1 and p2 are equal in content and identity
# ! This will be False without __eq__ method
print(f"p1 == p2? {p1 == p2}")  # This checks if the content is the same
print(f"p1 is p2 {p1 is p2}")  # This checks if they are the same object in memory