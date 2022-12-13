class Cleanup:
    def __init__(self, assignments):
        self.assignments = assignments

    def overlap_count(self):
        return sum([a.overlap() for a in self.assignments])

    @classmethod
    def load(cls, fh):
        return Cleanup([
            Assignments([[int(x) for x in r.split('-')] for r in line.split(',')])
            for line in fh.readlines()])

class Assignments:
    def __init__(self, ranges):
        self.ranges = ranges

    def overlap(self):
        ordered_ranges = sorted(self.ranges, key=lambda x: x[1]-x[0], reverse=True)
        longer = ordered_ranges[0]
        shorter = ordered_ranges[1]
        return (
            (shorter[0] >= longer[0] and shorter[1] <= longer[1])
            or (shorter[0] >= longer[0] and shorter[0] <= longer[1])
            or (shorter[1] >= longer[0] and shorter[1] <= longer[1]))

if __name__ == "__main__":
    import io
    print("Overlaps: ")
    with io.open("data.txt", "r") as fh:
        print(Cleanup.load(fh).overlap_count())
