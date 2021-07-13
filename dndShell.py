import cmd
import sys
from random import randint
import yaml


class BaseAbility:
    def __init__(self, raw: int, saving: int) -> None:
        self.raw = raw
        self.saving = saving
    
    def __str__(self):
        return "\n".join(f"    {k}: {v}" for k, v in self.__dict__.items())


class Strength(BaseAbility):
    def __init__(self, *, raw: int,
                          saving: int,
                          athletics: int) -> None:
        super().__init__(raw, saving)
        self.athletics = athletics


class Dexterity(BaseAbility):
    def __init__(self, *, raw: int,
                          saving: int,
                          acrobatics: int,
                          sleight_of_hand: int,
                          stealth: int) -> None:
        super().__init__(raw, saving)
        self.acrobatics = acrobatics
        self.sleight_of_hand = sleight_of_hand
        self.stealth = stealth


class Constitution(BaseAbility):
    def __init__(self, *, raw: int, saving: int) -> None:
        super().__init__(raw, saving)


class Intelligence(BaseAbility):
    def __init__(self, *, raw: int,
                          saving: int,
                          arcana: int,
                          history: int,
                          investigation: int,
                          nature: int,
                          religion: int) -> None:
        super().__init__(raw, saving)
        self.arcana = arcana
        self.history = history
        self.investigation = investigation
        self.nature = nature
        self.religion = religion


class Wisdom(BaseAbility):
    def __init__(self, *, raw: int,
                          saving: int,
                          animal_handling: int,
                          insight: int,
                          medicine: int,
                          perception: int,
                          survival: int) -> None:
        super().__init__(raw, saving)
        self.animal_handling = animal_handling
        self.insight = insight
        self.medicine = medicine
        self.perception = perception
        self.survival = survival


class Charisma(BaseAbility):
    def __init__(self, *, raw: int,
                          saving: int,
                          deception: int,
                          intimidation: int,
                          performance: int,
                          persuasion: int) -> None:
        super().__init__(raw, saving)
        self.deception = deception
        self.intimidation = intimidation
        self.performance = performance
        self.persuasion = persuasion


class dndShell(cmd.Cmd):      
    # Grammar: (<skill> | <ability>) ("-", ("c" | "s"), [[" -"], ("a" | "d")])
    # `deception -ca`, skill check with advantage
    # `charisma -s -d`, raw ability saving throw with disadvantage
    # `insight -c`, skill check
    intro = "Welcome to the DnD shell! Type help or ? to list commands.\n"
    prompt = "(DnD) > "
    adv = False
    disadv = False
    check = True
    saving = False

    def dice(self, num_sides, num_dice=1):
        return [randint(1, num_sides) for _ in range(num_dice)]

    def precmd(self, line) -> None:
        """Strip args"""
        args = line.split()
        self.adv = "-a" in args
        self.disadv = "-d" in args
        self.saving = "-s" in args
        self.check = "-c" in args or not self.saving

        if args[0] != "display":
            print(f"rolling: {args[0]}" + " saving throw"*self.saving
                                        + " check"*self.check
                                        + " with advantage"*self.adv
                                        + " with disadvantage"*self.disadv)
        return args[0]

    def roll(self, ability):
        rolls = self.dice(20, 1 + (self.adv ^ self.disadv))
        result = min(rolls) if ((not self.adv) and self.disadv) else max(rolls)
        modifier = (ability // 2) - 5
        print(f"raw ability score: {ability}")
        print(f"modifier: " + "+"*(modifier >= 0) + f"{modifier}")
        print(f"dice rolls: {rolls}")
        print(f"raw result: {result}")
        if result == 20:
            print("\nnat 20!!!\n")
        if result == 1:
            print("\nnat 1!!!\n")
        print(f"result with modifier: {result + modifier}\n")

    def do_display(self, args):
        print(self)

    def do_strength(self, args):
        if self.check:
            return self.roll(self.strength.raw)
        return self.roll(self.strength.saving)

    def do_dexterity(self, args):
        if self.check:
            return self.roll(self.dexterity.raw)
        return self.roll(self.dexterity.saving)

    def do_constitution(self, args):
        if self.check:
            return self.roll(self.constitution.raw)
        return self.roll(self.constitution.saving)

    def do_intelligence(self, args):
        if self.check:
            return self.roll(self.intelligence.raw)
        return self.roll(self.intelligence.saving)

    def do_wisdom(self, args):
        if self.check:
            return self.roll(self.wisdom.raw)
        return self.roll(self.wisdom.saving)

    def do_charisma(self, args):
        if self.check:
            return self.roll(self.charisma.raw)
        return self.roll(self.charisma.saving)

    def do_athletics(self, args):
        return self.roll(self.strength.athletics)

    def do_acrobatics(self, args):
        return self.roll(self.dexterity.acrobatics)

    def do_sleight_of_hand(self, args):
        return self.roll(self.dexterity.sleight_of_hand)

    def do_stealth(self, args):
        return self.roll(self.dexterity.stealth)

    def do_arcana(self, args):
        return self.roll(self.intelligence.arcana)

    def do_history(self, args):
        return self.roll(self.intelligence.history)

    def do_investigation(self, args):
        return self.roll(self.intelligence.investigation)

    def do_nature(self, args):
        return self.roll(self.intelligence.nature)

    def do_religion(self, args):
        return self.roll(self.intelligence.religion)

    def do_animal_handling(self, args):
        return self.roll(self.wisdom.animal_handling)

    def do_insight(self, args):
        return self.roll(self.wisdom.insight)

    def do_medicine(self, args):
        return self.roll(self.wisdom.medicine)

    def do_perception(self, args):
        return self.roll(self.wisdom.perception)

    def do_survival(self, args):
        return self.roll(self.wisdom.survival)

    def do_deception(self, args):
        return self.roll(self.charisma.deception)

    def do_intimidation(self, args):
        return self.roll(self.charisma.intimidation)

    def do_performance(self, args):
        return self.roll(self.charisma.performance)

    def do_persuasion(self, args):
        return self.roll(self.charisma.persuasion)


class Player(dndShell):
    def __init__(self, filepath: str) -> None:
        with open(filepath, "r") as player_file:
            player_data = yaml.safe_load(player_file.read())
        super().__init__()
        self.strength = Strength(**player_data["strength"])
        self.dexterity = Dexterity(**player_data["dexterity"])
        self.constitution = Constitution(**player_data["constitution"])
        self.intelligence = Intelligence(**player_data["intelligence"])
        self.wisdom = Wisdom(**player_data["wisdom"])
        self.charisma = Charisma(**player_data["charisma"])
        self.cmdloop()

    def __str__(self):
        return "\n".join(f"\n{k}:\n{v}" for k, v in self.__dict__.items())


if __name__ == "__main__":
    try:
        filepath = sys.argv[1]
    except IndexError:
        print("No filepath given!")
        quit

    Player(filepath)
