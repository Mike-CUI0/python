import re
import os


def makelines(x: int) -> None:
    print("-"*x)


# 현재작업하는 폴더를 저장/오픈시 사용하게 하는 os
# 추후에 파일이 있는 폴더에서 바로 작업할때 용이하라고 사용함
os.chdir(os.path.dirname(os.path.abspath(__file__)))

log_file = ["auth.log", "access.log"]

# 정규식 패턴에서 3으로 시작하는 IP는 찾고자 하는 IP가 아니기에 [^3] 3이 없는 것을 IP_PATTERN 으로 넣음
# (\d{1,3}\.){3}\d{1,3}
# IP_PATTERN = r"\d{1,3}[^110]\.\d{1,3}\.\d{1,3}\.\d{1,3}"
# 19로 시작하는 세자리 숫자 앞에 19가 있으니까 {1} 이 됨
# 1로 시작하는 세자리 \1.d{2}
# 1로 시작하며 두번째 자리 숫자가 0~4 사이의 세자리 숫자 2[0-4]\d

IP_PATTERN = r"19\d{1}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

for i in range(2):
    with open(log_file[i], "r") as f:
        log = f.read()
        ips = re.findall(IP_PATTERN, log)

        ip_counts = {}

        for ip in ips:
            if ip in ip_counts:
                ip_counts[ip] += 1
            else:
                ip_counts[ip] = 1
        if i == 1:
            top_ip = sorted(ip_counts.items(),
                            key=lambda x: x[1], reverse=True)[:20]
        else:
            top_ip = sorted(ip_counts.items(),
                            key=lambda x: x[1], reverse=True)[:10]

    line_count = "총 접속IP는 {len(ip_counts)}개 입니다"
    makelines(len(line_count))
    print(f"{log_file[i]}파일의 IP주소")
    makelines(len(line_count))

    for ip, count in top_ip:
        # 출력시의 포맷을 맞추어 주기 위해서 정수형 4자리수 :4d 를 넣음
        print(f'{count:4d}번 접속IP : {ip}')

    makelines(len(line_count))
    print(f"총 접속IP는 {len(ip_counts)}개 입니다")
    makelines(len(line_count))
