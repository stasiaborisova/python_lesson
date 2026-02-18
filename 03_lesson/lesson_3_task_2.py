from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 14", "+79123456701"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79123456702"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79123456703"))
catalog.append(Smartphone("Google", "Pixel 7", "+79123456704"))
catalog.append(Smartphone("Huawei", "P50", "+79123456705"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")