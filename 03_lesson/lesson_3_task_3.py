from address import Address
from mailing import Mailing

from_address = Address(
    index="101000",
    city="Москва",
    street="Тверская",
    house="1",
    apartment="10"
)

to_address = Address(
    index="190000",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="25",
    apartment="45"
)

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350,
    track="RA123456789RU"
)

print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, "
    f"{mailing.from_address.street}, "
    f"{mailing.from_address.house} - "
    f"{mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, "
    f"{mailing.to_address.city}, "
    f"{mailing.to_address.street}, "
    f"{mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)