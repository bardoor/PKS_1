from abc import ABC
import random
import os

class Creature(ABC):
    def __init__(self, name: str, hp: int, strength: int, mana: int):
        self._hp = hp
        self._strength = strength
        self._name = name
        self._mana = mana

    def hit(self, enemy: 'Creature'):
        enemy.take_damage(self._strength)

    def take_damage(self, damage: int):
        self._hp -= damage

    def get_hp(self):
        return self._hp

    def get_mana(self):
        return self._mana

    def get_name(self):
        return self._name

    def is_alive(self):
        return self._hp > 0

    def __str__(self):
        pass

class Monster(Creature):
    def __init__(self, name: str, hp=50, strength=1):
        super().__init__(name, hp, strength)

    def __str__(self):
        return f"Монстр {self._name} с {self._hp} hp и силой {self._strength}"


class Ability:
    def __init__(self, name: str, damage: int, mana: int):
        self.__name = name
        self.__damage = damage
        self.__mana = mana

    def __str__(self):
        return f"{self.__name} - наносит {self.__damage} урона"

    def use(self, target: Creature):
        if mana > 0:
            target.take_damage(self.__damage)
        else:
            return "У вас недостаточно Маны"

class Hero(Creature):
    mana: int
    def __init__(self, name: str, hp=100, strength=5, mana=10, abilities=None):
        super().__init__(name, hp, strength, mana)
        if abilities is None:
            self.__abilities = []
        else:
            self.__abilities = abilities

    def use_ability(self, ability: Ability, target: Creature, mana:int):
        if mana > 0 and ability in self.__abilities:
            ability.use(target)
        else:
            return "У вас недостаточно Маны"

    # Возвращает строку с перечислением способностей героя
    def show_abilities(self):
        result = ""
        for i in range(len(self.__abilities)):
            result += f"{i + 1}) {self.__abilities[i]}\n"
        return result

    # Возвращает список способностей героя
    def get_abilities(self):
        return self.__abilities

    def __str__(self):
        return f"Герой {self._name} с {self.get_hp()} hp"
