import cmd
import sys
from random import randint
import yaml


class Skill:
    def __init__(self, base: int, proficient: bool) -> None:
        self.base = base
        self.proficient = proficient

    @property
    def modifier(self):
        return self.base // 2 - 5

    def __str__(self):
        return "\n".join(f"    {k}: {v}" for k, v in self.__dict__.items())


class Ability(Skill):
    def __init__(self, base: int, saving: int, proficient: bool) -> None:
        super().__init__(base, proficient)
        self.saving = saving


class dndShell(cmd.Cmd):      
    intro = "Welcome to the DnD shell! Type help or ? to list commands.\n"
    prompt = "(DnD) > "
    advantage = False
    disadvantage = False
    verbose = False

    def precmd(self, line) -> None:
        """Strip args"""
        args = line.split()
        self.advantage = "-a" in args
        self.disadvantage = "-d" in args
        self.verbose = "-v" in args
        return " ".join(args[:2])
    
    def do_q(self, arg):
        """quit"""
        return 1

    def do_stats(self, arg):
        """show player stats"""
        print(self)
        return 0

    def do_check(self, arg):
        """check <ability or skill> (-a | -d) (-v)"""
        result = self.check(arg,
                            self.verbose,
                            self.advantage,
                            self.disadvantage)
        self.results(arg, "check", result, self.advantage, self.disadvantage)
        return 0

    def do_save(self, arg):
        """save <ability> (-a | -d) (-v)"""
        result = self.save(arg,
                           self.verbose,
                           self.advantage,
                           self.disadvantage)
        self.results(arg, "save", result, self.advantage, self.disadvantage)
        return 0

    def results(self, arg, roll_type, result, a, d):
        print(f"{arg} {roll_type}" \
              + (" with advantage"*a + " with disadvantage"*d)*(a ^ d) \
              + f": {result}")



class Player(dndShell):
    def __init__(self, filepath: str) -> None:
        with open(filepath, "r") as player_file:
            player_data = yaml.safe_load(player_file.read())

        self.name = player_data["name"]
        self.race = player_data["race"]
        self.occupation = player_data["class"]
        self.level = player_data["level"]
        self.hp = player_data["hp"]
        self.bonus = player_data["bonus"]

        for ability, stats in player_data.get("abilities").items():
            setattr(self, ability, Ability(**stats))
    
        for skill, stats in player_data.get("skills").items():
            setattr(self, skill, Skill(**stats))

        super().__init__()
        self.cmdloop()

    def check(self, attribute, verbose, advantage, disadvantage):
        attribute = getattr(self, attribute)
        modifier = attribute.modifier + self.bonus*attribute.proficient
        if verbose:
            self.verbose_roll(attribute.proficient,
                              self.bonus*attribute.proficient,
                              attribute.modifier,
                              modifier)
        return self.roll(verbose, advantage, disadvantage) + modifier

    def save(self, attribute, verbose, advantage, disadvantage):
        attribute = getattr(self, attribute)
        saving_bonus = attribute.saving // 2 - 5
        modifier = saving_bonus + self.bonus*attribute.proficient
        if verbose:
            self.verbose_roll(attribute.proficient,
                              self.bonus*attribute.proficient,
                              saving_bonus,
                              modifier)
        return self.roll(verbose, advantage, disadvantage) + modifier

    def roll(self, verbose, advantage: bool, disadvantage: bool) -> int:
        dice = self.dice(20, 1 + (advantage ^ disadvantage))
        d20 = min(dice) if ((not advantage) and disadvantage) else max(dice)
        if verbose:
            print(f"rolls: {', '.join(map(str, dice))}")
            print(f"d20: {d20}")
        return d20

    def dice(self, num_sides, num_dice=1):
        return [randint(1, num_sides) for _ in range(num_dice)]

    def verbose_roll(self, prof, prof_bonus, base_bonus, modifier):
        print(f"proficient: {prof}")
        print(f"proficiency bonus: {prof_bonus}")
        print(f"base bonus: {base_bonus}")
        print(f"modifier: {modifier}")

    def __str__(self):
        return "\n".join(f"\n{k}:\n{v}" for k, v in self.__dict__.items())


if __name__ == "__main__":
    try:
        filepath = sys.argv[1]
    except IndexError:
        print("No filepath given!")
        quit

    Player(filepath)
