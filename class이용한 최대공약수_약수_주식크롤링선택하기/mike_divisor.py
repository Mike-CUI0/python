
def divisor(x: int) -> None:

    list2 = []
    print("곱셉의 구성은 ", end=' ')
    for i in range(1, x+1):
        if i != 1 and i != x:
            if x % i == 0:
                if x // i not in list2:
                    list2.append(x // i)
                    list2.append(i)
                    print(f'[{x//i}, {i}]', end=' ')
        i += 1

    print()
    # print(f"구성정수는 {list2}")
    print(f"구성정수는 {sorted(list2)} ")
    # sorted 함수는 리스트 자체가 바뀌는것이 아니라 잠시 정렬해서 출력만 해줌. 원본인 list2 는 변하지 않음
    # print(f"구성정수는 {list2.sort()} ") # sort() 메소드는 아무것도 리턴시키지 않음. None을 리턴함


if __name__ == "__main__":
    x = int(input('x : '))
    divisor(x)

# def getMyDivisor(n):

#     divisorsList = []

#     for i in range(1, n + 1):
#         if (n % i == 0):
#             divisorsList.append(i)

#     return divisorsList


# print(getMyDivisor(x))
