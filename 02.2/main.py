from enum import Enum

class Cheatsheet:
    def __init__(self, rounds):
        self.rounds = rounds

    @classmethod
    def load(cls, fh):
        translations = {
            'A': Plays.ROCK,
            'B': Plays.PAPER,
            'C': Plays.SCISSORS,
            'X': Outcomes.LOSE,
            'Y': Outcomes.DRAW,
            'Z': Outcomes.WIN }
        return Cheatsheet(
                [Round(*[translations[token] for token in line.strip().split(' ')])
                    for line in fh.readlines()]) 

    def total_score(self):
        return sum([r.score() for r in self.rounds])

class Round:
    def __init__(self, opponent, outcome):
        self.opponent = opponent
        self.outcome = outcome

    def play(self):
        loses = {
            Plays.PAPER: Plays.ROCK,
            Plays.SCISSORS: Plays.PAPER,
            Plays.ROCK: Plays.SCISSORS }
        beats = dict([(value, key) for (key, value) in loses.items()]) 
        
        if self.outcome == Outcomes.DRAW:
            return self.opponent
        elif self.outcome == Outcomes.WIN:
            return beats[self.opponent] 
        elif self.outcome == Outcomes.LOSE:
            return loses[self.opponent]

    def score(self):
        return self.outcome.value + self.play().value

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
