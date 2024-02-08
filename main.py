class Square:
    def __init__(self, side_length: float) -> None:
        self.side_length = side_length

    def find_S(self) -> float:
        return (self.side_length ** 2)
    
    def find_P(self) -> float:
        return (self.side_length * 4)