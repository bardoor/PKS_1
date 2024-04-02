class User:
    __name: str
    def __init__(self, name: str):
        self.__name = name
    def start_computer(self):
        pass
    def turn_computer(self):
        pass

class Computer:
    __name: str
    __system: str
    __motherbroad: Motherboard
    def __init__(self, name: str,  system: str):
        self.__name = name
        self.__system = system
        self.__motherbroad = Motherboard
    def start_system(self, process):
        pass
    def turn_off_system(self):
        pass

class Process:
    _mulstaking: str
    def input_videocard(self, power):
        pass
    def input_processor(self, power):
        pass
    def input_ram(self, volume):
        pass
