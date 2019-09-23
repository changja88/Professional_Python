from abc import *


class Character():
    def __init__(self):
        self.hp = 100
        self.attack_power = 20

    def attack(self, other, attack_kind):
        other.get_damage(self.attack_power, attack_kind)

    @abstractmethod
    def get_damage(self, attack_power, attack_kind):
        pass


class Player(Character):
    pass


print('a')

# ABCMeta 클래스
# - Base 클래스를 상속 받는 파생 클래스가 반드시 Base 클래스의 메서드를 명시적으로 선언해서 구현하도록 강제하는 추상화 클래스 이다
