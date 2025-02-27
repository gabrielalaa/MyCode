class Vehicle:
    # Class attribute
    color = 'white'

    # CONSTRUCTOR with default seating capacity
    def __init__(self, seating_capacity = None):
        self.seating_capacity = seating_capacity

        self.fare_charge = 0

    # METHOD to calculate fare
    def fare(self):
        self.fare_charge = self.seating_capacity * 100
        return self.fare_charge


class Bus(Vehicle):
    # CONSTRUCTOR for Bus with default seating capacity of 50
    def __init__(self):
        super().__init__(50)
        self.fare()  # Calculate the fare with maintenance

    # Overriding the fare method
    def fare(self):
        base_fare = super().fare()
        # Add 10% maintenance
        self.fare_charge = base_fare + (0.10 * base_fare)
        return self.fare_charge


class Car(Vehicle):
    # CONSTRUCTOR for Car with default seating capacity of 5
    def __init__(self):
        super().__init__(5)
        super().fare()

# Create instances of Bus and Car
b = Bus()
print(f"Bus Seating Capacity: {b.seating_capacity}")
print(f"Bus Color: {b.color}")
print(f"Bus Fare: {b.fare_charge}")

c = Car()
print(f"Car Seating Capacity: {c.seating_capacity}")
print(f"Car Color: {c.color}")
print(f"Car Fare: {c.fare_charge}")