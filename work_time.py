class TimeInterval:
    seconds: int

    def __init__(self,seconds: int,minuts: int=0,hours: int=0) -> None:
        self.seconds = seconds + minuts * 60 + hours * 3600

    def get_in_seconds(self):
        result = self.seconds
        return result