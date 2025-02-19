import dataclasses


@dataclasses.dataclass
class Product:
    product_id: int
    quantity: int
    brand_id: int
    brand: str
    price: int


product_65292 = Product(
    product_id=100317,
    quantity=5,
    brand_id=1618,
    brand='Cesar',
    price=978)

product_66863 = Product(
    product_id=125006,
    quantity=3,
    brand_id=1419,
    brand='Royal Canin',
    price=1664)

