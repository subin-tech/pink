import pytest

from music_toolkit import validate_semitones


@pytest.mark.parametrize("semitones", [2, -3, 0, 128])
def test_accepts_integer_shifts(semitones):
    assert validate_semitones(semitones) is None


@pytest.mark.parametrize("semitones", [True, False, 2.0, 2.5, "2", None])
def test_rejects_non_integer_shifts_and_booleans(semitones):
    with pytest.raises(TypeError, match="semitones must be an integer"):
        validate_semitones(semitones)
