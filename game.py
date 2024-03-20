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