class TimeInterval:
    __seconds: int

    def __init__(self, seconds: int=0, minutes: int=0, hours: int=0) -> None:
        if not(seconds >= 0 and minutes >= 0 and hours >= 0):
            raise RuntimeError("Warning! Hours, minutes, seconds must be greater than or equal to 0")
        self.__seconds = seconds + minutes * 60 + hours * 3600

    def __add__(self, other: 'TimeInterval') -> 'TimeInterval':
        return TimeInterval(self.__seconds + other.__seconds)

    def __sub__(self, other: 'TimeInterval') -> 'TimeInterval':
        if self.__seconds < other.__seconds:
            raise RuntimeError("Warning! Time interval cannot be less than 0")
        return TimeInterval(self.__seconds - other.__seconds)
    
    def __eq__(self, other: 'TimeInterval') -> bool:
        return self.__seconds == other.__seconds
    
    def __ne__(self, other: 'TimeInterval') -> bool:
        return self.__seconds != other.__seconds
    
    def __lt__(self, other: 'TimeInterval') -> bool:
        return self.__seconds < other.__seconds

    def __gt__(self, other: 'TimeInterval') -> bool:
        return self.__seconds > other.__seconds
    
    def __le__(self, other: 'TimeInterval') -> bool:
        return self.__seconds <= other.__seconds

    def __ge__(self, other: 'TimeInterval') -> bool:
        return self.__seconds >= other.__seconds
    
    def get_time_interval_in_nanoseconds(self) -> int:
        return self.__seconds * 1000000000
    
    def get_time_interval_in_seconds(self) -> int:
        return self.__seconds
    
    def get_time_interval_in_minutes(self) -> float:
        return self.__seconds / 60
    
    def get_time_interval_in_hours(self) -> float:
        return self.__seconds / 3600
    
    def get_time_interval_in_days(self) -> float:
        return self.__seconds / 86400
    
    def __str__(self) -> str:
        hours = self.__seconds // 3600
        minutes = (self.__seconds - hours * 3600) // 60
        seconds = self.__seconds - hours * 3600 - minutes * 60
        return f"В данном промежутке времени есть {hours} часов, {minutes} минут, {seconds} секунд"