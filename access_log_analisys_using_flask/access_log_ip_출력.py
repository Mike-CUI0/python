import re
import os

# 현재작업하는 폴더를 저장/오픈시 사용하게 하는 os
# 추후에 파일이 있는 폴더에서 바로 작업할때 용이하라고 사용함
os.chdir(os.path.dirname(os.path.abspath(__file__)))

log_file = "auth.log"

list = []

with open(log_file, "r") as f:
    for line in f:
        # 정규식 표현 \d 숫자 {1,3} 1에서 3자리 , \.  .과 일치
        match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        if match:
            # 찾아낸 그룹중에서 0번째가 가장 같은 ip라고 보고 ip_address로 리스트 이동
            ip_address = match.group(0)
            list.append(ip_address)
            print(ip_address)
