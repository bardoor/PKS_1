class Clock:
    __hours:int
    __minutes:int

def __init__(self , hours:int , minutes:float):
   self.__hours = hours
   self.__minutes = minutes

def set_minutes(self , minutes:float):
    if 0 <= minutes <= 59.9:
        self.__minutes = minutes

def set_hours(self ,hours:int):
    if 0 <= hours <= 23:
        self.__hours = hours

def set_minutes_and_set_hours(self , hours:int , minutes:float):
    self.set_hours(hours)
    self.set_minutes(minutes)

def get_minutes(self):
    return self.__minutes

def get_hours(self):
    return self.__hours

def __str__(self):
    return f"Сейчас часов >>{self.__hours} , минут >>{self.__minutes}"

    