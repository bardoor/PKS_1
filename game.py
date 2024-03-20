from abc import ABC
import random


class Creature(ABC):
    _name: str
    _hp: int
    _strength: int

    def __init__(self, name: str, hp: int, strength: int) -> None:
        self._name = name
        self._hp = hp
        self._strength = strength

    def hit(self, enemy: 'Creature') -> None:
        enemy.take_damage(self._strength)

    def take_damage(self, damage: int) -> None:
        if damage < 0:
            raise RuntimeError("Урон не может быть отрицательным")
        self._hp -= damage

    def get_hp(self) -> int:
        return self._hp

    def get_name(self) -> str:
        return self._name

    def is_alive(self) -> bool:
        return self._hp > 0
    
    def __str__(self) -> None:
        pass


class Monster(Creature):
    def __init__(self, name: str, hp: int=50, strength: int=1) -> None:
        super().__init__(name, hp, strength)

    def __str__(self) -> str:
        return f"Монстр {self._name} с {self._hp} hp и силой {self._strength}"
    

class Ability(ABC):
    _name: str

    def __init__(self, name: str) -> None:
        self._name = name

    def use(self) -> None:
        pass

    def __str__(self) -> None:
        pass


class DamageAbility(Ability):
    __damage: int

    def __init__(self, name: str, damage: int) -> None:
        super().__init__(name)
        self.__damage = damage

    def use(self, enemy: 'Monster') -> None:
        enemy.take_damage(self.__damage)

    def __str__(self) -> str:
        return f"{self._name} - способность, сносит у противника: {self.__damage} хп"