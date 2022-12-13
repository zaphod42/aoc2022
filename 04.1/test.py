import pytest
import io
import main

def test_loads_ranges():
    cleanup = main.Cleanup.load(io.StringIO("2-4,6-8\n2-3,4-5\n"))

    assert len(cleanup.assignments) == 2
    assert cleanup.assignments[0].ranges == [[2, 4], [6, 8]]

def test_detects_total_overlap():
    cleanup = main.Cleanup.load(io.StringIO("6-6,4-6\n2-8,3-7\n5-7,7-9"))

    assert cleanup.assignments[0].total_overlap()
    assert cleanup.assignments[1].total_overlap()
    assert not cleanup.assignments[2].total_overlap()
    assert cleanup.overlap_count() == 2
