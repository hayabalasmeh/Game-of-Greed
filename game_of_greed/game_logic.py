from random import sample
from collections import Counter

class GameLogic:
    
    @staticmethod

    def calculate_score(number):
        score = 0 
        dice_Counter = Counter(number)

        # tuple of input numbers = (1,1,2,2,3,3)  ---> output = 200 
        # counter (1,1,2,2,3,3) ---> output = {1:2, 2:2, 3:2} 
        # 

        game_rules = {
        
        (1,): 100,
        (1, 1): 200,
        (1, 1, 1): 1000,
        (1, 1, 1, 1): 2000,
        (1, 1, 1, 1, 1): 3000,
        (1, 1, 1, 1, 1, 1): 4000,
        (2,): 0,
        (2, 2): 0,
        (2, 2, 2): 200,
        (2, 2, 2, 2): 400,
        (2, 2, 2, 2, 2): 600,
        (2, 2, 2, 2, 2, 2): 800,
        (3,): 0,
        (3, 3): 0,
        (3, 3, 3): 300,
        (3, 3, 3, 3): 600,
        (3, 3, 3, 3, 3): 900,
        (3, 3, 3, 3, 3, 3): 1200,
        (4,): 0,
        (4, 4): 0,
        (4, 4, 4): 400,
        (4, 4, 4, 4): 800,
        (4, 4, 4, 4, 4): 1200,
        (4, 4, 4, 4, 4, 4): 1600,
        (5,): 50,
        (5, 5): 100,
        (5, 5, 5): 500,
        (5, 5, 5, 5): 1000,
        (5, 5, 5, 5, 5): 1500,
        (5, 5, 5, 5, 5, 5): 2000,
        (6,): 0,
        (6, 6): 0,
        (6, 6, 6): 600,
        (6, 6, 6, 6): 1200,
        (6, 6, 6, 6, 6): 1800,
        (6, 6, 6, 6, 6, 6): 2400,
        (1, 2, 3, 4, 5, 6): 1500,
        (2, 2, 3, 3, 4, 6): 0,
        (2, 2, 3, 3, 6, 6): 1500,
        (1, 1, 1, 2, 2, 2): 1200,
            }    





    
    @staticmethod
    def roll_dice(num):
        return tuple(sample(range(1,6+1),num))
        

class Banker:
    def shelf():
        pass    
    def bank():
        pass 
    def clear_shelf():
        pass
    
    
    