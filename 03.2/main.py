import functools

class Rucksacks:
    def __init__(self, groups):
        self.groups = groups

    def total_priority(self):
        return sum([group.priority() for group in self.groups])

    @classmethod
    def load(cls, fh):
        lines = [line.strip() for line in fh.readlines()]
        groups = zip(lines[:-2:3], lines[1:-1:3], lines[2::3])
        return Rucksacks([Group(group) for group in groups])

class Group:
    def __init__(self, contents):
        self.contents = list(contents)

    def common(self):
        return list(functools.reduce(lambda a, b: a & b, [set(x) for x in self.contents]))[0]

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
