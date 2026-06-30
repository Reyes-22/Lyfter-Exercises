class Person():
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} gets on the bus.")
        else:
            print("The bus is full.")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} got off the bus.")
        else:
            print(f"{person.name} is not on the bus.")


my_bus = Bus(5)
person = Person("Bryan")

my_bus.add_passenger(person)
my_bus.remove_passenger(person)
