import pytest
import io
import main

def test_loads_multiple_knapsacks():
    inventory = main.FoodInventory.load(io.StringIO("100\n200\n\n400"))

    assert len(inventory.knapsacks) == 2
    assert [sack.total() for sack in inventory.knapsacks] == [300, 400]

def test_ignores_a_trailing_newline():
    inventory = main.FoodInventory.load(io.StringIO("400\n"))

    assert len(inventory.knapsacks) == 1
    assert [sack.total() for sack in inventory.knapsacks] == [400]

def test_finds_the_max_calories():
    data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    inventory = main.FoodInventory.load(io.StringIO(data))

    assert inventory.max_calories() == 24000
