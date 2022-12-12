from enum import Enum

class Cheatsheet:
    def __init__(self, rounds):
        self.rounds = rounds

    @classmethod
    def load(cls, fh):
        plays = {
            'A': Plays.ROCK, 'X': Plays.ROCK,
            'B': Plays.PAPER, 'Y': Plays.PAPER,
            'C': Plays.SCISSORS, 'Z': Plays.SCISSORS }
        return Cheatsheet(
                [Round(*[plays[token] for token in line.strip().split(' ')])
                    for line in fh.readlines()]) 

    def total_score(self):
        return sum([r.score() for r in self.rounds])

class Round:
    def __init__(self, opponent, own):
        self.opponent = opponent
        self.own = own

    def outcome(self):
        beats = {
            Plays.PAPER: Plays.ROCK,
            Plays.SCISSORS: Plays.PAPER,
            Plays.ROCK: Plays.SCISSORS }
        
        if self.opponent == self.own:
            return Outcomes.DRAW
        if beats[self.opponent] == self.own:
            return Outcomes.LOSE
        if self.opponent == beats[self.own]:
            return Outcomes.WIN

    def score(self):
        return self.outcome().value + self.own.value

class Outcomes(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3

class Plays(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

if __name__ == "__main__":
    import io

    print("Score at end: ")
    with io.open("data.txt", "r") as fh:
        print(Cheatsheet.load(fh).total_score())
