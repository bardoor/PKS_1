class Clock:
    __minutes: int
    __hours: int

    def __init__(self, minutes: int, hours: int):
        if not (0 <= hours <= 23.9):
            raise RuntimeError("Ошибка. Неправильный ввод Часов!")
        self.__hours = hours
        
        if not (0 <= minutes <= 59.9):
            raise RuntimeError("Ошибка. Неправильный ввод Минут!")
        self.__minutes = minutes

    def set_hours(self, hours: int):
        if not (0 <= hours <= 23.9):
            raise RuntimeError("Ошибка. Неправильный ввод Часов!")
        self.__hours = hours

    def set_minutes(self, minutes: int):
        if not (0 <= minutes <= 59.9):
            raise RuntimeError("Ошибка. Неправильный ввод Минут!")
        self.__minutes = minutes

    def __str__(self):
        return f'{self.__hours}:{self.__minutes}'

    def get_hours(self):
        return self.__hours

    def get_minutes(self):
        return self.__minute

    
