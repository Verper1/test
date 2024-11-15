class Vehicle:
    make = '1'
    model = '2'

    @classmethod
    def get_info(cls):
        return cls.make, cls.model


class Car(Vehicle):
    fuel_type = '3'

    @classmethod
    def get_info(cls):
        return cls.make, cls.model, cls.fuel_type


v = Vehicle()
print(v.get_info())

volvo = Car()
print(volvo.get_info())
