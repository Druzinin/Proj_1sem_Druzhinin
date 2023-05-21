# Вариант 27

class Automobile:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


class Truck(Automobile):

    def __init__(self, brand, model, year, cargo_capacity):
        super().__init__(brand, model, year)
        self.cargo_capacity = cargo_capacity

    def carry_cargo(self):
        print("This truck can carry", self.cargo_capacity, "tons of cargo.")


class Car(Automobile):

    def __init__(self, brand, model, year, num_passengers):
        super().__init__(brand, model, year)
        self.num_passengers = num_passengers

    def carry_passengers(self):
        print("This car can carry", self.num_passengers, "passengers.")


# создание объектов классов Truck и PassengerCar
truck = Truck("Volvo", "FH16", 2022, 20)
passenger_car = Car("Tesla", "Model S", 2022, 5)

# вызов методов класса Truck
print(truck.brand)
print(truck.model)
print(truck.year)
truck.carry_cargo()
print()

# вызов методов класса PassengerCar
print(passenger_car.brand)
print(passenger_car.model)
print(passenger_car.year)
passenger_car.carry_passengers()
