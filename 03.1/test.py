import pytest
import io
import main

def test_loads_rucksack_contents():
    rucksacks = main.Rucksacks.load(io.StringIO("vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n"))

    assert len(rucksacks.sacks) == 2
    assert rucksacks.sacks[0].compartments == ["vJrwpWtwJgWr", "hcsFMMfFFhFp"]

def test_finds_the_common_type():
    rucksacks = main.Rucksacks.load(io.StringIO("vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg"))

    assert rucksacks.sacks[0].common() == "p"
    assert rucksacks.sacks[1].common() == "L"
    assert rucksacks.sacks[2].common() == "P"

def test_produces_priority_information():
    rucksacks = main.Rucksacks.load(io.StringIO("vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg"))

    assert rucksacks.sacks[0].priority() == 16
    assert rucksacks.sacks[1].priority() == 38
    assert rucksacks.sacks[2].priority() == 42
    assert rucksacks.total_priority() == 16 + 38 + 42

