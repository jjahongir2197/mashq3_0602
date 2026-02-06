class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def hit(self, enemy):
        enemy.hp -= self.attack
        print(self.name, "zarba berdi:", self.attack)


class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 15)
        self.level = 1
        self.exp = 0

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.level += 1
            self.exp = 0
            self.hp += 20
            self.attack += 5
            print("LEVEL UP!")


class Enemy(Character):
    def __init__(self, name, hp, attack, exp):
        super().__init__(name, hp, attack)
        self.exp = exp


p = Player("Hero")
e = Enemy("Goblin", 50, 10, 40)

while p.hp > 0 and e.hp > 0:
    p.hit(e)
    if e.hp <= 0:
        p.gain_exp(e.exp)
        break
    e.hit(p)
