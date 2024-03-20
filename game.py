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

    def take_heal(self, heal: int) -> None:
        if heal < 0:
            raise RuntimeError("Хил не может быть отрицательным")
        self._hp += heal

    def take_debuff(self, debuff_index: float) -> None:
        if debuff_index <= 0 or debuff_index > 1:
            raise RuntimeError("Дебафф не может быть баффом или быть отрицательным")
        self._strength *= debuff_index

    def take_buff(self, buff_index: float) -> None:
        if buff_index < 1:
            raise RuntimeError("Бафф не может быть дебаффом")
        self._strength *= buff_index

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
    

class HealAbility(Ability):
    __heal_points: int

    def __init__(self, name: str, heal_points: int) -> None:
        super().__init__(name)
        self.__heal_points = heal_points

    def use(self, ability_user: Creature) -> None:
        ability_user.take_heal(self.__heal_points)

    def __str__(self) -> str:
        return f"{self._name} - способность, исцеляет у владельца: {self.__heal_points} хп"


class DebuffAbility(Ability):
    __debuff_index: float

    def __init__(self, name: str, debuff_index: float) -> None:
        super().__init__(name)
        self.__debuff_index = debuff_index

    def use(self, enemy: Monster) -> None:
        enemy.take_debuff(self.__debuff_index)

    def __str__(self) -> str:
        return f"{self._name} - способность, позволяющая понизить силу врага, коэфф.: {self.__debuff_index}"
    

class BuffAbility(Ability):
    __buff_index: float

    def __init__(self, name: str, buff_index: float) -> None:
        super().__init__(name)
        self.__buff_index = buff_index

    def use(self, ability_user: Creature) -> None:
        ability_user.take_buff(self.__buff_index)

    def __str__(self) -> str:
        return f"{self._name} - способность, позволяющая увеличить силу владельца, коэфф.: {self.__buff_index}"


class Hero(Creature):
    __abilities: list[Ability]

    def __init__(self, name: str, hp: int=100, strength: int=5, abilities=None) -> None:
        super().__init__(name, hp, strength)
        if abilities is None:
            self.__abilities = []
        else:
            self.__abilities = abilities