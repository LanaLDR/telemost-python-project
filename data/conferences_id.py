import dataclasses


@dataclasses.dataclass
class Ids:
    correct_number: str
    invalid_number: str
    invalid_not_int_number: str

ids = Ids(
    correct_number = "2285230217",
    invalid_number = "1233141331315",
    invalid_not_int_number = "qwertyyqewry"
)

