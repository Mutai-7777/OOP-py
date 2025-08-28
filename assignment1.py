# Class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")

    def info(self):
        return f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB"

# Inheritance Example
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    # Polymorphism: overriding info()
    def info(self):
        return f"Gaming Phone: {self.brand} {self.model}, {self.storage}GB with {self.cooling_system} cooling ❄️"


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S22", 128)
phone2 = GamingPhone("Asus", "ROG 6", 256, "Liquid Cooling")

print(phone1.info())
phone1.call("+254700123456")

print(phone2.info())
phone2.call("+254711987654")
