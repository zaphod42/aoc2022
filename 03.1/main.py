import functools

class Rucksacks:
    def __init__(self, sacks):
        self.sacks = sacks

    def total_priority(self):
        return sum([sack.priority() for sack in self.sacks])

    @classmethod
    def load(cls, fh):
        return Rucksacks([Sack(line.strip()) for line in fh.readlines()])

class Sack:
    def __init__(self, line):
        middle = int(len(line)/2)
        self.compartments = [line[0:middle], line[middle:]]

    def common(self):
        return list(functools.reduce(lambda a, b: a & b, [set(x) for x in self.compartments]))[0]

    def priority(self):
        priorities = dict(
                [[chr(c), c - ord('a') + 1] for c in range(ord('a'), ord('z') + 1)]
                + [[chr(c), c - ord('A') + 27] for c in range(ord('A'), ord('Z') + 1)])

        return priorities[self.common()]

if __name__ == "__main__":
    import io
    print("Total Priority: ")
    with io.open("data.txt", "r") as fh:
        print(Rucksacks.load(fh).total_priority())
