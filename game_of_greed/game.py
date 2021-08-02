from game_of_greed.game_logic import GameLogic

class Game:

    def __init__(self):
        pass
       
    
    def play (self,roller):

        print('Welcome to Game of Greed')
        print('(y)es to play or (n)o to decline')
        response = input('> ')
        if response.lower() == 'n':
            print('OK. Maybe another time')
        if response.lower() == 'y' or response.lower()=='yes':
            print('Starting round 1')
            print('Rolling 6 dice...')
            print('*** 4 4 5 2 3 1 ***')
            print('Enter dice to keep, or (q)uit:')
            response = input('> ')
            if  response.lower() == 'q':
                    print('Thanks for playing. You earned 0 points')
            if  response.lower() == '5':
                    print('You have 50 unbanked points and 5 dice remaining')
                    print('(r)oll again, (b)ank your points or (q)uit:')
                    response =input('> ')
                    if response.lower() == 'b' or response.lower() =='B':
                        print('You banked 50 points in round 1')
                        print('Total score is 50 points')
                        print('Starting round 2')
                        print('Rolling 6 dice...')
                        print('*** 6 4 5 2 3 1 ***')
                        print('Enter dice to keep, or (q)uit:')
                        response = input('> ')
                        if response.lower() == 'q':
                            print('Thanks for playing. You earned 50 points')
if __name__=='__main__':
    play = Game((1,2,3,4,5,6))
    play.play((1,2,3,4,5,6))
