# API

`validate_notes()`는 음표 목록을 검증하고, `create_score()`는 음표와 템포를 받아 MusicXML 문자열을 생성합니다. 나머지 함수들은 아직 구현되지 않았으며 호출하면 `NotImplementedError`가 발생합니다.

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
