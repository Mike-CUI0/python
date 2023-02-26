import math


def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


if __name__ == "__main__":
    x = int(input('x : '))
    y = int(input('y : '))
    print(f'최대공약수는 {gcd(x,y)} 입니다')
