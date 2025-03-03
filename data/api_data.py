import dataclasses


@dataclasses.dataclass
class Product:
    product_id: int
    quantity: int
    brand_id: int
    brand: str
    price: int


product_120571_toys = Product(
    product_id=120571,
    quantity=1,
    brand_id=917262,
    brand="PETSHOP игрушки",
    price=194)

product_127000_toys = Product(
    product_id=127000,
    quantity=1,
    brand_id=787756,
    brand="PETSHOP",
    price=49)

