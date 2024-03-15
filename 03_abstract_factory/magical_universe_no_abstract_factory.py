# Defining concrete classes directly

class ElfMale:
    def lifespan(self):
        print("A male elf typically lives for 500 years")

    def skills(self):
        print("The male elf is capable of great agility and speed")


class ElfFemale:
    def lifespan(self):
        print("A female elf typically lives for 1000 years")

    def skills(self):
        print("The female elf is capable of great wisdom and magic")


class DwarfMale:
    def lifespan(self):
        print("A male dwarf typically lives for 2000 years")

    def skills(self):
        print("The male dwarf is capable of great strength and endurance")


class DwarfFemale:
    def lifespan(self):
        print("A female dwarf typically lives for 3000 years")

    def skills(self):
        print("The female dwarf is capable of great intelligence and craftsmanship")

# Client code directly creating instances of the characters
def create_character(race, gender):
    if race == "Elf" and gender == "Male":
        character = ElfMale()
    elif race == "Elf" and gender == "Female":
        character = ElfFemale()
    elif race == "Dwarf" and gender == "Male":
        character = DwarfMale()
    elif race == "Dwarf" and gender == "Female":
        character = DwarfFemale()
    else:
        raise ValueError("Invalid race or gender")

    character.lifespan()
    character.skills()


# Example usage
if __name__ == "__main__":
    print("Creating elves:")
    create_character("Elf", "Male")
    create_character("Elf", "Female")

    print("\nCreating dwarves:")
    create_character("Dwarf", "Male")
    create_character("Dwarf", "Female")

""" Output - 
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
