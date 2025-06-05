class Flight:
    def __init__(self, flight_number, origin, destination, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.capacity = capacity
        self.passengers = []

    def available_seats(self):
        return self.capacity - len(self.passengers)

    def book_seat(self, passenger_name):
        if self.available_seats() > 0:
            self.passengers.append(passenger_name)
            print(f"Seat booked for {passenger_name} on Flight {self.flight_number}.")
        else:
            print(f"Sorry, no seats available on Flight {self.flight_number}.")

    def cancel_booking(self, passenger_name):
        if passenger_name in self.passengers:
            self.passengers.remove(passenger_name)
            print(f"Booking canceled for {passenger_name} on Flight {self.flight_number}.")
        else:
            print(f"No booking found for {passenger_name} on Flight {self.flight_number}.")


class FlightReservationSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)
        print(f"Flight {flight.flight_number} added successfully.")

    def display_available_flights(self):
        if self.flights:
            print("\nAvailable Flights:")
            for flight in self.flights:
                print(f"Flight Number: {flight.flight_number}, Origin: {flight.origin}, Destination: {flight.destination}, Available Seats: {flight.available_seats()}")
        else:
            print("No flights available.")

    def book_seat(self, flight_number, passenger_name):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                flight.book_seat(passenger_name)
                return
        print(f"Flight {flight_number} not found.")

    def cancel_booking(self, flight_number, passenger_name):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                flight.cancel_booking(passenger_name)
                return
        print(f"Flight {flight_number} not found.")


def main():
    reservation_system = FlightReservationSystem()

    while True:
        print("\nFlight Reservation System Menu:")
        print("1. Add a flight")
        print("2. Display available flights")
        print("3. Book a seat")
        print("4. Cancel booking")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            flight_number = input("Enter flight number: ")
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            capacity = int(input("Enter capacity: "))
            flight = Flight(flight_number, origin, destination, capacity)
            reservation_system.add_flight(flight)
        elif choice == '2':
            reservation_system.display_available_flights()
        elif choice == '3':
            flight_number = input("Enter flight number: ")
            passenger_name = input("Enter passenger name: ")
            reservation_system.book_seat(flight_number, passenger_name)
        elif choice == '4':
            flight_number = input("Enter flight number: ")
            passenger_name = input("Enter passenger name: ")
            reservation_system.cancel_booking(flight_number, passenger_name)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
