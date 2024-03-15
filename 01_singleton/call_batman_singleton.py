# singleton
class Batman:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


b1 = Batman()
b2 = Batman()
print(f"b1 is b2 = {b1 is b2}")  # True
