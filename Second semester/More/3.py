class InitializationFailed(Exception):
    pass

class ComplexNumber:
    def __init__(self,real,imaginary):
        self.a=real
        self.b=imaginary
        self.complex = 0

        # Conditions
        try:
            if isinstance(self.a, int) or isinstance(self.a, float):
                if isinstance(self.b, int) or isinstance(self.b, float):
                    if self.a == 0:
                        self.complex =  f'{self.b}i'
                    if self.b == 0:
                        self.complex = self.a
                    self.complex = f'{self.a} + {self.b}i'
        except InitializationFailed:
            print(InitializationFailed('Initialization Failed'))

    def __add__(self,other):
        return ComplexNumber(self.a+other.a,self.b+other.b)

    def __sub__(self,other):
        return ComplexNumber(self.a-other.a,self.b-other.b)

    def __mul__(self,other):
        return ComplexNumber(self.a*other.a,self.b*other.b)

    def __repr__(self):
        return f'{self.a} + {self.b}i'


#Test Code

# Valid complex number representations
print(str(ComplexNumber(2, -3))) # returns "2 - 3i"
print(str(ComplexNumber(3, 0))) # returns "3"
print(str(ComplexNumber(0, 5))) # returns "5i"

# # Invalid initializations
print(str(ComplexNumber('a', 2))) # returns "Initialization Failed"
print(str(ComplexNumber(3, [1]))) # returns "Initialization Failed"

# # Arithmetic operations
print(ComplexNumber(1, 1) + ComplexNumber(2, 3)) # returns ComplexNumber(3, 4) --> 3+4i
print(ComplexNumber(4, -2) - ComplexNumber(2, 3)) # returns ComplexNumber(2, -5) --> 2-5i
print(ComplexNumber(2, 3) * ComplexNumber(1, -4)) # returns ComplexNumber(14, -5) --> 1-4i