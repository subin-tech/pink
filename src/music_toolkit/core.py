"""Proposed interfaces for transcription and score transposition.

The functions are documentation-only stubs and are not implemented yet.
"""

from typing import TypedDict


class Note(TypedDict):
    """A MIDI pitch and its start and end times in seconds."""

    pitch: int
    start: float
    end: float


def load_audio(path: str) -> tuple[list[float], int]:
    """Load a mono WAV recording and normalize audio samples to the range[-1,1].

    Args:
        path (str): Path to a mono WAV file of at most 30 seconds.

    Returns:
        tuple[list[float], int]: Audio samples between -1 and 1 and the sample rate in Hz.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not a supported mono WAV or exceeds 30 seconds.

    Examples:
        >>> samples, sample_rate = load_audio("melody.wav")
        >>> sample_rate
        44100

    Note:
        The example assumes a suitable file with a 44100 Hz sample rate.
        This function is not implemented yet.
    """
    raise NotImplementedError


def transcribe_notes(samples: list[float], sample_rate: int) -> list[Note]:
    """Estimate notes from a single-instrument recording.

    Args:
        samples (list[float]): Mono audio samples normalized between -1 and 1.
        sample_rate (int): Number of samples per second; must be positive.

    Returns:
        list[Note]: Estimated MIDI pitches and start and end times in seconds.

    Raises:
        ValueError: If samples are empty or the sample rate is not positive.

    Examples:
        >>> notes = transcribe_notes(samples, 44100)
        >>> notes[0]  # Example result; actual recognition varies.
        {'pitch': 60, 'start': 0.0, 'end': 0.5}

    Note:
        Transcription can be inaccurate, especially for overlapping notes.
        This function is not implemented yet.
    """
    raise NotImplementedError


def transpose_notes(notes: list[Note], semitones: int) -> list[Note]:
    """Shift all MIDI pitches by the requested number of semitones.

    Args:
        notes (list[Note]): Notes with MIDI pitches and times in seconds.
        semitones (int): Signed number of semitones to move each pitch.

    Returns:
        list[Note]: New notes with shifted pitches and unchanged times.

    Raises:
        ValueError: If a resulting MIDI pitch is outside the range 0 to 127.

    Examples:
        >>> transpose_notes([{'pitch': 60, 'start': 0.0, 'end': 0.5}], 2)
        [{'pitch': 62, 'start': 0.0, 'end': 0.5}]

    Note:
        This function is not implemented yet.
    """
    raise NotImplementedError


def summarize_transposition(
    original_notes: list[Note],
    transposed_notes: list[Note],
) -> list[tuple[int, int]]:
    """Pair each original MIDI pitch with its transposed pitch.

    Args:
        original_notes (list[Note]): Notes in their original order.
        transposed_notes (list[Note]): Corresponding notes in the same order.

    Returns:
        list[tuple[int, int]]: One (original pitch, transposed pitch) pair
            per note, in input order. Two empty lists yield an empty list.

    Raises:
        ValueError: If the two lists have different lengths.

    Examples:
        >>> original = [{'pitch': 60, 'start': 0.0, 'end': 0.5}]
        >>> changed = [{'pitch': 62, 'start': 0.0, 'end': 0.5}]
        >>> summarize_transposition(original, changed)
        [(60, 62)]

    Note:
        The example shows the planned behavior. This stub raises
        NotImplementedError on every call.
    """
    raise NotImplementedError


def create_score(notes: list[Note], tempo: int = 120) -> str:
    """Create a MusicXML score from notes at a fixed tempo.

    Args:
        notes (list[Note]): MIDI pitches with start and end times in seconds.
        tempo (int): Tempo in beats per minute; must be positive. Defaults to 120.

    Returns:
        str: MusicXML document containing the converted notes.

    Raises:
        ValueError: If tempo is not positive or a note has invalid pitch or times.

    Examples:
        >>> score = create_score([{'pitch': 60, 'start': 0.0, 'end': 0.5}])
        >>> '<score-partwise' in score
        True

    Note:
        The first version uses a fixed tempo and may require manual rhythm correction.
        This function is not implemented yet.
    """
    raise NotImplementedError


def save_score(score: str, path: str) -> str:
    """Save a MusicXML document to a new file.

    Args:
        score (str): MusicXML document to save.
        path (str): Destination path ending in .musicxml.

    Returns:
        str: Path of the saved MusicXML file.

    Raises:
        ValueError: If the destination does not end in .musicxml.
        FileExistsError: If the destination already exists.
        OSError: If the file cannot be written.

    Examples:
        >>> save_score(score, 'melody_transposed.musicxml')
        'melody_transposed.musicxml'

    Note:
        This function is not implemented yet.
    """
    raise NotImplementedError
