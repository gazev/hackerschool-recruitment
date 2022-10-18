from slot_machine import SlotMachine

class Game:
    def __init__(self, player, slot):
        self.__player = player
        self.__slot = slot 
        
    def is_jackpot(self):
        '''
        Returns True if current Slot has a jackpot combinatinon
        '''
        return self.__slot.is_winning_combination()

    def is_over(self):
        ''' 
        Returns True if player doesn't have credits left
        '''
        return not self.__player.get_credits() # o python converte valores para bool falso se estes forem zero null ou uma collection vazia

    def play_round(self, bet):
        '''
        Plays a round, alterning Slot's combination and deducing bet credits from Player
        If Jackpot is hit, adds prize to Player's credits 
        '''
        # take player bet
        self.__player.deduce_credits(bet)
        # roll slot combination
        self.__slot.roll()
        if(self.is_jackpot()):
            print('''
    /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$
   |__  $$ /$$__  $$ /$$__  $$| $$  /$$/| $$__  $$ /$$__  $$|__  $$__/| $$
      | $$| $$  \ $$| $$  \__/| $$ /$$/ | $$  \ $$| $$  \ $$   | $$   | $$
      | $$| $$$$$$$$| $$      | $$$$$/  | $$$$$$$/| $$  | $$   | $$   | $$
 /$$  | $$| $$__  $$| $$      | $$  $$  | $$____/ | $$  | $$   | $$   |__/
| $$  | $$| $$  | $$| $$    $$| $$\  $$ | $$      | $$  | $$   | $$       
|  $$$$$$/| $$  | $$|  $$$$$$/| $$ \  $$| $$      |  $$$$$$/   | $$    /$$
 \______/ |__/  |__/ \______/ |__/  \__/|__/       \______/    |__/   |__/
                ''')
            self.pay_prize(bet)

    def pay_prize(self, bet):
        '''
        Pays jackpot prize to player depending on bet value and combination symbol
        '''
        # get bet multiplier
        multiplier = SlotMachine.get_symbols_dic()[self.__slot.get_combination()[0]]
        # add credits to player's wallet
        self.__player.add_credits(bet * multiplier)
        print(f"You won {bet * multiplier} credits!")
    
    def display_info(self):
        '''
        Prints information on Slot's symbols and multipliers
        '''
        # print prizes info
        print("\nPrizes: ")
        print(*(f"{k}: {v}x" for k,v in SlotMachine.get_symbols_dic().items()), sep='\n') #Using a generator can also work, but it's a personal preference
        # for k, v in SlotMachine.get_symbols_dic().items():
        #     print(f"{k}: {v}x")

    def __str__(self):
        return f"{self.__slot}\n{self.__player}\n" #using an fstring here seems better and more readable
    