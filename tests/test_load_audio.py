
import wave
import pytest

from music_toolkit.core import load_audio


def make_wav(path, channels=1, seconds=1):
    sample_rate = 8000

    with wave.open(str(path), "wb") as audio:
        audio.setnchannels(channels)
        audio.setsampwidth(2)
        audio.setframerate(sample_rate)
        audio.writeframes(
            b"\x00\x00" * (sample_rate * seconds * channels)
        )


def test_valid_wav(tmp_path):
    path = tmp_path / "valid.wav"
    make_wav(path)

    samples, sample_rate = load_audio(str(path))

    assert sample_rate == 8000
    assert len(samples) == 8000
    assert all(-1 <= sample <= 1 for sample in samples)


def test_stereo_wav(tmp_path):
    path = tmp_path / "stereo.wav"
    make_wav(path, channels=2)

    with pytest.raises(ValueError):
        load_audio(str(path))


def test_too_long_wav(tmp_path):
    path = tmp_path / "long.wav"
    make_wav(path, seconds=31)

    with pytest.raises(ValueError):
        load_audio(str(path))


def test_missing_wav(tmp_path):
    path = tmp_path / "missing.wav"

    with pytest.raises(FileNotFoundError):
        load_audio(str(path))
