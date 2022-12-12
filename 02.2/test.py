import pytest
import io
import main

def test_loads_cheatsheet():
    sheet = main.Cheatsheet.load(io.StringIO("A Y\nB X\nC Z"))

    assert len(sheet.rounds) == 3

def test_determines_needed_move_for_outcome():
    sheet = main.Cheatsheet.load(io.StringIO("A Y\nB X\nC Z\nB Z"))

    assert sheet.rounds[0].play() == main.Plays.ROCK
    assert sheet.rounds[1].play() == main.Plays.ROCK
    assert sheet.rounds[2].play() == main.Plays.ROCK
    assert sheet.rounds[3].play() == main.Plays.SCISSORS

def test_determines_my_score_of_round():
    sheet = main.Cheatsheet.load(io.StringIO("A Y\nB X\nC Z"))

    assert sheet.rounds[0].score() == 4
    assert sheet.rounds[1].score() == 1
    assert sheet.rounds[2].score() == 7
    assert sheet.total_score() == 12
