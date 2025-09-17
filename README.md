# smart_parking_system
🅿️ Smart Parking System Project

A Python-based Object-Oriented Parking System that manages vehicles, parking spots, and payments.
This project demonstrates OOP concepts like inheritance, abstraction, encapsulation, and polymorphism along with real-world features like parking fee calculation and multiple payment methods.

🚀 Features

Support for multiple vehicle types:

🏍 Bike

🚗 Car

🚙 SUV

🚛 Truck

Encapsulated vehicle details (license plate, owner info).

Parking spots with sizes (S, M, L, XL).

Automatic vehicle-to-spot matching.

Fee calculation based on vehicle type and hours parked.

Multiple payment methods:

💵 Cash

💳 Card

📱 UPI

Live parking lot status (occupied/empty).

🛠 Tech Stack

Language: Python 3.x

Concepts Used:

Object-Oriented Programming (OOP)

Abstraction (abc module)

Encapsulation (__private_attributes)

Polymorphism & Method Overriding

📂 Project Structure
SmartParkingSystem/
│── smart_parking.py    # Main source code
│── README.md           # Documentation

▶️ How to Run

Clone the repository or download the script.

Run the program:

python smart_parking.py


Sample Output:

Parking Lot Created: CityMall Parking | Total Spots Added: 5
Bike (TS01AB1234) parked in Spot 1
Car (TS05CD5678) parked in Spot 2
SUV (TS09EF9012) parked in Spot 4
Truck (AP11XY4455) parked in Spot 5

Parking Status:
Spot 1 (S): Occupied → Bike (TS01AB1234)
Spot 2 (M): Occupied → Car (TS05CD5678)
Spot 3 (M): Empty
Spot 4 (L): Occupied → SUV (TS09EF9012)
Spot 5 (XL): Occupied → Truck (AP11XY4455)

---- Unparking ----
Car (TS05CD5678) removed from Spot 2
Parking Fee = ₹150
Paid ₹150 using UPI

📊 Parking Fee Rules
Vehicle Type	Fee (per hour)
Bike 🏍	₹20
Car 🚗	₹50
SUV 🚙	₹70
Truck 🚛	₹100
🧑‍💻 Concepts Demonstrated

Abstraction: Payment is an abstract base class.

Encapsulation: Vehicle details like __license_plate are private.

Inheritance: Bike, Car, SUV, and Truck inherit from Vehicle.

Polymorphism: Different calculate_parking_fee implementations per vehicle.

✨ Future Improvements

Add a GUI or Web Interface.

Store parking history in a database.

Implement dynamic pricing (peak hours, weekends).

Add QR-based ticketing system.

👩‍💻 Author

Trisha – 🚀 Engineer & Tech Enthusiast
