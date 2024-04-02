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

class Game:
    def __init__(self):
        hero_abilities = [Ability("Чихнуть", 10,1),
                          Ability("Ударить сильно прям", 20,1),
                          Ability("Плюнуть Кислоту", 30, 1),
                          Ability("Взрывная Волна от Прыжка", 20,1)]
        self.__hero = Hero(name="Поликарп Незыблемый", abilities=hero_abilities)
        self.__monsters = [Monster("Худющий гоблин", 10, 1),
                           Monster("Старый дракон", 100, 3),
                           Monster("Мощнейший комар", 150, 10)]

    def game_loop(self):
        game_end = False

        print(f"{self.__hero} готов к путешествию!")

        while not game_end:
            player_choice = int(input(
            "Перед вами развилка. Куда идти?\n"
            "1) Направо\n"
            "2) Налево\n"
            "3) Прямо\n"))

            if random.randint(0, 1) == 1:
                monster = random.choice(self.__monsters)
                print(f"Перед вами {monster}\n")
                self.__battle(monster)
                if not monster.is_alive():
                    self.__monsters.remove(monster)
            else:
                print("Монстра нет!\n")

            game_end = self.is_game_end()

        if self.__hero.is_alive():
            print("Вы победили!")
        else:
            print("Вы проиграли!")


    def is_game_end(self):
        return len(self.__monsters) == 0 or not self.__hero.is_alive()

    def __battle(self, monster: Monster):
        while self.__hero.is_alive() and monster.is_alive():
            print(f"У {self.__hero.get_name()} осталось {self.__hero.get_hp()} hp\n")
            self.__hero_action(monster)

            if not monster.is_alive():
                print(f"{monster.get_name()} убит!\n")
            else:
                print(f"У {monster.get_name()} осталось {monster.get_hp()} очков здоровья\n")
                self.__monster_action(monster)


    def __hero_action(self, monster, mana):
        action_choice = int(input("1) Удар \n2) Способность\n"))

        if action_choice == 1:
            self.__hero.hit(monster)
        else:
            if mana > 0:
                ability_choice = int(input((self.__hero.show_abilities())))
                hero_abilities = self.__hero.get_abilities()
                # Опасная операция...
                ability = hero_abilities[ability_choice - 1]
                self.__hero.use_ability(ability, monster)
                mana -= 1
            elif mana == 0 or mana < 0:
                return "У вас недостаточно Маны"

    def __monster_action(self, monster):
        hp_before_hit = self.__hero.get_hp()
        monster.hit(self.__hero)
        print(f"{monster.get_name()} ударил {self.__hero.get_name()} и нанёс {hp_before_hit - self.__hero.get_hp()} урона\n")
