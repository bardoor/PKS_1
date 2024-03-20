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

    def use_ability(self, ability: Ability, target: Creature) -> None:
        if ability in self.__abilities:
            ability.use(target)

    def show_abilities(self) -> str:
        if len(self.__abilities) == 0:
            return "<<У Героя нет способностей"
        result = ""
        for i in range(len(self.__abilities)):
            result += f"<<{i + 1}){self.__abilities[i]}\n"
        return result

    def get_abilities(self) -> list[Ability]:
        return self.__abilities

    def __str__(self) -> str:
        return f"Герой {self._name} с {self._hp} hp и с силой: {self._strength}"


class Game:
    __hero: Hero
    __monsters: list[Monster]

    def __init__(self) -> None:
        hero_abilities = [DamageAbility("Чихнуть", 10), 
                          HealAbility("О! Пирожок в кармане :)", 20), 
                          BuffAbility("СДАЙ ЕГЭ! Ты сейчас возьмешь и сдашь ЕГЭ!", 3), 
                          DebuffAbility("Ты всего лишь часть исполняемого кода!", 0.5)]
        self.__hero = Hero(name="Поликарп Незыблемый", abilities=hero_abilities)
        self.__monsters = [Monster("Худющий гоблин", 10, 1), Monster("Старый дракон", 100, 3), Monster("Мощнейший комар", 150, 10)]

    def game_loop(self) -> None:
        game_end = False

        print(f"<<{self.__hero} - готов к путешествию!")

        while not game_end:
            player_choice = input(
            "<<Перед вами развилка. Куда идти?\n"
            "<<1)Направо\n"
            "<<2)Налево\n"
            "<<3)Прямо\n"
            ">>")
            if player_choice not in ('1', '2', '3'):
                print("<<Ну раз не хочешь выбирать...")
                print("<<Тогда пойдем " + random.choice(('направо', 'налево', 'прямо')))

            if random.randint(0, 1) == 1:
                monster = random.choice(self.__monsters)
                print(f"<<Перед вами {monster}\n")
                self.__battle(monster)
                if not monster.is_alive():
                    self.__monsters.remove(monster)
            else:
                print("<<Никого нет!\n")

            game_end = self.is_game_end()

        if self.__hero.is_alive():
            print("<<Вы победили!")
        else:
            print("<<Вы проиграли!")

    def is_game_end(self) -> bool:
        return len(self.__monsters) == 0 or not self.__hero.is_alive()
    
    def __battle(self, monster: Monster) -> None:
        while self.__hero.is_alive() and monster.is_alive():
            print(f"<<У {self.__hero.get_name()} осталось {self.__hero.get_hp()} hp\n")
            if not(self.__hero_action(monster)):
                continue

            if not monster.is_alive():
                print(f"<<{monster.get_name()} убит!\n")
            else:
                print(f"<<У {monster.get_name()} осталось {monster.get_hp()} очков здоровья\n")
                self.__monster_action(monster)

    def __hero_action(self, monster: Monster) -> bool:
        action_choice = input("<<1)Удар \n<<2)Способность\n>>")

        if action_choice == '1':
            self.__hero.hit(monster)
            print("<<Неплохой удар!")
        elif action_choice == '2':
            hero_abilities = self.__hero.get_abilities()
            if len(hero_abilities) == 0:
                print("<<У героя нет способностей")
                return False
            ability_choice = input(f"{self.__hero.show_abilities()}>>")
            if not(ability_choice.isdigit()):
                print("<<Вы можете ввести только целое число, попробуйте еще раз")
                return False
            ability_choice = int(ability_choice)
            if ability_choice > len(hero_abilities) or ability_choice == 0:
                print("<<Вы не можете ввести это число, попробуйте еще раз")
                return False
            ability = hero_abilities[ability_choice - 1]
            if isinstance(ability, DamageAbility) or isinstance(ability, DebuffAbility):
                self.__hero.use_ability(ability, monster)
            elif isinstance(ability, HealAbility) or isinstance(ability, BuffAbility):
                self.__hero.use_ability(ability, self.__hero)
            print(f"<<Успешная активация способности: ({ability})")
        else:
            print("<<Нет такого варианта, попробуйте еще раз")
            return False
        return True
    
    def __monster_action(self, monster: Monster) -> None:
        hp_before_hit = self.__hero.get_hp()
        monster.hit(self.__hero)
        print(f"<<{monster.get_name()} ударил {self.__hero.get_name()} и нанёс {hp_before_hit - self.__hero.get_hp()} урона\n")


if __name__ == "__main__":
    game = Game()
    game.game_loop()