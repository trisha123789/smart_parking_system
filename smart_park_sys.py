#----------------SMART PARKING SYSTEM PROJECT---------
from abc import ABC, abstractmethod


class Vehicle:
    def __init__(self, vehicle_id, license_plate, owner_name):
        self.__license_plate = license_plate 
        self.__owner_name = owner_name         
        self.vehicle_id = vehicle_id

    
    def get_license_plate(self):
        return self.__license_plate

    def get_owner_name(self):
        return self.__owner_name

    
    def display(self):
        print(f"ID: {self.vehicle_id}, Plate: {self.__license_plate}, Owner: {self.__owner_name}")

    def calculate_parking_fee(self, hours):
        return 0


class Bike(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, helmet_required):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        super().display()
        print(f"Helmet Required: {self.helmet_required}")

    def calculate_parking_fee(self, hours):
        return hours * 20


class Car(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, seats):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.seats = seats

    def display(self):
        super().display()
        print(f"Seats: {self.seats}")

    def calculate_parking_fee(self, hours):
        return hours * 50


class SUV(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, four_wheel_drive):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        super().display()
        print(f"4WD: {self.four_wheel_drive}")

    def calculate_parking_fee(self, hours):
        return hours * 70


class Truck(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, max_load_capacity):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.max_load_capacity = max_load_capacity

    def display(self):
        super().display()
        print(f"Max Load Capacity: {self.max_load_capacity} Tons")

    def calculate_parking_fee(self, hours):
        return hours * 100



class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size   
        self.__is_occupied = False
        self.vehicle = None

    def assign_vehicle(self, vehicle):
        if not self.__is_occupied:
            self.__is_occupied = True
            self.vehicle = vehicle
            return True
        return False

    def remove_vehicle(self):
        if self.__is_occupied:
            self.__is_occupied = False
            v = self.vehicle
            self.vehicle = None
            return v
        return None

    def is_available(self):
        return not self.__is_occupied

    def show_status(self):
        if self.__is_occupied:
            print(f"Spot {self.spot_id} ({self.size}): Occupied → {type(self.vehicle).__name__} ({self.vehicle.get_license_plate()})")
        else:
            print(f"Spot {self.spot_id} ({self.size}): Empty")


class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def show_spots(self):
        print("\nParking Status:")
        for spot in self.spots:
            spot.show_status()

    def park_vehicle(self, vehicle):
        size_map = {"Bike": "S", "Car": "M", "SUV": "L", "Truck": "XL"}
        required_size = size_map[type(vehicle).__name__]

        for spot in self.spots:
            if spot.size in ["S", "M", "L", "XL"]: 
                if required_size == spot.size and spot.is_available():
                    spot.assign_vehicle(vehicle)
                    print(f"{type(vehicle).__name__} ({vehicle.get_license_plate()}) parked in Spot {spot.spot_id}")
                    return True
        print(f"No available spot for {type(vehicle).__name__}")
        return False

    def unpark_vehicle(self, vehicle, hours, payment_method):
        for spot in self.spots:
            if spot.vehicle == vehicle:
                removed = spot.remove_vehicle()
                fee = removed.calculate_parking_fee(hours)
                print(f"{type(vehicle).__name__} ({vehicle.get_license_plate()}) removed from Spot {spot.spot_id}")
                print(f"Parking Fee = ₹{fee}")
                payment_method.process_payment(fee)
                return True
        print("Vehicle not found in lot")
        return False



class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using Cash")


class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using Card")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using UPI")




lot = ParkingLot("CityMall Parking")
lot.add_spot(ParkingSpot(1, "S"))
lot.add_spot(ParkingSpot(2, "M"))
lot.add_spot(ParkingSpot(3, "M"))
lot.add_spot(ParkingSpot(4, "L"))
lot.add_spot(ParkingSpot(5, "XL"))

print(f"Parking Lot Created: {lot.name} | Total Spots Added: {len(lot.spots)}")


bike1 = Bike("B101", "TS01AB1234", "Trisha", True)
car1 = Car("C201", "TS05CD5678", "Priya", 5)
suv1 = SUV("S30+1", "TS09EF9012", "Anjali", True)
truck1 = Truck("T401", "AP11XY4455", "Ravi", 12)

    
lot.park_vehicle(bike1)
lot.park_vehicle(car1)
lot.park_vehicle(suv1)
lot.park_vehicle(truck1)
lot.show_spots()

    
print("\n---- Unparking ----")
lot.unpark_vehicle(car1, hours=3, payment_method=UPIPayment())
lot.show_spots()
