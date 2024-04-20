class Item:
    def __init__(self):
        self.name = None
        self.description = None
        self.value = None

    def __str__(self):
        return f"{self.name}\n=====\n{self.description}\nValue: {self.value}"


class HealthPotion(Item):
    def __init__(self):
        self.name = "Health Potion"
        self.description = "A potion that heals you for 50 HP"
        self.value = 50

    def use(self):
        self.user.hp += self.value
        print(f"Your HP is now {self.user.hp}")


class ManaPotion(Item):
    def __init__(self):
        self.name = "Mana Potion"
        self.description = "A potion that restores 50 MP"
        self.value = 50

    def use(self):
        self.user.mp += self.value
        print(f"Your MP is now {self.user.mp}")


class Coin(Item):
    def __init__(self):
        self.name = "Coin"
        self.description = "A shiny coin"
        self.value = 1
