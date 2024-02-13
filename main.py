class TimeInterval:
    seconds: int
    def __init__(self, seconds:int , minutes:int = 0, hours: int = 0 ):
        self.seconds = seconds + minutes * 60 + hours * 3600

    def __eq__(self, other):
        if self.seconds == other.seconds:
            return True
        return False
    
    def __ne__(self,other):
        if self.seconds == other.seconds:
            return True
        return False

    
    def __str__(self):
        hours = self.seconds // 3600
        minutes = (self.seconds - hours * 3600) // 60
        seconds = self.seconds - (hours * 3600) - (minutes * 60)
        return f"Здесь часов >>{hours} , минут >> {minutes} , секунд{seconds} "
    
    def __gt__(self, other):
        if self.seconds > other.seconds:
            return True
        return False
        
    def __lt__(self, other):
        if self.seconds < other.seconds:
            return True
        return False

    
    def __add__(self, other):
        return TimeInterval(self.seconds + other.seconds)
    
    def __sub__(self, other):
        return(self.seconds - other.seconds)
    
    def __le__(self, other):
        if self.seconds <= other.seconds:
            return True
        return False
    
    def __ge__(self , other):
        if self.seconds >= other.seconds:
            return True
        return Falseы
    
    def getting_the_time_in_minutes(self, other):
        return self.seconds / 60 
    
    def getting_the_time_in_hours(self, other):
        return self.seconds // 3600
    
    def getting_the_time_in_seconds(self, other):
        return self.seconds 

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     