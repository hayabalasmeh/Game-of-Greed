from random import sample
from collections import Counter


class GameLogic:   
    @staticmethod
    def calculate_score(d):
        score = 0
        #The Counter() function returns unorderd dictionary
        d = Counter(d)
        if len(d) == 0:
            return 0
        # most_common function returns a list, which is sorted based on the count of the elements.
        elif d.most_common(1) == 1 and len(d) == 6:
            score += 1500
            return score
    @staticmethod
    def roll_dice(num):
        return sample(range(1,6+1),num)
        

class Banker:
    def shelf():
        pass    
    def bank():
        pass 
    def clear_shelf():
        pass
    
    
