from Address import Address

class Mailing:

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track} из {self.from_address} в {self.to_address}. "
                f"Стоимость {self.cost} рублей")
    
from_address = Address("123456", "Москва", "Ленина", "10", "101")
to_address = Address("654321", "Санкт-Петербург", "Невский", "20", "202")
mailing = Mailing(to_address, from_address, 500, "TRACK12345")
