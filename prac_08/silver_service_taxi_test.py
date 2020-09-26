from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi_car = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi_car.drive(18)
    print(taxi_car)
    print(taxi_car.get_fare())

main()