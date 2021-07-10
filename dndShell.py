import cmd
# import yaml


class Strength:
    def __init__(self, **kwargs) -> None:
        self.raw : int
        self.saving : int
        self.athletics : int


class Dexterity:
    def __init__(self, **kwargs) -> None:
        self.raw : int
        self.saving : int
        self.acrobatics : int
        self.sleight_of_hand : int
        self.stealth : int


class Constitution:
    def __init__(self, **kwargs) -> None:
        self.raw : int
        self.saving : int


class Intelligence:
    def __init__(self, **kwargs) -> None:
        self.raw : int
        self.saving : int
        self.arcana : int
        self.history : int
        self.investigation : int
        self.nature : int
        self.religion : int


class Wisdom:
    def __init__(self, **kwargs) -> None:
        self.raw : int
        self.saving : int
        self.animal_handling : int
        self.insight : int
        self.medicine : int
        self.perception : int
        self.survival : int


class Charisma:
    def __init__(self, **kwargs) -> None:
        self.raw : int
        self.saving : int
        self.deception : int
        self.intimidation : int
        self.performance : int
        self.persuasion : int


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
        pass

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
