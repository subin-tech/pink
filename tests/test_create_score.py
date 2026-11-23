from xml.etree import ElementTree

import pytest

from music_toolkit.core import create_score


def test_middle_c_quarter_second_is_an_eighth_note_at_120_bpm():
    notes = [{"pitch": 60, "start": 0.0, "end": 0.25}]

    score = ElementTree.fromstring(create_score(notes, tempo=120))

    pitched_notes = score.findall("./part/measure/note[pitch]")
    assert len(pitched_notes) == 1
    note = pitched_notes[0]
    assert note.findtext("pitch/step") == "C"
    assert note.findtext("pitch/octave") == "4"
    assert float(note.findtext("pitch/alter", "0")) == 0

    # MusicXML expresses duration in divisions per quarter note.
    divisions = int(score.findtext("./part/measure/attributes/divisions"))
    assert divisions > 0
    assert 2 * int(note.findtext("duration")) == divisions


def test_zero_tempo_raises_value_error():
    notes = [{"pitch": 60, "start": 0.0, "end": 0.25}]

    with pytest.raises(ValueError):
        create_score(notes, tempo=0)


def test_rounded_onsets_chords_and_overlaps_at_60_bpm():
    notes = [
        {"pitch": 65, "start": 1.0, "end": 1.01},
        {"pitch": 61, "start": 0.26, "end": 1.5},
        {"pitch": 64, "start": 0.26, "end": 1.5},
    ]
    measure = ElementTree.fromstring(create_score(notes, 60)).find("./part/measure")
    assert measure.find("sound").get("tempo") == "60"
    cursor = 0
    events = []
    for item in measure:
        duration = int(item.findtext("duration", "0"))
        if item.tag == "backup":
            cursor -= duration
        elif item.tag == "forward":
            cursor += duration
        elif item.tag == "note":
            if item.find("chord") is None:
                onset = cursor
                cursor += duration
            events.append((onset, duration, item.findtext("pitch/step"),
                           item.findtext("pitch/alter", "0"), item.findtext("voice")))
    assert events == [(1, 2, "C", "1", "1"), (1, 2, "E", "0", "1"),
                      (2, 1, "F", "0", "2")]


@pytest.mark.parametrize("note", [
    {"pitch": 128, "start": 0.0, "end": 0.5},
    {"pitch": 60, "start": 0.5, "end": 0.5},
    {"pitch": 60, "start": 0.0, "end": float("inf")},
])
def test_invalid_notes_raise_value_error(note):
    with pytest.raises(ValueError):
        create_score([note])
