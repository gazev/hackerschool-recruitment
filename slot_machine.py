import random

class SlotMachine:
    # maps all available symbols and their respective bet multiplier
    __symbols = {
        "#": 5,
        "&": 10,
        "%": 20,
        "»": 70,
        "@": 200,
        "$": 1000,
        "£": 100000
    } 

    @classmethod
    def get_symbols_dic(cls):
        return cls.__symbols


    def __init__(self):
        # initial machine combination (first three symbols) 
        self.__combination = [_ for _ in list(SlotMachine.__symbols.keys())[:3]]
    
    def get_combination(self):
        return self.__combination
    
    def roll(self):
        '''
        Determines Slot's combination with weighted probability 
        1st symbol - 50/156
        2nd symbol - 40/156
        3rd symbol - 30/156
        4th symbol - 20/156
        5th symbol - 10/156
        6th symbol - 5/156
        7th symbol - 1/156 
        '''
        self.__combination = random.choices(list(SlotMachine.__symbols.keys()), 
                                weights=[50, 40, 30, 20, 10, 5, 1], k=3)

    def is_winning_combination(self):
        '''
        Returns True if current Slot combination is a winning combination
        '''
        return self.__combination[0] == self.__combination[1] == self.__combination[2]

    def __str__(self):
        return "+~~~~~~~~~~~+\n" + \
               "| € SLOTS € |\n" + \
               "|'''''''''''|\n" + \
               "|   {}   |\n".format('-'.join(self.__combination)) + \
               "|___________|"