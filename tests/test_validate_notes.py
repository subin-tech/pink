import pytest

from music_toolkit.core import validate_notes


def test_validate_notes_accepts_empty_list():
    assert validate_notes([]) is None


def test_validate_notes_accepts_valid_pitch_boundaries():
    notes = [
        {"pitch": 0, "start": 0.0, "end": 0.5},
        {"pitch": 127, "start": 0.0, "end": 1.0},
    ]

    assert validate_notes(notes) is None


@pytest.mark.parametrize(
    ("note", "reason"),
    [
        ({"pitch": -1, "start": 0.0, "end": 0.5}, "pitch must be between 0 and 127"),
        ({"pitch": 128, "start": 0.0, "end": 0.5}, "pitch must be between 0 and 127"),
        ({"pitch": 60, "start": -0.5, "end": 0.5}, "start must be non-negative"),
        ({"pitch": 60, "start": 0.5, "end": 0.5}, "end must be greater than start"),
    ],
)
def test_validate_notes_rejects_invalid_note(note, reason):
    notes = [{"pitch": 60, "start": 0.0, "end": 0.5}, note]

    with pytest.raises(ValueError, match=rf"notes\[1\]: {reason}"):
        validate_notes(notes)
