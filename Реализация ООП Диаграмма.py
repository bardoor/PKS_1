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

class Motherboard:
    __ram: Ram
    __videocard: Videocard
    __processor: Processor
    is_mulstaking: void
    binding: void
    def __init__(self):
        self.__ram = Ram()
        self.__videocard = Videocard()
        self.__processor = Processor()
    def can_run(self, process):
        pass

class Ram:
    _is_volume: bool
    def get_value(self):
        pass
