class Player:
    def __init__(self, credits):
        self.__credits = credits
    
    def get_credits(self):
        return self.__credits
    
    def deduce_credits(self, deduce_value):
        '''
        Deduces given deduce_value from Player's credits.
        Throws AssertionException if Player doesn't have enough credits
        '''
        assert (self.__credits >= deduce_value), f"\nInsufficient funds!\n{self.__str__()}\n"
        self.__credits -= deduce_value
    
    def add_credits(self, prize):
        '''
        Adds credits to Player
        '''
        self.__credits += prize 
        
    def __str__(self):
        return f"Your credits: {self.__credits}"