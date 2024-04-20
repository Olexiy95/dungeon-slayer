import random
from dataclasses import dataclass


@dataclass
class MonsterBaseStats:
    health_points: int
    min_armour: int
    max_armour: int
    min_hit: int
    max_hit: int


class MonsterBaseClass:
    stats_list = ["health_points", "armour", "hit"]
    difficulty_scale = {"Easy": 0.8, "Normal": 1, "Hard": 1.5}

    def __init__(self, name: str, difficulty: str, base_stats: MonsterBaseStats):
        self.name = name
        self.difficulty = difficulty
        self.base_stats = base_stats
        self.health_points = (
            base_stats.health_points * self.difficulty_scale[difficulty]
        )
        self.armour = (
            random.randint(base_stats.min_armour, base_stats.max_armour)
            * self.difficulty_scale[difficulty]
        )
        self.hit = (
            random.randint(base_stats.min_hit, base_stats.max_hit)
            * self.difficulty_scale[difficulty]
        )
        self.abilities = []
        self.talents = []

    def describe_stats(self):
        return " ".join(f"{stat}: {getattr(self, stat)}" for stat in self.stats_list)

    @staticmethod
    def damage_received_calculation(incoming_damage: int, armour_value: int):
        damage_received = incoming_damage - armour_value
        return max(damage_received, 0)


class Goblin(MonsterBaseClass):
    def __init__(self, name: str, difficulty: str):
        base_stats = MonsterBaseStats(80, 0, 5, 8, 12)
        super().__init__(name, difficulty, base_stats)
        self.abilities.extend(["Bite"])
        self.talents.extend(["Stealth"])


class Skeleton(MonsterBaseClass):
    def __init__(self, name: str, difficulty: str):
        base_stats = MonsterBaseStats(100, 5, 10, 10, 15)
        super().__init__(name, difficulty, base_stats)
        self.abilities.extend(["Slash"])
        self.talents.extend(["Regeneration"])


class Troll(MonsterBaseClass):
    def __init__(self, name: str, difficulty: str):
        base_stats = MonsterBaseStats(120, 10, 15, 12, 18)
        super().__init__(name, difficulty, base_stats)
        self.abilities.extend(["Smash"])
        self.talents.extend(["Regeneration"])


class Orc(MonsterBaseClass):
    def __init__(self, name: str, difficulty: str):
        base_stats = MonsterBaseStats(150, 15, 20, 15, 22)
        super().__init__(name, difficulty, base_stats)
        self.abilities.extend(["Bash"])
        self.talents.extend(["Bravery"])


class Dragon(MonsterBaseClass):
    def __init__(self, name: str, difficulty: str):
        base_stats = MonsterBaseStats(200, 25, 50, 20, 30)
        super().__init__(name, difficulty, base_stats)
        self.abilities.extend(["Fire Breath"])
        self.talents.extend(["Flight"])
