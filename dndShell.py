import cmd
from random import randint
# import yaml


class Ability:
    def __init__(self, **data) -> None:
        for attr, value in data.items():
            setattr(self, attr, value)


class Strength:
    def __init__(self, **kwargs) -> None:
        self.raw = 0
        self.saving = 0
        self.athletics = 0


class Dexterity:
    def __init__(self, **kwargs) -> None:
        self.raw = 0
        self.saving = 0
        self.acrobatics = 0
        self.sleight_of_hand = 0
        self.stealth = 0


class Constitution:
    def __init__(self, **kwargs) -> None:
        self.raw = 0
        self.saving = 0


class Intelligence:
    def __init__(self, **kwargs) -> None:
        self.raw = 0
        self.saving = 0
        self.arcana = 0
        self.history = 0
        self.investigation = 0
        self.nature = 0
        self.religion = 0


class Wisdom:
    def __init__(self, **kwargs) -> None:
        self.raw = 0
        self.saving = 0
        self.animal_handling = 0
        self.insight = 0
        self.medicine = 0
        self.perception = 0
        self.survival = 0


class Charisma:
    def __init__(self, **kwargs) -> None:
        self.raw = 0
        self.saving = 0
        self.deception = 0
        self.intimidation = 0
        self.performance = 0
        self.persuasion = 0


class Player:
    def __init__(self, filepath: str) -> None:
        self.strength = Strength()
        self.dexterity = Dexterity()
        self.constitution = Constitution()
        self.intelligence = Intelligence()
        self.wisdom = Wisdom()
        self.charisma = Charisma()


class dndShell(cmd.Cmd):      
    # Grammar: (<skill> | <ability>) ("-", ("c" | "s"), [[" -"], ("a" | "d")])
    # `deception -ca`, skill check with advantage
    # `charisma -s -d`, raw ability saving throw with disadvantage
    # `insight -c`, skill check
    intro = "Welcome to the DnD shell! Type help or ? to list commands.\n"
    prompt = "(DnD) "
    advantage = False
    disadvantage = False
    check = True
    saving = False

    def dice(self, num_sides, num_dice=1):
        return [randint(1, num_sides) for _ in range(num_dice)]

    def precmd(self, line) -> None:
        """Strip args"""
        args = line.split()
        # set advantage or disadvantage
        # set ability check or saving throw
        # return
        pass

    def postcmd(self, line: str, stop=False) -> bool:
        """Reset state"""
        self.advantage = False
        self.disadvantage = False
        self.check = True
        self.saving = False
        return stop

    def roll(self, ability, advantage, disadvantage):
        rolls = [self.dice(20) for _ in range(1 + (advantage ^ disadvantage))]
        if (not advantage) and disadvantage:
            raw_roll = min(rolls)
        else:
            raw_roll = max(rolls)
        return raw_roll + (ability // 2) - 5

    def do_strength(self):
        self.strength.raw
        self.strength.saving
        pass

    def do_dexterity(self):
        self.dexterity.raw
        self.dexterity.saving
        pass

    def do_constitution(self):
        self.constitution.raw
        self.constitution.saving
        pass

    def do_intelligence(self):
        self.intelligence.raw
        self.intelligence.saving
        pass

    def do_wisdom(self):
        self.wisdom.raw
        self.wisdom.saving
        pass

    def do_charisma(self):
        self.charisma.raw
        self.charisma.saving
        pass

    def do_athletics(self):
        pass

    def do_acrobatics(self):
        pass

    def do_sleight_of_hand(self):
        pass

    def do_stealth(self):
        pass

    def do_arcana(self):
        pass

    def do_history(self):
        pass

    def do_investigation(self):
        pass

    def do_nature(self):
        pass

    def do_religion(self):
        pass

    def do_animal_handling(self):
        pass

    def do_insight(self):
        pass

    def do_medicine(self):
        pass

    def do_perception(self):
        pass

    def do_survival(self):
        pass

    def do_deception(self):
        pass

    def do_intimidation(self):
        pass

    def do_performance(self):
        pass

    def do_persuasion(self):
        pass
