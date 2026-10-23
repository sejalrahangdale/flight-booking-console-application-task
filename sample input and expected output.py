class Flight:
    def __init__(self, code, source, destination, seats, fare):
        self.code = code
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare


class Passenger:
    def __init__(self, name, age, passenger_type):
        self.name = name
        self.age = age
        self.passenger_type = passenger_type

    def get_discount(self):
        if self.passenger_type.lower() == "student":
            return 10
        return 0


class Booking:
    def __init__(self, booking_id, flight, passenger, tickets):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets

        self.subtotal = flight.fare * tickets
        self.discount = (
            self.subtotal * passenger.get_discount() / 100
        )
        self.total = self.subtotal - self.discount

    def display(self):
        print("\nBooking confirmed!")
        print("Booking ID:", self.booking_id)
        print(
            "Flight:", self.flight.code, "|",
            self.flight.source, "to", self.flight.destination
        )
        print("Passenger:", self.passenger.name)
        print("Passenger type:", self.passenger.passenger_type)
        print("Tickets:", self.tickets)
        print("Base fare per ticket: Rs.", self.flight.fare)
        print("Subtotal: Rs.", self.subtotal)
        print(
            f"Student/Passenger discount "
            f"({self.passenger.get_discount()}%): "
            f"Rs.{self.discount:.0f}"
        )
        print(f"Final amount: Rs.{self.total:.0f}")


class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Pune", "Delhi", 20, 4000),
            Flight("PN102", "Mumbai", "Bengaluru", 30, 5000),
            Flight("PN103", "Pune", "Hyderabad", 25, 3500)
        ]
        self.bookings = []
        self.booking_number = 1001

    def view_flights(self):
        print("\nAvailable Flights:")
        for flight in self.flights:
            print(
                flight.code, "|", flight.source, "to",
                flight.destination, "| Seats:", flight.seats,
                "| Fare: Rs.", flight.fare
            )

    def book_flight(self):
        self.view_flights()

        code = input("\nEnter flight code: ").strip().upper()

        flight = None
        for item in self.flights:
            if item.code == code:
                flight = item
                break

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

        # Validate all details
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

        # Check seats before booking
        if tickets > flight.seats:
            print("Booking failed: Not enough seats available.")
            print("No booking was created. Available seats remain unchanged.")
            return

        passenger = Passenger(name, age, passenger_type)

        booking = Booking(
            "BK" + str(self.booking_number),
            flight,
            passenger,
            tickets
        )

        # Update seats only after validation
        flight.seats -= tickets
        self.bookings.append(booking)
        self.booking_number += 1

        booking.display()

    def view_booking(self):
        if not self.bookings:
            print("No booking exists.")
        else:
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
                print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()