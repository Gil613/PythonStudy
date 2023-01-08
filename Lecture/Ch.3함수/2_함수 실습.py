
#함수 호출 방법
def multiply(x, y):
    result = x * y
    return result

multiply(3,4)


# 출력을 보고 함수를 구성해보기
# a b c 합계를 구하고 평균을 반환하는 함수
# 출력 값
# -> 합계 : 60, 평균 : 20

def print_sum_avg(a, b, c):
    """
    a b c의 합계를 구하고 평균을 계산해주는 함수
    """
    result = a + b + c
    print(f"합계 : {result}, 평균 : {result // 3}")


print_sum_avg(10, 20, 30)

print()