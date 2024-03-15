from abc import ABC, abstractmethod


# Abstract Factory Interface
class MagicalCharacterFactory(ABC):
    @abstractmethod
    def create_male(self):
        pass

    @abstractmethod
    def create_female(self):
        pass


# Concrete Factory for Elves characters
class ElvesFactory(MagicalCharacterFactory):
    def create_male(self):
        return ElfMale()

    def create_female(self):
        return ElfFemale()


# Concrete Factory for Dwarves characters
class DwarvesFactory(MagicalCharacterFactory):
    def create_male(self):
        return DwarfMale()

    def create_female(self):
        return DwarfFemale()

    # Abstract Product for Male


class Male(ABC):
    @abstractmethod
    def lifespan(self):
        pass

    @abstractmethod
    def skills(self):
        pass


# Concrete Class for Elf Male
class ElfMale(Male):
    def lifespan(self):
        print("A male elf typically lives for 500 years")

    def skills(self):
        print("The male elf is capable of great agility and speed")


# Concrete Class for Dwarf Male
class DwarfMale(Male):
    def lifespan(self):
        print("A male dwarf typically lives for 2000 years")

    def skills(self):
        print("The male dwarf is capable of great strength and endurance")


# Abstract Class for Female
class Female(ABC):
    @abstractmethod
    def lifespan(self):
        pass

    @abstractmethod
    def skills(self):
        pass


# Concrete Class for Elf Female
class ElfFemale(Female):
    def lifespan(self):
        print("A female elf typically lives for 1000 years")

    def skills(self):
        print("The female elf is capable of great wisdom and magic")


# Concrete Class for Dwarf Female
class DwarfFemale(Female):
    def lifespan(self):
        print("A female dwarf typically lives for 3000 years")

    def skills(self):
        print("The female dwarf is capable of great intelligence and craftsmanship")

    # Client code that uses the abstract factory


def creature_creator(factory: MagicalCharacterFactory):
    male = factory.create_male()
    female = factory.create_female()
    male.lifespan()
    male.skills()
    female.lifespan()
    female.skills()


# Example usage
if __name__ == "__main__":
    print("Creating elves:")
    creature_creator(ElvesFactory())

    print("\nCreating dwarves:")
    creature_creator(DwarvesFactory())

"""
Output - 

Creating elves:
A male elf typically lives for 500 years
The male elf is capable of great agility and speed
A female elf typically lives for 1000 years
The female elf is capable of great wisdom and magic

Creating dwarves:
A male dwarf typically lives for 2000 years
The male dwarf is capable of great strength and endurance
A female dwarf typically lives for 3000 years
The female dwarf is capable of great intelligence and craftsmanship
"""