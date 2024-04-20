class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def list_items(self):
        return ", ".join(self.items) if self.items else "No items"


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.abilities = []
        self.talents = []
        self.health_points = 100
        self.mana_points = 100

    def describe(self):
        return (
            f"{self.name} is a {self.__class__.__name__} with abilities: {', '.join(self.abilities)} "
            f"and talents: {', '.join(self.talents)}. Inventory: {self.inventory.list_items()}."
        )


class WarriorClass(Player):
    def __init__(self, name):
        super().__init__(name)
        self.abilities.extend(["Power Strike"])
        self.talents.extend(["Bravery"])


class MageClass(Player):
    def __init__(self, name):
        super().__init__(name)
        self.abilities.extend(["Cast Spell"])
        self.talents.extend(["Arcane Knowledge"])


class ArcherClass(Player):
    def __init__(self, name):
        super().__init__(name)
        self.abilities.extend(["Precise Shot"])
        self.talents.extend(["Sharpshooter"])
