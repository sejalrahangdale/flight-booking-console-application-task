#flight booking application
from abc import ABC, abstractmethod


# Base class for passengers
class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass


# Regular passenger class
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0


# Student passenger class
class StudentPassenger(Passenger):
    def get_discount(self):
        return 10


# Flight class
class Flight:
    def __init__(self, code, airline, source, destination,
                 seats, base_fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.seats = seats
        self.base_fare = base_fare

    def display_flight(self):
        print(
            f"{self.code} | {self.airline} | "
            f"{self.source} to {self.destination} | "
            f"Seats: {self.seats} | Fare: Rs.{self.base_fare}"
        )


# Booking class
class Booking:
    def __init__(self, booking_id, passenger, flight, tickets, total_fare):
        self.booking_id = booking_id
        self.passenger = passenger
        self.flight = flight
        self.tickets = tickets
        self.total_fare = total_fare

    def display_summary(self):
        print("\n----- BOOKING SUMMARY -----")
        print("Booking ID:", self.booking_id)
        print("Passenger:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Flight:", self.flight.code)
        print("Route:", self.flight.source, "to", self.flight.destination)
        print("Tickets:", self.tickets)
        print("Total Fare: Rs.", self.total_fare)


# Main flight booking system
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("AI101", "Air India", "Nagpur", "Mumbai", 20, 3000),
            Flight("6E202", "IndiGo", "Nagpur", "Delhi", 15, 4500),
            Flight("UK303", "Vistara", "Mumbai", "Bangalore", 10, 5000)
        ]
        self.booking = None
        self.booking_count = 0

    def view_flights(self):
        print("\n----- AVAILABLE FLIGHTS -----")
        for flight in self.flights:
            flight.display_flight()

    def book_flight(self):
        self.view_flights()

        code = input("\nEnter flight code: ").strip().upper()
        selected_flight = None

        for flight in self.flights:
            if flight.code == code:
                selected_flight = flight
                break

        if selected_flight is None:
            print("Error: Invalid flight code.")
            return

        if selected_flight.seats <= 0:
            print("Sorry, no seats available.")
            return

        name = input("Enter passenger name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return

        try:
            age = int(input("Enter passenger age: "))
            tickets = int(input("Enter number of tickets: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            return

        if age <= 0 or age > 120:
            print("Error: Enter a valid age.")
            return

        if tickets <= 0 or tickets > selected_flight.seats:
            print("Error: Invalid ticket count or insufficient seats.")
            return

        category = input(
            "Passenger category (1. Regular, 2. Student): "
        ).strip()

        if category == "1":
            passenger = RegularPassenger(name, age)
        elif category == "2":
            passenger = StudentPassenger(name, age)
        else:
            print("Error: Invalid passenger category.")
            return

        base_total = selected_flight.base_fare * tickets
        discount = passenger.get_discount()
        discount_amount = base_total * discount / 100
        final_fare = base_total - discount_amount

        self.booking_count += 1
        booking_id = "BK" + str(self.booking_count)

        booking = Booking(
            booking_id, passenger, selected_flight,
            tickets, final_fare
        )

        # Confirm booking only after all validations
        selected_flight.seats -= tickets
        self.booking = booking

        print("\nBooking successful!")
        print("Base Fare: Rs.", base_total)
        print("Discount: ", discount, "%")
        print("Discount Amount: Rs.", discount_amount)
        booking.display_summary()

    def view_booking(self):
        if self.booking is None:
            print("\nNo booking found. Please book a flight first.")
        else:
            self.booking.display_summary()

    def run(self):
        while True:
            print("\n===== FLIGHT BOOKING SYSTEM =====")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.view_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Flight Booking System!")
                break
            else:
                print("Invalid choice. Please select 1 to 4.")


# Program execution
if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()