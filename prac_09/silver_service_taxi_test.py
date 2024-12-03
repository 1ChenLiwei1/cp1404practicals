from silver_service_taxi import SilverServiceTaxi

taxis = [SilverServiceTaxi('T-F1', 100, 1),
         SilverServiceTaxi('T-F3', 100, 3),]

for taxi in taxis:
    print(taxi)
    taxi.drive(60)
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")

    taxi.start_fare()
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")

    taxi.drive(18)
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")

    print(f"Remained fuel: {taxi.fuel}")
    print()