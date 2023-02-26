

import itertools
import zipfile
import time

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

i = 0

start = time.time()


#zFile = zipfile.ZipFile(r'C:\Users\kkich\Desktop\python_40 exaples\test.zip')
"""
for len in range(1, 6):
    to_attempt = itertools.product(passwd_string, repeat=len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        # print(passwd)

        try:
            zFile.extractall(pwd=passwd.encode())
            print(f"비밀번호는 {passwd} 입니다.")
            break
        except:
            pass
"""

for l in range(1, 500000):
    i += i
    i += 1
end = time.time()

sec1 = end - start
min1 = sec1/60
print(f'{sec1:.2f}초 , {min1:.2f}분이 걸렸습니다')
