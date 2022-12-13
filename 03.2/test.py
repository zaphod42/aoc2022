import pytest
import io
import main

def test_loads_rucksack_contents():
    rucksacks = main.Rucksacks.load(io.StringIO("vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg"))

    assert len(rucksacks.groups) == 1
    assert rucksacks.groups[0].contents == ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]

def test_finds_the_common_type():
    rucksacks = main.Rucksacks.load(io.StringIO("vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg"))

    assert rucksacks.groups[0].common() == "r"

def test_produces_priority_information():
    rucksacks = main.Rucksacks.load(io.StringIO("vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw#"))
    
    assert rucksacks.groups[0].priority() == 18
    assert rucksacks.groups[1].priority() == 52 
    assert rucksacks.total_priority() == 18+52

