from unreliable_car import UnreliableCar


def main():
    cars = [UnreliableCar('Car-01', 100, 100),
            UnreliableCar('Car-02', 100, 50),
            UnreliableCar('Car-03', 100, 0)]
    for car in cars:
        print(car)
        print(car.drive(99))
        print(car)
        print()


if __name__ == '__main__':
    main()
