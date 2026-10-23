from abc import ABC, abstractmethod


# 1. Passenger Base Class - Abstraction
class Passenger(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    @abstractmethod
    def get_discount(self):
        pass

    @abstractmethod
    def get_type(self):
        pass


# 2. Inheritance
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0

    def get_type(self):
        return "Regular"


class StudentPassenger(Passenger):
    def get_discount(self):
        return 10

    def get_type(self):
        return "Student"


# 3. Flight Class
class Flight:
    def __init__(self, code, source, destination, seats, fare):
        self.__code = code
        self.__source = source
        self.__destination = destination
        self.__seats = seats
        self.__fare = fare

    def get_code(self):
        return self.__code

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def get_seats(self):
        return self.__seats

    def get_fare(self):
        return self.__fare

    def display(self):
        print(
            f"{self.__code} | {self.__source} to "
            f"{self.__destination} | Seats: {self.__seats} | "
            f"Fare: Rs.{self.__fare}"
        )

    def book_seats(self, count):
        if count > 0 and count <= self.__seats:
            self.__seats -= count
            return True
        return False


# 4. Booking Class
class Booking:
    def __init__(self, booking_id, passenger, flight, tickets):
        self.booking_id = booking_id
        self.passenger = passenger
        self.flight = flight
        self.tickets = tickets

        self.base_fare = flight.get_fare() * tickets
        self.discount_percent = passenger.get_discount()
        self.discount_amount = (
            self.base_fare * self.discount_percent / 100
        )
        self.final_amount = self.base_fare - self.discount_amount

    def display(self):
        print("\nBooking confirmed!")
        print("Booking ID:", self.booking_id)
        print(
            "Flight:",
            self.flight.get_code(),
            "|",
            self.flight.get_source(),
            "to",
            self.flight.get_destination()
        )
        print("Passenger:", self.passenger.get_name())
        print("Passenger type:", self.passenger.get_type())
        print("Age:", self.passenger.get_age())
        print("Tickets:", self.tickets)
        print("Base fare per ticket: Rs.", self.flight.get_fare())
        print("Subtotal: Rs.", self.base_fare)
        print(
            f"{self.passenger.get_type()} discount "
            f"({self.discount_percent}%): Rs.{self.discount_amount:.2f}"
        )
        print("Final amount: Rs.", f"{self.final_amount:.2f}")


# 5. Flight Booking System
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Pune", "Delhi", 20, 4000),
            Flight("PN102", "Mumbai", "Bengaluru", 30, 5000),
            Flight("PN103", "Pune", "Hyderabad", 25, 3500)
        ]

        self.bookings = []
        self.booking_counter = 1001

    def view_flights(self):
        print("\n===== AVAILABLE FLIGHTS =====")
        for flight in self.flights:
            flight.display()

    def find_flight(self, code):
        for flight in self.flights:
            if flight.get_code().lower() == code.lower():
                return flight
        return None

    def book_flight(self):
        self.view_flights()

        code = input("\nEnter flight code: ").strip()
        flight = self.find_flight(code)

        if flight is None:
            print("Booking failed: Invalid flight code.")
            print("No booking was created. Available seats unchanged.")
            return

        name = input("Enter passenger name: ").strip()
        age_text = input("Enter age: ").strip()
        passenger_type = input(
            "Passenger type (Regular/Student): "
        ).strip().lower()
        tickets_text = input("Enter number of tickets: ").strip()

        # Validate all input before booking
        if name == "":
            print("Booking failed: Passenger name cannot be blank.")
            return

        if not age_text.isdigit() or int(age_text) <= 0:
            print("Booking failed: Age must be greater than 0.")
            return

        if not tickets_text.isdigit() or int(tickets_text) <= 0:
            print("Booking failed: Ticket count must be greater than 0.")
            return

        if passenger_type not in ("regular", "student"):
            print("Booking failed: Invalid passenger type.")
            return

        age = int(age_text)
        tickets = int(tickets_text)

        # Check seat availability before changing seats
        if tickets > flight.get_seats():
            print("Booking failed: Not enough seats available.")
            print("No booking was created. Available seats remain unchanged.")
            return

        # Create passenger object
        if passenger_type == "student":
            passenger = StudentPassenger(name, age)
        else:
            passenger = RegularPassenger(name, age)

        # Create booking details
        booking = Booking(
            self.booking_counter,
            passenger,
            flight,
            tickets
        )

        # Change seats only after validation succeeds
        if flight.book_seats(tickets):
            self.bookings.append(booking)
            self.booking_counter += 1
            booking.display()
        else:
            print("Booking failed: Seats unavailable.")

    def view_booking(self):
        if len(self.bookings) == 0:
            print("No booking exists.")
            return

        self.bookings[-1].display()

    def run(self):
        print("Welcome to Kiran Air Booking!")

        while True:
            print("\n1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.view_flights()

            elif choice == "2":
                self.book_flight()

            elif choice == "3":
                self.view_booking()

            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, 3 or 4.")


# Main Program
if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()