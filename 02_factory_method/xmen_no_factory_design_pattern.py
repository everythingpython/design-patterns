class Telepathy:
    @staticmethod
    def use_power(name: str) -> str:
        return f"{name} is reading minds with telepathy."


class Telekinesis:
    @staticmethod
    def use_power(name: str) -> str:
        return f"{name} is lifting objects using the power of the mind."


class OpticBlast:
    @staticmethod
    def use_power(name: str) -> str:
        return f"{name} is firing powerful optic blasts from the eyes."


class XMen:
    def __init__(self, name: str, power: str):
        self.name = name
        self.power = power

    def use_power(self) -> str:
        return self.power.use_power(self.name)


# Client code example

def showcase_power(mutation_type: str, name: str) -> str:
    if mutation_type == "telepath":
        power = Telepathy
    elif mutation_type == "telekinetic":
        power = Telekinesis
    elif mutation_type == "optic_blast":
        power = OpticBlast
    else:
        raise ValueError("Invalid X-Men power provided")

    xmen = XMen(name, power)
    return xmen.use_power()


print(showcase_power("telepath", "Professor X"))
print(showcase_power("optic_blast", "Cyclops"))
