
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import warnings  # 오류메시지 안 보이게 하기

# 옵션 사용을 위하여 사용
from selenium.webdriver.chrome.options import Options
# 크롬드라이버 자동설치를 위해서 사용
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By  # 셀레니움 4에서 By 필요
from selenium.webdriver.common.keys import Keys

import time
import os


def stock_crawling(x: int) -> None:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    # 현재작업하는 폴더를 저장/오픈시 사용하게 하는 os
    # 추후에 파일이 있는 폴더에서 바로 작업할때 용이하라고 사용함
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    warnings.filterwarnings("ignore")  # 오류메시지 안 보이게 하기

    options = Options()

    # 브라우저가 항상 켜 있기를 원할때 나중에 닫을때 driver.quit()로 닫는다
    options.add_experimental_option("detach", True)
    # 불필요한 메시지 출력을 방지한다. 예) usb device 오류 나는 메시지 안뜨게 하기 구글링해서 알음
    options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])
    # DevTools listening on ws ~~ 의 메시지 안 뜨게 해줌
    options.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    options.add_argument('headless')  # 실행 화면 안 보이게 처리
    # options.add_argument('--disable-gpu')  # 브라우저의 화면 렌더링 사용 안함
    # user-agent 지정은 headless 탐지하는 것을 막기 위함

    service = Service(ChromeDriverManager().install())

    browser = webdriver.Chrome(
        service=service, options=options)  # 객체생성 browser로 생성

    baseurl = 'https://finance.naver.com/sise/sise_market_sum.naver?sosok=0&page='
    baseurl_kosdaq = 'https://finance.naver.com/sise/sise_market_sum.naver?sosok=1&page='

    # https://finance.naver.com/sise/sise_market_sum.naver?sosok=1&page=2 # 코스닥

    browser.get(baseurl)

    checkboxes = browser.find_elements(By.NAME, 'fieldIds')
    # 브라우저 F12개발자 도구에서 볼때 name이 fieldIds 인 요소들 여러개 elements 를 리스트 checkboxes 로 가져온다
    for checkbox in checkboxes:
        if checkbox.is_selected():
            checkbox.click()

    dict_select = {
        "1": "영업이익",
        "2": "PER",
        "3": "ROE",
        "4": "영업이익증가율",
        "5": "당기순이익",
        "6": "매출액증가율",
        "7": "거래량",
        "8": "외국인비율",
        "9": "시가총액",
        "10": "부채총계",
        "11": "주당순이익",
        "12": "ROA",
        "13": "PBR",
        "14": "유보율"
    }

    selected_items = []
    menu = "영업이익(1) | PER(2) | ROE(3) | 영업이익증가율(4) | 당기순이익(5) | 매출액증가율(6) | 거래량(7) | 외국인비율(8) | 시가총액(9) | 부채총계(10) | 주당순이익(11) | ROA(12) | PBR(13) | 유보율(14)"
    print(menu)
    print("-"*70)
    print("네이버주식 Kospi/Kosdaq의 관심영역 6가지를 크롤링 하는 프로그램입니다")

    flag = 0

    while flag == 0:
        try:
            for i in range(6):
                print("-"*70)
                number = input("관심 번호를 입력하세요. ")
                selected_items.append(dict_select[number])

        except KeyError:
            print("-"*70)
            print("관심번호 입력오류. 처음부터 다시 시작해 주세요")
            break

        print("-"*70)
        f_name = input("저장할 파일명을 입력하세요. 파일은 .csv로 바탕화면에 저장됩니다 : ")
        # path = os.chdir("/")  # 디렉토리 변경
        # path = os.getcwd()  # 현재 작업경로 얻어오기
        # 자신계정 ID를 얻어와야지만 바탕화면 경로를 정확히 파악한다
        username = os.path.expanduser('~')
        f_name = username+'/Desktop/'+f_name + '.csv'

        for checkbox in checkboxes:
            parent = checkbox.find_element(By.XPATH, '..')  # 부모 element 찾기
            label = parent.find_element(By.TAG_NAME, 'label')
            # print(label.text)
            if label.text in selected_items:
                checkbox.click()

        btn_apply = browser.find_element(
            By.XPATH, '//*[@id="contentarea_left"]/div[2]/form/div/div/div/a[1]/img')
        btn_apply.click()

        for idx in range(1, 40):

            browser.get(baseurl + str(idx))
            # 필요한 데이터가 [1] 에 있음 df[0] df[1] 등을 치면서 확인한 사항
            df = pd.read_html(browser.page_source)[1]
            # 줄 전체가 비어있을때 지우라. how='any' 하나라도 비어있으면 지우라 .. inplace 데이터 프레임에 반영하기 true
            df.dropna(axis='index', how='all',
                      inplace=True)  # index 는 row를 말한다
            # columns 는 columns 을 말한다
            df.dropna(axis='columns', how='all', inplace=True)
            if len(df) == 0:
                break
            if os.path.exists(f_name):
                df.to_csv(f_name, encoding='utf-8-sig', index=False,
                          mode='a', header=False)  # index는 앞의 1,2,3,4, 번호들
            else:
                df.to_csv(f_name, encoding='utf-8-sig', index=False)

        for idx in range(1, 40):
            browser.get(baseurl_kosdaq + str(idx))
            # 필요한 데이터가 [1] 에 있음 df[0] df[1] 등을 치면서 확인한 사항
            df = pd.read_html(browser.page_source)[1]
            # 줄 전체가 비어있을때 지우라. how='any' 하나라도 비어있으면 지우라 .. inplace 데이터 프레임에 반영하기 true
            df.dropna(axis='index', how='all',
                      inplace=True)  # index 는 row를 말한다
            # columns 는 columns 을 말한다
            df.dropna(axis='columns', how='all', inplace=True)
            if len(df) == 0:
                break

            if os.path.exists(f_name):
                df.to_csv(f_name, encoding='utf-8-sig', index=False,
                          mode='a', header=False)  # index는 앞의 1,2,3,4, 번호들
            else:
                df.to_csv(f_name, encoding='utf-8-sig', index=False)

            # utf-8-sig 로 하면 pandas로 엑셀로 불러 올때 한글이 깨지지 않는다 . csv 파일

            # print(f'{idx} 페이지완료')
        flag = 1

    browser.quit()


if __name__ == "__main__":
    print(f'Stock Crawling')
    stock_crawling()
