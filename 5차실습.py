import random

class Player:
    def __init__(self):
        self.hand = ""
        self.num_wins = 0

    def play(self):
        # 0: rock
        # 1: scissors
        # 2: paper
        self.hand=random.randint(0,2)

    def feedback(self, opponent):
        if self.hand==opponent.hand:
            return "draw"
        elif self.hand==opponent.hand+1 or self.hand==opponent.hand-2:
            return "lose"
        else:
            self.num_wins += 1
            return "win"

def main():

    RSP = {0: 'rock', 1: 'scissors', 2: 'paper'}
    a = Player()
    b = Player()

    for i in range(5):
        a.play()
        b.play()
        result_a = a.feedback(b)
        result_b = b.feedback(a)


        print("round %d, (a) %s vs %s (b)" % (i, RSP[a.hand], RSP[b.hand]))
        print("a %s b %s" %(result_a, result_b))

    print("a win %d times" %a.num_wins)
    print("b win %d times" %b.num_wins)


main()