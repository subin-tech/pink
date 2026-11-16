# MelodifyAI

짧은 악기 연주를 음표로 옮기고 조를 바꾸는 Python 라이브러리입니다.

> 개발 중인 프로젝트입니다. 음원 채보, 조 변환과 MusicXML 저장은 아직 구현되지 않았습니다.

## 1. What it does

30초 이내의 단일 악기 모노 WAV 음원을 입력받아 음표를 추정하고, 사용자가 지정한 반음 수만큼 음높이를 바꿔 MusicXML 악보로 저장하는 것을 목표로 합니다. 음질이나 겹친 음에 따라 채보가 부정확할 수 있으므로 사용자가 결과를 직접 확인해야 합니다.

## 2. Installation

패키징과 TestPyPI 배포를 준비 중입니다. 아직 `pip install`로 설치할 수 없습니다.

현재 구현된 코드를 확인하려면 저장소를 복제한 뒤 프로젝트 폴더에서 아래 Quick start를 실행합니다.

```bash
git clone https://github.com/subin-tech/pink.git
cd pink
```

## 3. Quick start

현재 구현된 `validate_notes()`는 MIDI 음높이와 시작·종료 시간이 유효한지 확인합니다. 아래 명령은 macOS 또는 Linux 터미널에서 저장소 루트를 기준으로 실행합니다.

```bash
PYTHONPATH=src python3 -c "from music_toolkit.core import validate_notes; validate_notes([{'pitch': 60, 'start': 0.0, 'end': 0.5}]); print('유효한 음표입니다')"
```

음원 입력부터 악보 생성까지의 예제는 해당 기능 구현 후 추가합니다.

## 4. Dependencies

현재 구현된 `validate_notes()`는 Python 표준 라이브러리만 사용합니다. 음원 분석과 MusicXML 생성에 사용할 외부 라이브러리는 선정 후 이름과 라이선스를 기록합니다.

## 5. Tests

TODO: 자동 테스트와 실행 방법을 추가합니다.

## 6. Documentation

- [문서 사이트](https://subin-tech.github.io/pink/)
- [API 문서](https://subin-tech.github.io/pink/api/)
- [프로젝트 제안서](docs/proposal.md)

## 7. Release

TODO: 패키지 이름, TestPyPI 배포와 버전 관리 방법을 정리합니다.

## 8. Team

- 박수빈 — [@subin-tech](https://github.com/subin-tech)
- 박서준 — [@gosu1](https://github.com/gosu1)
- 최라엘 — [@lael0805-ctrl](https://github.com/lael0805-ctrl)
- 김은민 — [@kimmmon2](https://github.com/kimmmon2)
- 오준혁 — [@ojh2465](https://github.com/ojh2465)

협업 방법은 [팀 규칙](docs/team-rules.md)을 따릅니다. 팀원들은 Codex를 사용하며, PR마다 AI 사용 내역과 직접 확인한 내용을 기록합니다.

## 9. License

[MIT License](LICENSE)를 사용합니다.
