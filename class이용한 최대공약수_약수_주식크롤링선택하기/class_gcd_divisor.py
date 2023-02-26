from enum import Enum
from typing import Any
import mike_divisor
import mike_gcd
from crawling_stock_01 import stock_crawling

Menu = Enum('Menu', ['gcd', 'divisor', '주식크롤링', 'stop'])


def select_menu() -> Menu:
    print("-"*70)
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ', end='')
        n = int(input(': '))
        print("-"*70)

        if 1 <= n <= len(Menu):
            return Menu(n)


while True:
    judge = select_menu()

    if judge == Menu.gcd:
        x = int(input('두수의 공약수 구하기 첫번째 수 : '))
        y = int(input('두수의 공약수 구하기 두번째 수 : '))
        print(f'최대공약수는 {mike_gcd.gcd(x,y)} 입니다')

    elif judge == Menu.divisor:
        x = int(input('약수를 구할 정수를 입력하세요 : '))
        mike_divisor.divisor(x)

    elif judge == Menu.주식크롤링:
        print(f'Stock Crawling')
        stock_crawling(3)

    elif judge == Menu.stop:
        break
