# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

import sys
sys.path.insert(0, "C:/Users/georg/first_project/venv/Seminar10")
from Task5 import Birds, Reptiles, Fishes


class AnimalFabric:
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def _get_maker(self, animal_type: str):
        types = {"bird": Birds, "reptile": Reptiles, "fish": Fishes}
        return types[animal_type.lower()]


if __name__ == '__main__':
    fabric = AnimalFabric()
    animal_from_fabric = fabric.make_animal("bird", "Gosha", "Parrot")
    animal_from_fabric.commands = ["sing", "talk"]
    print(animal_from_fabric)
    print(* animal_from_fabric.commands)
