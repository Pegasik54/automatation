from Address import Address
from Mailing import Mailing

from_address = Address("630099", "Новосибирск", "Урицкого", "9", "123")
to_address = Address("620100", "Екатеринбург", "Куйбышева", "100", "321")

mailing = Mailing(to_address, from_address, 700, "TRACK909988")

print(f"Отправление {mailing.track} из {mailing.from_address} в {mailing.to_address}. "
      f"Стоимость {mailing.cost} рублей.")