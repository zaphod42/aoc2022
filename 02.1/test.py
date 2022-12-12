import pytest
import io
import main

def test_loads_cheatsheet():
    sheet = main.Cheatsheet.load(io.StringIO("A Y\nB X\nC Z"))

    assert len(sheet.rounds) == 3

def test_determines_outcome_of_round():
    sheet = main.Cheatsheet.load(io.StringIO("A Y\nB X\nC Z"))

    assert sheet.rounds[0].outcome() == main.Outcomes.WIN
    assert sheet.rounds[1].outcome() == main.Outcomes.LOSE
    assert sheet.rounds[2].outcome() == main.Outcomes.DRAW

def test_determines_my_score_of_round():
    sheet = main.Cheatsheet.load(io.StringIO("A Y\nB X\nC Z"))

    assert sheet.rounds[0].score() == 8
    assert sheet.rounds[1].score() == 1
    assert sheet.rounds[2].score() == 6
    assert sheet.total_score() == 15
