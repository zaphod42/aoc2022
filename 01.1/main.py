class FoodInventory:
    def __init__(self, knapsacks):
        self.knapsacks = knapsacks

    @classmethod
    def load(cls, fh):
        text = fh.read()
        sacks = text.strip().split("\n\n")
        return FoodInventory([Knapsack([int(item) for item in sack.split("\n")]) for sack in sacks])

    def max_calories(self):
        return max([sack.total() for sack in self.knapsacks])


class Knapsack:
    def __init__(self, contents):
        self.contents = contents

    def total(self):
        return sum(self.contents)

if __name__ == "__main__":
    import io

    print("Max Calories: ")
    with io.open("data.txt", "r") as fh:
        print(FoodInventory.load(fh).max_calories())
