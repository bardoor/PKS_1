class Clock:
    __hours: int
    __minutes: int

    def __init__(self, hours: int=0, minutes: int=0) -> None:
        if not(0 <= hours <= 23):
            hours = 0
        self.__hours = hours
        if not(0 <= minutes <= 59):
            minutes = 0
        self.__minutes = minutes

    def set_hours(self, hours: int) -> None:
        if 0 <= hours <= 23:
            self.__hours = hours

    def set_minutes(self, minutes: int) -> None:
        if 0 <= minutes <= 59:
            self.__minutes = minutes

    def set_hours_and_minutes(self, hours: int, minutes: int) -> None:
        self.set_hours(hours)
        self.set_minutes(minutes)
    
    def get_hours(self) -> int:
        return self.__hours