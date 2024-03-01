class Clock:
    __hours: int
    __minutes: int

    def __init__(self, hours: int=0, minutes: int=0) -> None:
        if not(0 <= hours <= 23):
            raise RuntimeError("Warning! Before creating - check if 0 <= hours <= 23, after that just create.")
        self.__hours = hours
        if not(0 <= minutes <= 59):
            raise RuntimeError("Warning! Before creating - check if 0 <= minutes <= 59, after that just create.")
        self.__minutes = minutes

    def set_hours(self, hours: int) -> None:
        if not(0 <= hours <= 23):
            raise RuntimeError("Warning! Before setting hours, check if 0 <= hours <= 23")
        self.__hours = hours

    def set_minutes(self, minutes: int) -> None:
        if not(0 <= minutes <= 59):
            raise RuntimeError("Warning! Before setting minutes, check if 0 <= minutes <= 59")
        self.__minutes = minutes

    def set_hours_and_minutes(self, hours: int, minutes: int) -> None:
        self.set_hours(hours)
        self.set_minutes(minutes)
    
    def get_hours(self) -> int:
        return self.__hours
    
    def get_minutes(self) -> int:
        return self.__minutes
    
    def __str__(self) -> str:
        return f"{self.__hours}:{self.__minutes}"