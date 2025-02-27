# Example 1: Employee and Company
class Employee:
    def __init__(self, employee_name):
        self.employee_name = employee_name

        self.company = None


class Company:
    def __init__(self, company_name):
        self.company_name = company_name

        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        employee.company = self.company_name


# Example Usage
company = Company("TechCorp")
employee1 = Employee("Alice")
employee2 = Employee("Bob")

company.add_employee(employee1)
company.add_employee(employee2)


###


# Example 2: Administrative Assistant and Manager
class AdministrativeAssistant:
    def __init__(self, name):
        self.name = name

        self.supervisors = []


class Manager:
    def __init__(self, manager_name):
        self.manager_name = manager_name

        self.assistants = []

    def add_assistant(self, assistant):
        self.assistants.append(assistant)
        assistant.supervisors.append(self.manager_name)
        print(f"{assistant.name} is now assisting {self.manager_name}.")


# Exampl Usage
manager1 = Manager("Sarah")
manager2 = Manager("John")

assistant1 = AdministrativeAssistant("Emily")

manager1.add_assistant(assistant1)
manager2.add_assistant(assistant1)


###


# Example 3: Company and BoardOfDirectors
class Company:
    def __init__(self, company_name):
        self.company_name = company_name

        self.board = None

    def assign_board(self, board):
        self.board = board
        # board.company = self.company_name
        # or
        board.assign_company(self)


class BoardOfDirectors:
    def __init__(self, board_of_directors):
        self.board_of_directors = board_of_directors

        self.company = None

    def assign_company(self, c):
        self.company = c
        print(f"Board of Directors for {self.company.name} assigned.")


# Example Usage
company = Company("TechCorp")
board = BoardOfDirectors("TechCorp Board")

company.assign_board(board)


###


# Example 4: Office and Employee
class Office:
    def __init__(self, location):
        self.location = location

        self.employee = None  # one/zero employees assigned

    def allocate_to(self, employee):
        if self.employee is None:
            self.employee = employee
            print(f"Office at {self.location} allocated to {employee.name}.")
        else:
            print(f"Office at {self.location} is already allocated.")


# up:
# class Employee:
#     def __init__(self, employee_name):
#         self.employee_name = employee_name
#


# Example Usage
office = Office("5th Avenue")
employee = Employee("Alice")

office.allocate_to(employee)


###


# Example 5: Person and BoardOfDirectors
class Person:
    def __init__(self, name):
        self.name = name

        self.board_memberships = []  # List to hold multiple board memberships

    def join_board(self, b):
        if len(self.board_memberships) < 8:  # The limit
            self.board_memberships.append(b)
            b.members.append(self)
            print(f"{self.name} has joined the board of {b.name}.")
        else:
            print(f"{self.name} cannot join more than 8 boards.")


class BoardOfDirectors2:
    def __init__(self, name):
        self.name = name

        self.members = []


# Example Usage
person = Person("John")
board1 = BoardOfDirectors("TechCorp Board")
board2 = BoardOfDirectors("FinanceCo Board")

person.join_board(board1)
person.join_board(board2)