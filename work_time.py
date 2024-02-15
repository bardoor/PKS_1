class TimeInterval:
    seconds: int

    def __init__(self,seconds: int,minuts: int=0,hours: int=0) -> None:
        self.seconds = seconds + minuts * 60 + hours * 3600

    def get_in_seconds(self) -> int:
        result = self.seconds
        return result
    
    def __str__(self) -> str:
        hours = self.seconds // 3600
        minuts = (self.seconds - hours * 3600) // 60
        seconds = self.seconds - hours * 3600 - minuts * 60

        return f"{hours}:{minuts}:{seconds}"