class Clock:
    __minutes: int
    __hours: int
    def __init__(self, minutes: int, hours: int):
        if not (0 <= hours <= 23):
            raise RuntimeError("Ошибка. Неправильный ввод Часов!")
        self.__hours = hours
        
        if not (0 <= minutes <= 59):
            raise RuntimeError("Ошибка. Неправильный ввод Минут!")
        self.__minutes = minutes

    
    
