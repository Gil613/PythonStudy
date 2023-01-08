# 비교연산자란 두 값을 비교하는 연산자이다
"""
<
>
==
!=
>=
<=
"""

#논리 연산자
"""
and
or
not
"""

#멤버 연산자
"""
x in a
x not in a
"""

#if문은 주어진 조건을 판단하여 상황에 맞게 처리될 수 있게끔 해준다. (분기처리)

#if문 형태
"""
if 조건 : 실행 될 코드
elif 조건 : 실행 될 코드
else : 실행 될 코드
"""

#조건에 대한 실행 코드가 간단하면 한 줄로 써도 무관하지만 두 줄 이상의 코드라면 들여쓰기를 해야 한다
"""
if 조건 : 
    실행코드 1
    실행코드 2
"""

#조건문에서 어떠한 조건에 따라 아무런 행동을 하지 않을때 pass를 사용한다
"""
if 조건 : 
    pass
else :
    print("123")
"""

# 유저 패스워드 체크하기
# def pwd_check(__value__):
#     user_pwd = '1234'
#     if __value__ == user_pwd:
#         print("로그인 성공")
#     else : print("비밀번호를 확인해주세요")

# pwd_check('1234')




#https://school.programmers.co.kr/learn/courses/30/lessons/120808
# num1 = 2
# denum1 = 1
# num2 = 4
# denum2 = 3
# answer = []
# num3 = num1 * num2
# denum3 = 0
# if num1 < num2 : 
#     denum3 = (denum1 * num2) + (denum2 * num1)
 
# elif num1 == num2 : 
#     denum3 = denum1 + denum2
 

# for i in range(2, num3+1,2):
#     if denum3 % i == 0 :
#         a = num3 / i
#         b = denum3 / i
# answer.append(b)
# answer.append(a)
# answer
# https://school.programmers.co.kr/learn/courses/30/lessons/120811
# def sort(array):
#     sort_array = []
#     for j in range(len(array)):
#         i = len(array) - j
#         for k in range(1,i):
#             if array[k-1] >= array[k]:
#                 sort_array = array[k-1]
#                 array[k-1] = array[k]
#                 array[k] = sort_array

#     return array

# def solution(array):
#     array1 = sort(array)

#     print(array1[len(array1) // 2])

# array = [6,3,5,1,2]

# solution(array)

# 가위바위보
import random

def 가위바위보(value):
    if value == 1:
        print("asf")
    elif value == 2:
        print("")
    elif value == 3:
        print("")


while True:
    choose = ['1. 가위', '2. 바위', '3. 보']
    choose1 = {1 : '가위', 2 : '바위', 3 : '보'}
    choose_number = int(input(f"{choose1} 원하는 숫자를 입력해주세요"))
    computer_choose = random.random
    print(computer_choose)
    # if choose_number not in choose1.keys():
    #     print("다시 입력해주세요")
    # else:
    #     가위바위보(choose_number)





