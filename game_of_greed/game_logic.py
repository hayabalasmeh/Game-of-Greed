
from random import sample , randint
from collections import Counter

class GameLogic:
     game_rules = {
        
        (1,1): 100,
        (1, 2): 200,
        (1, 3): 1000,
        (1, 4): 2000,
        (1, 5): 3000,
        (1, 6): 4000,
        (2,1): 0,
        (2, 2): 0,
        (2, 3): 200,
        (2, 4): 400,
        (2, 5): 600,
        (2, 6): 800,
        (3,1): 0,
        (3, 2): 0,
        (3, 3): 300,
        (3, 4): 600,
        (3, 5): 900,
        (3, 6): 1200,
        (4,1): 0,
        (4, 2): 0,
        (4, 3): 400,
        (4, 4): 800,
        (4, 5): 1200,
        (4, 6): 1600,
        (5,1): 50,
        (5, 2): 100,
        (5, 3): 500,
        (5, 4): 1000,
        (5, 5): 1500,
        (5, 6): 2000,
        (6,1): 0,
        (6, 2): 0,
        (6, 3): 600,
        (6, 4): 1200,
        (6, 5): 1800,
        (6, 6): 2400,
        (1, 2, 3, 4, 5, 6): 1500,
        (2, 2, 3, 3, 4, 6): 0,
        (2, 2, 3, 3, 6, 6): 1500,
        (1, 1, 1, 2, 2, 2): 1200,
            } 
    @staticmethod
    def calculate_score(number):
          

        score = 0 
        dice_Counter = Counter(number) 
        list_repetition = dice_Counter.most_common()
        if len(number) == 6 and len(list_repetition)== 6:
                score = 1500
        elif len(number) == 6 and len(list_repetition)== 3 and list(dice_Counter.values())[0] == 2:
            score = 1500
       
        else:
          for element in list_repetition:
             score = score + game_rules.get(element,0)

        return score 

    
    @staticmethod
    def roll_dice(num):
        roll_list = [randint(1,6) for _ in range(num)]
        return tuple(roll_list)
        

class Banker:
 
    def __init__(self):
        self.shelved = 0
        self.balance = 0
        
    def shelf(self,score):
        self.shelved += score
    def bank(self):
        self.balance = self.shelved 
        self.shelved =0 
    def clear_shelf(self):
        self.shelved =0 

if  __name__ == "__main__":
    values = (1,2,3,1) 
    output = (1,1)
    values_counter = Counter(values)
    tuples = values_counter.most_common()
    list = []
    
    for element in tuples:
        if game_rules.get(element,0)


## (1,2,3,1) -- (1,1)
# (1)
## for element in list_repetition: 
##
             ## if game_rules.get(element,0) == 0 
             ## (1,2) ()
             ## 



