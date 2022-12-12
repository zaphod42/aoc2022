class FoodInventory:
    def __init__(self, knapsacks):
        self.knapsacks = knapsacks

    @classmethod
    def load(cls, fh):
        text = fh.read()
        sacks = text.strip().split("\n\n")
        return FoodInventory([Knapsack([int(item) for item in sack.split("\n")]) for sack in sacks])

    def total_max_calories(self, n):
        ordered = sorted(self.knapsacks, key=Knapsack.total, reverse=True)
        return sum([sack.total() for sack in ordered[0:n]])


class Knapsack:
    def __init__(self, contents):
        self.contents = contents

    def total(self):
        return sum(self.contents)

if __name__ == "__main__":
    import io

    print("Top 3 Total Calories: ")
    with io.open("data.txt", "r") as fh:
        print(FoodInventory.load(fh).total_max_calories(3))
