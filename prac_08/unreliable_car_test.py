
from prac_08.unreliable_car import UnreliableCar

new_car = UnreliableCar("Reliable", 100, 90)
old_car = UnreliableCar("Unreliable", 100, 10)


for i in range(10, 41, 10):
    print(f"Driving {i}km:")
    print(f"New car drove {new_car.drive(i)}km")
    print(f"Old car drove {old_car.drive(i)}km")

print(new_car)
print(old_car)
