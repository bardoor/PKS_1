class TimeInterval:
    seconds: int

    def __init__(self, seconds: int, minutes: int = 0, hours: int = 0) -> None:
        self.seconds = seconds + minutes * 60 + hours * 3600

    def __add__(self, other):
        return TimeInterval(self.seconds + other.seconds)

    def __sub__(self, other):
        return TimeInterval(self.seconds - other.seconds)
    
    def __str__(self) -> str:
        hours = self.seconds // 3600
        minutes = (self.seconds - hours * 3600) // 60
        seconds = self.seconds - hours * 3600 - minutes * 60
        return f"В данном промежутке времени есть {hours} часов, {minutes} минут, {seconds} секунд"
    
    def __eq__(self, other) -> bool:
        if self.seconds == other.seconds:
            return True
        return False
    
    def __ne__(self, other) -> bool:
        if self.seconds != other.seconds:
            return True
        return False
    
    def __lt__(self, other) -> bool:
        if self.seconds < other.seconds:
            return True
        return False

    def __gt__(self, other) -> bool:
        if self.seconds > other.seconds:
            return True
        return False
    
    def __le__(self, other) -> bool:
        if self.seconds <= other.seconds:
            return True
        return False

    def __ge__(self, other) -> bool:
        if self.seconds >= other.seconds:
            return True
        return False