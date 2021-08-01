from random import sample
from collections import Counter

class GameLogic:
    
    @staticmethod
    def calculate_score():
        pass
        
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
    
if __name__== "__main__":
    items = (1,2,2,3,3,4) # 
    result = Counter(items)
    dic = {(1,1):100,(2,2):50}
    score = 0
    for item in result.most_common():
       score = score + dic.get(item,0)
       
    print(score)
    