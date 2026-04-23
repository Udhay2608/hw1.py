class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "240 km/h"


class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "350 km/h"


def show_details(car):
    print(car.fuel_type())
    print(car.max_speed())


b = BMW()
f = Ferrari()

show_details(b)
show_details(f)
