# 🎧 Discord Voice Server IP Resolver

> Discord 통화방(Voice Channel)의 서버 ID를 입력하면 실제 연결되는 서버의 IP를 `클라우드플레어` API를 이용하여 확인할 수 있는 Python 도구입니다.

---

## 📦 기능 소개

- 디스코드 음성 통화 서버 ID → `.discord.gg` 도메인 생성
- 클라우드플레어를 통해 도메인을 IP로 변환
- nslookup처럼 동작하지만 웹 기반 API 사용
- 서버 위치 분석, 응답속도 확인 등에 활용 가능

---

## 🔎 서버 아이디 추출하는 법

> 음성채널에 연결하게 되면 아래 사진처럼 음성 연결됨이 뜹니다.

[사진](https://raw.githubusercontent.com/linsae123/discord-voice-server-ip/main/assets/screen.png)

> 음성 연결됨에 클릭을 하면 서버 아이디가 나옵니다.

[사진](https://raw.githubusercontent.com/linsae123/discord-voice-server-ip/main/assets/screen2.png)

---

## 🖥️ 사용 예시

```bash
$ python voice_server_resolver.py
🎧 디스코드 음성 서버 ID로 IP 확인기
예시 입력: japan289, syd108, singapore221 등
🔧 서버 ID 입력: japan289
🔍 생성된 도메인: japan289.discord.gg
✅ japan289.discord.gg → IP 주소: 162.159.130.45
```

---

## 📫 Contact
- Discord: _linsae