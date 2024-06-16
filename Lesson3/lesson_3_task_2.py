from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79111234567"),
    Smartphone("Samsung", "Galaxy S23", "+79221234567"),
    Smartphone("Google", "Pixel 6", "+79331234567"),
    Smartphone("OnePlus", "9 Pro", "+79441234567"),
    Smartphone("Xiaomi", "Mi 11", "+79551234567")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")