import requests
import socket

def resolve_ip_dns(domain):
    url = f"https://1.1.1.1/dns-query?name=${domain}&type=A"
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        data = response.json()
        answers = data.get("Answer", [])
        ip = next((a["data"] for a in answers if a["type"] == 1), None)
        return ip
    except Exception as e:
        print(f"❌ DNS 조회 중 오류 발생: {e}")
        return None

def main():
    server_id = input("디스코드 음성 서버 아이디를 입력하세요(README에 설명됨) : ")

    ip = resolve_ip_dns(server_id)

    if ip:
        print(f"아이피가 추출되었습니다. {ip}")
    else:
        print("아이피 주소를 찾지 못했습니다.")
