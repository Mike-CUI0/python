import smtplib
from email.mime.multipart import MIMEMultipart  # 영어 이외 언어는 mike 포맷으로 변경해야 함
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication  # 일반파일첨부
from email.mime.image import MIMEImage  # 이미지 파일 첨부


# # 데이터 파일 첨부하기
# from email.mime.application import MIMEApplication # 메일의 첨부 파일을 base64 형식으로 변환

# file_name = "file.xlsx"

# with open(file_name, 'rb') as excel_file :
#     attachment = MIMEApplication( excel_file.read() )
#     #첨부파일의 정보를 헤더로 추가
#     attachment.add_header('Content-Disposition','attachment', filename=file_name)
#     msg.attach(attachment)

# # 이미지 파일 추가
# from email.mime.image import MIMEImage # 메일의 이미지 파일을 base64 형식으로 변환

# image_name = "image.png"
# with open(image_name, 'rb') as fp:
#     img = MIMEImage(fp.read())
#     img.add_header('Content-Disposition','attachment', filename=image_name)
#     msg.attach(img)

import csv

with open("C:/Users/kkich/Desktop/Python_prg/Excel_openpyxl/letter.txt", "r", encoding="utf-8") as file:
    letter = file.read()

with open(r"C:\Users\kkich\Desktop\Python_prg\Excel_openpyxl\email_address.csv", "r", encoding="utf-8-sig") as file:
    # csv로 읽어온 file을 list 화 해서 mail_list에 리스트로 넣는다
    # r 은 raw string 로 있는 그대로 읽어달라는 뜻
    mail_list = list(csv.reader(file))

my_mail = "xxxx@gmail.com"
pwd = "xxxx"
# to_mail = "kkichumi@naver.com"
attach_file_name = r"C:\Users\kkich\Desktop\Python_prg\Excel_openpyxl\email_address.csv"
image_name = r"C:\Users\kkich\Desktop\Python_prg\Excel_openpyxl\regexp.png"

for name, to_mail in mail_list:  # 리스트화 해서 나오는 자료와 밑에 미리 해 놓은 변수와의 일치를 위해서 name , to_mail 이라고 해서 iterate을 사용함

    msg = MIMEMultipart()  # 메일보낼때 들어가는 가장 기본적인 내용
    msg['Subject'] = "출장보고서 pdf변환 후 파일 첨부 전송"
    msg['From'] = my_mail
    msg['To'] = to_mail

    content = letter.replace("[name]", name)

    # 읽어온 파일을 letter에 넣었고 letter안의 [name]을 리스트 안의 name으로 변환후 그 content를 text에 넣은 후 msg.attach(text)로 보내기
    text = MIMEText(content)
    msg.attach(text)  # msg 개체에 어태치

    # 먼저 text 본문을 보낸 후 파일 첨부해서 보내는 작업을 아래와 같이 rb 해서 진행함
    with open(attach_file_name, 'rb') as excel_file:
        attachment = MIMEApplication(excel_file.read())
        # 첨부파일의 정보를 헤더로 추가
        attachment.add_header('Content-Disposition',
                              'attachment', filename=attach_file_name)
        msg.attach(attachment)
        # 파일을 첨부해서 보낸다. msg.attach(첨부파일)

    with open(image_name, 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition',
                       'attachment', filename=image_name)
        msg.attach(img)

    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(user=my_mail, password=pwd)
    # string 문자열로 변환해서 송부, html 로 가거나 첨부파일도 할 수 있음
    smtp.sendmail(my_mail, to_mail, msg.as_string())
    smtp.close()

    print(name, "전송완료")
