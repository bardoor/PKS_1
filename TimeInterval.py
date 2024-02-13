class TimeInterval:
    seconds: int

    def __init__(self, seconds: int, minutes: int = 0, hours: int = 0) -> None:
        self.seconds = seconds + minutes * 60 + hours * 3600