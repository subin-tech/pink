from copy import deepcopy

import pytest

from music_toolkit import summarize_transposition


def test_docstring_example():
    original = [{'pitch': 60, 'start': 0.0, 'end': 0.5}]
    changed = [{'pitch': 62, 'start': 0.0, 'end': 0.5}]
    assert summarize_transposition(original, changed) == [(60, 62)]


def test_pairs_preserve_order_duplicates_and_inputs():
    original = [
        {'pitch': pitch, 'start': 0.0, 'end': 0.5}
        for pitch in [127, 0, 60, 60]
    ]
    changed = [
        {'pitch': pitch, 'start': 0.0, 'end': 0.5}
        for pitch in [125, 2, 60, 62]
    ]
    before = deepcopy((original, changed))
    result = summarize_transposition(original, changed)
    assert result == [(127, 125), (0, 2), (60, 60), (60, 62)]
    assert (original, changed) == before


def test_empty_lists_return_empty_list():
    assert summarize_transposition([], []) == []


@pytest.mark.parametrize('lengths', [(0, 1), (1, 0), (1, 2), (2, 1)])
def test_unequal_lengths_raise_without_mutating_inputs(lengths):
    note = {'pitch': 60, 'start': 0.0, 'end': 0.5}
    original = [note.copy() for _ in range(lengths[0])]
    changed = [note.copy() for _ in range(lengths[1])]
    before = deepcopy((original, changed))
    with pytest.raises(ValueError, match='same length'):
        summarize_transposition(original, changed)
    assert (original, changed) == before
