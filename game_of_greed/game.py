from game_of_greed.game_logic import GameLogic

# class Game:

    # def __init__(self):
    #     self.round = 0
    #     # self.roller = roller or GameLogic.roll_dice
    
    # def play (self,roller= GameLogic.roll_dice(6)):

    #     print('Welcome to Game of Greed')
    #     print('(y)es to play or (n)o to decline')
    #     response = input('> ')
    #     if response.lower() == 'n':
    #         print('OK. Maybe another time')
    #     if response.lower() == 'y' or response.lower()=='yes':
    #         print('Starting round 1')
    #         print('Rolling 6 dice...')

    #         print(f'*** {roller} ***')
    #         print('Enter dice to keep, or (q)uit:')
    #         response = input('> ')
    #         if  response.lower() == 'q':
    #                 print('Thanks for playing. You earned 0 points')
    #         if  response.lower() == '5':
    #                 print('You have 50 unbanked points and 5 dice remaining')
    #                 print('(r)oll again, (b)ank your points or (q)uit:')
    #                 response =input('> ')
    #                 if response.lower() == 'b' or response.lower() =='B':
    #                     print('You banked 50 points in round 1')
    #                     print('Total score is 50 points')
    #                     print('Starting round 2')
    #                     print('Rolling 6 dice...')
    #                     print('*** 6 4 5 2 3 1 ***')
    #                     print('Enter dice to keep, or (q)uit:')
    #                     response = input('> ')
    #                     if response.lower() == 'q':
    #                         print('Thanks for playing. You earned 50 points')



class Game:
    
    def __init__(self):
        self.count = 0
        self.bank = 0
        self.score = 0
        self.result = 0

    
    def play(self,roller=None):
        roller = roller or GameLogic.roll_dice 
        dice = 6
        print('Welcome to Game of Greed')
        print('(y)es to play or (n)o to decline')
        self.count+=1
        start_or_not = input('> ')
        start = True
        if start_or_not.lower() == 'n':
            print('OK. Maybe another time')
            start = False 
        while start:
          
          if start_or_not.lower() == 'y':
            print('Starting round {}'.format(self.count))
            print('Rolling 6 dice...')
            roll = roller(dice)
            roll_str = ""
            for num in roll:
                roll_str += str(num) + " "
            print(f"*** {roll_str}***")
            print('Enter dice to keep, or (q)uit:')
            respone = input('> ')
          if respone == 'q':
            print('Thanks for playing. You earned {} points'.format(self.bank)) 
            break
          elif respone != 'b':
             data = []
             p = list(respone)     
             for i in p:
                data.append(int(i)) 
             self.score = GameLogic.calculate_score(tuple(data))
             self.result = GameLogic.calculate_score(tuple(data))
             dice_one = 6-len(p) 
             print('You have {} unbanked points and {} dice remaining'.format(self.result,dice_one))
             print('(r)oll again, (b)ank your points or (q)uit:')
             respone = input('> ')
          if respone == 'b': 
            self.bank += self.score
            print('You banked {} points in round {}'.format(self.result,self.count))
            self.count+=1
            print('Total score is {} points'.format(self.bank))
            self.result = 0
          if respone == "r":
            
            print(f'Rolling {dice_one} dice...')
            roll = roller(dice_one)
            roll_str = ""
            for num in roll:
                roll_str += str(num) + " "
            print(f"*** {roll_str}***")
            print('Enter dice to keep, or (q)uit:')
            response = input('> ')
            data = []
            p = list(response)     
            for i in p:
                data.append(int(i)) 
            self.score = GameLogic.calculate_score(tuple(data))
            self.result = GameLogic.calculate_score(tuple(data))
            dice_two = 6-len(p) 
            print('You have {} unbanked points and {} dice remaining'.format(self.result,dice_two))
            print('(r)oll again, (b)ank your points or (q)uit:')
            response = input('> ')
            
            if response == 'b': 
                self.bank += self.score
                print('You banked {} points in round {}'.format(self.result,self.count))
                self.count+=1
                print('Total score is {} points'.format(self.bank))
                self.result = 0
                print('Starting round {}'.format(self.count))
                print('Rolling 6 dice...')
                roll = roller(dice_two)
                roll_str = ""
                for num in roll:
                    roll_str += str(num) + " "
                print(f"*** {roll_str}***")
                print('Enter dice to keep, or (q)uit:')
                response = input('> ')
                if respone == 'q':
                   print('Thanks for playing. You earned {} points'.format(self.bank)) 
                   break



            

if __name__ =='__main__':
    print('work')
    x = Game()
    x.play()






# if respone == '5':
#     print('You have 50 unbanked points and 5 dice remaining')
#     print('(r)oll again, (b)ank your points or (q)uit:')
#     bank= input('> ') 
#     if bank == 'b':

#         print('You banked 50 points in round 1')
#         print('Total score is 50 points')
#         print('Starting round 2')
#         print('Rolling 6 dice...')
#         print('*** 6 4 5 2 3 1 ***') 
#         print('Enter dice to keep, or (q)uit:')
#         respone_after = input('> ') 
#         if respone_after == 'q':
#             print('Thanks for playing. You earned 50 points')      
