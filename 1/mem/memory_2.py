from pympler import asizeof
from dataclasses import dataclass
from pydantic import BaseModel


# Обычный класс
class RegularClass:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value


# Класс с использованием dataclasses без __slots__
@dataclass
class DataClassSimple:
    name: str
    value: int


# Класс с использованием dataclasses и __slots__
@dataclass(slots=True)
class DataClassWithSlots:
    name: str
    value: int

# Модель Pydantic


class PydanticModel(BaseModel):
    name: str
    value: int


regular_instance = RegularClass("regular", 1)
dataclass_simple_instance = DataClassSimple("dataclass_simple", 2)
dataclass_slots_instance = DataClassWithSlots("dataclass_slots", 3)
pydantic_instance = PydanticModel(name="pydantic", value=4)

print(f"Regular Class: {asizeof.asizeof(regular_instance)} bytes")
print(f"DataClass without slots: {asizeof.asizeof(dataclass_simple_instance)} bytes")
print(f"DataClass with slots: {asizeof.asizeof(dataclass_slots_instance)} bytes")
print(f"Pydantic Model: {asizeof.asizeof(pydantic_instance)} bytes")
