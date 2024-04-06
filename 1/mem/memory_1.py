from dataclasses import dataclass
from sys import getsizeof
from pydantic import BaseModel

# Обычный класс
class RegularClass:
    # __slots__ = ["name" , "value"]
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

class RegularClassSlots:
    __slots__ = ["name" , "value" , "dict"]

    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value
        self.dict = {}





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
regular_instance_slots = RegularClassSlots("regular", 1)
dataclass_simple_instance = DataClassSimple("dataclass_simple", 2)
dataclass_slots_instance = DataClassWithSlots("dataclass_slots", 3)
pydantic_instance = PydanticModel(name="pydantic", value=4)

regular_instance.new_data = 123
# regular_instance_slots.new_data = 123
# print(regular_instance.__dict__)
print(regular_instance_slots.__dir__())
print(regular_instance.__dir__())

print(f"Regular Class: {getsizeof(regular_instance)} bytes")
print(f"DataClass without slots: {getsizeof(dataclass_simple_instance)} bytes")
print(f"DataClass with slots: {getsizeof(dataclass_slots_instance)} bytes")
print(f"Pydantic Model: {getsizeof(pydantic_instance)} bytes")
