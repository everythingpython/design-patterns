from abc import abstractmethod


class XMen:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def use_power(self):
        pass


class Telepath(XMen):
    def use_power(self):
        print(f"{self.name}  is reading minds with telepathy.")


class Telekinesis(XMen):
    def use_power(self):
        print(f"{self.name} is lifting objects using the power of the mind.")


class OpticBlast(XMen):
    def use_power(self):
        print(f"{self.name} is firing powerful optic blasts from the eyes.")


class XMenFactory:
    @staticmethod
    def create_xmen(mutation_type, name):
        if mutation_type == "telepath":
            return Telepath(name)
        elif mutation_type == "telekinetic":
            return Telekinesis(name)
        elif mutation_type == "optic_blast":
            return OpticBlast(name)
        else:
            raise ValueError("Invalid X-Men power provided")


# Client example
def showcase_powers(mutation_type, name):
    xmen = XMenFactory.create_xmen(mutation_type, name)
    xmen.use_power()


showcase_powers("telepath", "Professor X")
showcase_powers("optic_blast", "Cyclops")
