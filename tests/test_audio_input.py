
from music_toolkit.core import validate_audio_input


def test_valid_audio():
    assert validate_audio_input(20, 1) is True


def test_max_duration():
    assert validate_audio_input(30, 1) is True


def test_too_long():
    assert validate_audio_input(31, 1) is False


def test_stereo_audio():
    assert validate_audio_input(20, 2) is False


def test_zero_duration():
    assert validate_audio_input(0, 1) is False
