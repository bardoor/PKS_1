class Circle:
    def __init__(self, radius_length: float) -> None:
        self.radius_length = radius_length
        self.radius_length = radius_length

    def find_S(self) -> float:
        π = 3.14
        return π * (self.radius_length ** 2)

    def find_P(self) -> float:
        π = 3.14
        return (2 * π * self.radius_length)


