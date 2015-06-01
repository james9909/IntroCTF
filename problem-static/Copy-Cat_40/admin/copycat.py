import sys

flag = "shoulda_been_my_final_project"

ROCK = 1
PAPER = 2
SCISSORS = 3
moves = ['r', 'p', 's']

WIN = 1
LOSE = 2
TIE = 3
INVALID = 4

# Ignore this, just for output
class UnbufferedStream(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

class AI():
    '''Unbeatable rock-paper-scissors ai. Might as well give up now.'''

    def __init__(self):
        self.history = []

    def run(self, player_move):
        if player_move in moves:
            if len(self.history) == 0:
                computer_move = 'r'
            else:
                computer_move = self.history[-1]
            self.history.append(player_move)
            result = self.win_lose_tie(player_move, computer_move)
            return result
        else:
            return False

    def win_lose_tie(self, player_move, computer_move):
        if __name__ == "__main__":
            print "The computer chose %s!" %(computer_move)
        if player_move == computer_move:
            return TIE
        if player_move == ROCK:
            if computer_move == PAPER:
                return LOSE
            if computer_move == SCISSORS:
                return WIN
        elif player_move == PAPER:
            if computer_move == SCISSORS:
                return LOSE
            if computer_move == ROCK:
                return WIN
        elif player_move == SCISSORS:
            if computer_move == ROCK:
                return LOSE
            if computer_move == PAPER:
                return WIN
        else:
            return INVALID

sys.stdout = UnbufferedStream(sys.stdout)

if __name__ == "__main__":
    print "Let's make a deal. Beat my rock paper scissors bot and I'll give you the flag."
    computer = AI()
    turns = 1
    wins = 0
    while turns <= 100:
        player_move = raw_input("Round " + str(turns) + " - Choose (r)ock, (p)aper, or (s)cissors\n>> ")
        result = computer.run(player_move)
        if result == False:
            print "Bad Input!"
            continue
        elif result == WIN:
            print "Win!"
            wins += 1
        elif result == LOSE:
            print "Lose!"
            break
        elif result == TIE:
            print "Tie!"
            break
        turns += 1
    if wins == 100:
        print "Impossible! What a cheater... Here's the flag for winning I guess... %s" %(flag)
    else:
        print "You only won %s times. No flag for you." %(wins)
