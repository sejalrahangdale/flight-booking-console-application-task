from abc import ABC, abstractmethod


# 1. ABSTRACTION
class Passenger(ABC):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Encapsulation: Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    @abstractmethod
    def get_discount(self):
        pass


# 2. INHERITANCE
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0


class StudentPassenger(Passenger):
    def get_discount(self):
        return 10


# 3. CLASS AND OBJECT
class Flight:
    def __init__(self, code, airline, source, destination, fare, seats):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.fare = fare
        self.__seats = seats

    def get_seats(self):
        return self.__seats

    def book_seats(self, tickets):
        if tickets > 0 and tickets <= self.__seats:
            self.__seats -= tickets
            return True
        return False

    def display_flight(self):
        print("\nFlight Code:", self.code)
        print("Airline:", self.airline)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print("Fare: Rs.", self.fare)
        print("Available Seats:", self.get_seats())


# 4. POLYMORPHISM
def calculate_fare(flight, passenger, tickets):
    base_fare = flight.fare * tickets
    discount_percent = passenger.get_discount()
    discount_amount = base_fare * discount_percent / 100
    final_fare = base_fare - discount_amount

    print("\n----- FARE DETAILS -----")
    print("Base Fare: Rs.", base_fare)
    print("Discount:", discount_percent, "%")
    print("Discount Amount: Rs.", discount_amount)
    print("Final Fare: Rs.", final_fare)

    return final_fare


# 5. BOOKING CLASS
class Booking:
    def __init__(self, booking_id, passenger, flight, tickets, total_fare):
        self.booking_id = booking_id
        self.passenger = passenger
        self.flight = flight
        self.tickets = tickets
        self.total_fare = total_fare

    def display_summary(self):
        print("\n===== BOOKING SUMMARY =====")
        print("Booking ID:", self.booking_id)
        print("Passenger Name:", self.passenger.get_name())
        print("Passenger Age:", self.passenger.get_age())
        print("Flight:", self.flight.code)
        print("Airline:", self.flight.airline)
        print("Route:", self.flight.source, "to", self.flight.destination)
        print("Tickets:", self.tickets)
        print("Total Fare: Rs.", self.total_fare)


# FLIGHT BOOKING SYSTEM
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("F101", "Air India", "Nagpur", "Mumbai", 3500, 50),
            Flight("F102", "IndiGo", "Nagpur", "Delhi", 5000, 40),
            Flight("F103", "Akasa Air", "Mumbai", "Pune", 2500, 30)
        ]
        self.bookings = []
        self.booking_id = 1001

    def view_flights(self):
        print("\n===== AVAILABLE FLIGHTS =====")
        for flight in self.flights:
            flight.display_flight()

    def book_flight(self):
        self.view_flights()

        code = input("\nEnter flight code: ").strip().upper()
        flight = None

        for item in self.flights:
            if item.code == code:
                flight = item
                break

        if flight is None:
            print("Error: Invalid flight code.")
            return

        name = input("Enter passenger name: ").strip()
        age_text = input("Enter passenger age: ").strip()
        tickets_text = input("Enter number of tickets: ").strip()

        if not name:
            print("Error: Name cannot be empty.")
            return

        if not age_text.isdigit() or int(age_text) <= 0:
            print("Error: Enter a valid age.")
            return

        if not tickets_text.isdigit() or int(tickets_text) <= 0:
            print("Error: Enter valid number of tickets.")
            return

        age = int(age_text)
        tickets = int(tickets_text)

        print("1. Regular Passenger")
        print("2. Student Passenger")
        category = input("Select passenger type: ").strip()

        if category == "1":
            passenger = RegularPassenger(name, age)
        elif category == "2":
            passenger = StudentPassenger(name, age)
        else:
            print("Error: Invalid passenger type.")
            return

        # Calculate fare before confirming
        total_fare = calculate_fare(flight, passenger, tickets)

        if tickets > flight.get_seats():
            print("Error: Not enough available seats.")
            return

        confirm = input("Confirm booking? (yes/no): ").strip().lower()

        if confirm != "yes":
            print("Booking cancelled.")
            return

        if not flight.book_seats(tickets):
            print("Booking failed: Seats unavailable.")
            return

        booking = Booking(
            self.booking_id, passenger, flight, tickets, total_fare
        )

        self.bookings.append(booking)
        self.booking_id += 1

        print("\nBooking successful!")
        booking.display_summary()

    def view_booking(self):
        if not self.bookings:
            print("No booking found.")
            return

        self.bookings[-1].display_summary()

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
                print("Invalid choice. Enter 1, 2, 3 or 4.")


# MAIN PROGRAM
if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()