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
    
    def __eq__(self, other) -> bool:
        return self.get_in_seconds() == other.get_in_seconds()
    
    def __ne__(self,other) -> bool:
        return not (self.get_in_seconds() == other.get_in_seconds())
    
    def __gt__(self, other) -> bool:
        return self.get_in_seconds() > other.get_in_seconds()
    
    def __lt__(self, other) -> bool:
        return self.get_in_seconds() < other.get_in_seconds()
    
    def __add__(self, other) -> bool:
        return self.get_in_seconds() + other.get_in_seconds()
    
    def __sub__(self, other):
        return self.get_in_seconds() - other.get_in_seconds()
