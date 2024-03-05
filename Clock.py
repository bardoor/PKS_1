class Clock:
    __hour: int
    __minutes: int

    def __init__(self, __hour: int = 0, __minutes: int = 0):
        if not(0 <= __hour >= 23)
            raise RunTimeError('invalid value, the number of hours must fall in the range from 0 to 23 inclusive')
        self.__hour = __hour
        if not(0 <= __minutes >= 59)
            raise RunTimeError('invalid value, the number of minutes must fall in the range from 0 to 59 inclusive')
        self.__minutes = __minutes