class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_items(self):
        return ", ".join(self.items) if self.items else "No items"


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.abilities = []
        self.talents = []

    def describe(self):
        return (
            f"{self.name} is a {self.__class__.__name__} with abilities: {', '.join(self.abilities)} "
            f"and talents: {', '.join(self.talents)}. Inventory: {self.inventory.list_items()}."
        )


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name)
        self.abilities.extend(["Power Strike"])
        self.talents.extend(["Bravery"])


class Mage(Player):
    def __init__(self, name):
        super().__init__(name)
        self.abilities.extend(["Cast Spell"])
        self.talents.extend(["Arcane Knowledge"])


class Archer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.abilities.extend(["Precise Shot"])
        self.talents.extend(["Sharpshooter"])




