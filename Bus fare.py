class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def __init__(self, capacity=50):
        super().__init__(capacity)
    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 0.10
        return total_fare + maintenance_charge
bus = Bus(50)
print("Total Bus fare:", bus.fare())