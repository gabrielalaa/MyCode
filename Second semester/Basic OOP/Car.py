class Car:
    def __init__(self, numberplate):
        # # It is not wrong like this:
        # self.model = model
        # self.Year = Year
        # self.numberplate = numberplate
        self.model = None
        self.Year = None
        self.numberplate = numberplate

        self.owner = None

    # def set_owner(self, owner):
    #     self.owner = owner

    # String representation to that object
    def __str__(self):
        return f'{self.numberplate} and the owner is: {self.owner}'


class Customer:
    def __init__(self, name):
        self.ID = None
        self.name = name
        self.address = None

        self.cars = []
        self.agent = None
        self.insuranceCompany = None

    def add_car(self, car):
        self.cars.append(car)

    def agent(self, agent):
        self.agent = agent

    def insurance_company(self, comp):
        self.insuranceCompany = comp

    def __str__(self):
        return self.name


class Agent:
    def __init__(self, name):
        self.ID = None
        self.name = name
        self.address = None

        self.customers = []
        self.CarInsuranceCompany = None

    def add_customer_for_agent(self, c):
        self.customers.append(c)

    def add_car_for_agent(self, car):
        self.CarInsuranceCompany = car


class CarInsuranceCompany:
    def __init__(self, name):
        self.company_name = name

        # self.agents = []
        # self.customers = []

        self.customersForInsuranceCompany = []
        self.agentsForInsuranceCompany = []

    def add_agent(self, agent_insurance):
        self.agentsForInsuranceCompany.append(agent_insurance)

    def add_customer(self, customer_insurance):
        self.customersForInsuranceCompany.append(customer_insurance)


car1 = Car('W 12313 F')
p1 = Customer('Samuel Jackson')
company = CarInsuranceCompany("We ensure your safety")
a1 = Agent('Mark')
company.add_agent(a1)
company.add_customer(p1)

car1.owner = p1
# Print
print(car1)
# W 12313 F
