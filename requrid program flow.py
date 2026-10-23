from abc import ABC, abstractmethod


# STEP 1: Passenger base class (Abstraction)
class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass


# STEP 2: Passenger types (Inheritance and Polymorphism)
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0


class StudentPassenger(Passenger):
    def get_discount(self):
        return 10


# STEP 3: Flight class
class Flight:
    def __init__(self, code, airline, source, destination, seats, base_fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.__seats = seats
        self.base_fare = base_fare

    @property
    def seats(self):
        return self.__seats

    def reserve_seats(self, count):
        if count <= self.__seats:
            self.__seats -= count
            return True
        return False

    def display_flight(self):
        print(
            f"{self.code} | {self.airline} | "
            f"{self.source} to {self.destination} | "
            f"Seats: {self.seats} | Fare: Rs.{self.base_fare}"
        )


# STEP 4: Booking class
class Booking:
    def __init__(self, booking_id, passenger, flight, tickets,
                 base_total, discount, final_fare):
        self.booking_id = booking_id
        self.passenger = passenger
        self.flight = flight
        self.tickets = tickets
        self.base_total = base_total
        self.discount = discount
        self.final_fare = final_fare

    def display_summary(self):
        print("\n===== BOOKING SUMMARY =====")
        print("Booking ID:", self.booking_id)
        print("Passenger:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Flight:", self.flight.code)
        print("Airline:", self.flight.airline)
        print("Route:", self.flight.source, "to", self.flight.destination)
        print("Tickets:", self.tickets)
        print("Base Fare: Rs.", self.base_total)
        print("Discount:", self.discount, "%")
        print("Final Fare: Rs.", self.final_fare)


# STEP 5: Flight Booking System
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("AI101", "Air India", "Nagpur", "Mumbai", 20, 3000),
            Flight("6E202", "IndiGo", "Nagpur", "Delhi", 15, 4500),
            Flight("UK303", "Vistara", "Mumbai", "Bangalore", 10, 5000)
        ]
        self.bookings = []
        self.booking_count = 0

    def view_flights(self):
        print("\n===== AVAILABLE FLIGHTS =====")
        for flight in self.flights:
            flight.display_flight()

    def book_flight(self):
        self.view_flights()

        code = input("Enter flight code: ").strip().upper()
        flight = next(
            (f for f in self.flights if f.code == code), None
        )

        if flight is None:
            print("Error: Invalid flight code!")
            return

        name = input("Enter passenger name: ").strip()
        if not name:
            print("Error: Passenger name cannot be empty!")
            return

        try:
            age = int(input("Enter passenger age: "))
            tickets = int(input("Enter number of tickets: "))
        except ValueError:
            print("Error: Age and tickets must be numbers!")
            return

        if age < 1 or age > 120:
            print("Error: Invalid age!")
            return

        if tickets < 1:
            print("Error: Ticket count must be at least 1!")
            return

        if tickets > flight.seats:
            print("Error: Not enough available seats!")
            return

        print("1. Regular Passenger")
        print("2. Student Passenger")
        category = input("Select passenger category: ").strip()

        if category == "1":
            passenger = RegularPassenger(name, age)
        elif category == "2":
            passenger = StudentPassenger(name, age)
        else:
            print("Error: Invalid passenger category!")
            return

        # Calculate fare
        base_total = flight.base_fare * tickets
        discount = passenger.get_discount()
        discount_amount = base_total * discount / 100
        final_fare = base_total - discount_amount

        # Confirm booking after validation
        if not flight.reserve_seats(tickets):
            print("Error: Seats are no longer available!")
            return

        self.booking_count += 1
        booking = Booking(
            f"BK{self.booking_count}",
            passenger, flight, tickets,
            base_total, discount, final_fare
        )

        self.bookings.append(booking)
        print("\nBooking successful!")
        booking.display_summary()

    # STEP 6: View most recent booking
    def view_booking(self):
        if not self.bookings:
            print("No booking found. Please book a flight first.")
        else:
            self.bookings[-1].display_summary()

    # STEP 7: Main menu and exit
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
                print("Invalid choice! Please select 1 to 4.")


# Run the application
if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()
        