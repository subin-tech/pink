# API

`validate_notes()`는 음표 목록을, `validate_semitones()`는 반음 이동 값을 검증합니다. 나머지 함수는 호출하면 `NotImplementedError`가 발생합니다.

::: music_toolkit.core
    options:
      members:
        - validate_notes
        - load_audio
        - transcribe_notes
        - transpose_notes
        - summarize_transposition
        - create_score
        - save_score
        - validate_semitones
        - validate_audio_input
