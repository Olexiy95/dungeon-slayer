from player import WarriorClass, MageClass, ArcherClass
from monster import MonsterClass

warrior = WarriorClass("Aragorn")
mage = MageClass("Gandalf")
archer = ArcherClass("Legolas")
monster = MonsterClass("Dragon", "Hard")

# Describing each player
print(warrior.describe())
print(mage.describe())
print(archer.describe())
print(monster.describe_stats())
