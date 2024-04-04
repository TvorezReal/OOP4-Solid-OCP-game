# Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle) в Разработке Простой Игры
# Цель: Цель этого домашнего задание - закрепить понимание и навыки применения принципа открытости/закрытости
# (Open/Closed Principle), одного из пяти SOLID принципов объектно-ориентированного программирования. Принцип гласит,
# что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.
# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия, не изменяя
# существующий код бойцов или механизм боя.
# Исходные данные:
# - Есть класс `Fighter`, представляющий бойца.
# - Есть класс `Monster`, представляющий монстра.
# - Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
# Шаг 1:Создайте абстрактный класс для оружия
# - Создайте абстрактный класс `Weapon`, который будет содержать абстрактный метод `attack()`.
# Шаг 2: Реализуйте конкретные типы оружия
# - Создайте несколько классов, унаследованных от `Weapon`, например, `Sword` и `Bow`. Каждый из этих классов реализует метод `attack()` своим уникальным способом.
# Шаг 3: Модифицируйте класс `Fighter`
# - Добавьте в класс `Fighter` поле, которое будет хранить объект класса `Weapon`.
# - Добавьте метод `changeWeapon()`, который позволяет изменить оружие бойца.
# Шаг 4: Реализация боя
# - Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
# Требования к заданию:
# - Код должен быть написан на Python.
# - Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко добавлять,
# не изменяя существующие классы бойцов и механизм боя.
# - Программа должна выводить результат боя в консоль.
# Пример результата:
# Боец выбирает меч.
# Боец наносит удар мечом.
# Монстр побежден!
# Боец выбирает лук.
# Боец наносит удар из лука.
# Монстр побежден!

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"


class Fighter:
    def __init__(self):
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon
        print(f"Боец выбирает {self.weapon.__class__.__name__}")

    def attack(self):
        if self.weapon is not None:
            return f"Боец {self.weapon.attack()}."
        else:
            return "Боец безоружен!"


class Monster:
    pass

# Реализация боя

def main():
    # Создание бойца и монстра
    fighter = Fighter()
    monster = Monster()

    # Бой с использованием меча
    fighter.changeWeapon(Sword())
    print(fighter.attack()) # Боец наносит удар мечом.
    print("Монстр побежден!")

    print("") # Для разделения вывода

    # Бой с использованием лука
    fighter.changeWeapon(Bow())
    print(fighter.attack()) # Боец наносит удар из лука.
    print("Монстр побежден!")


if __name__ == "__main__":
    main()