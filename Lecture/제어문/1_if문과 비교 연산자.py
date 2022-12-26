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



# 유투버로부터 현재 구독자 수를 입력하면 수익창출이 가능한지 불가능한지 알려주는 프로그램 제작을 요청받았다.
# 수익창출은 1,000명 이상일 경우 가능하며, "현재 구독자 수를 입력하세요" 라는 문구와 함께 숫자를 입력했을 경우 "수익 창출이 가능합니다!", 
# "수익 창출이 불가능합니다! 부족한 구독자 수는 00명입니다."  라는 안내 문구가 출력되도록 기획하였다.

def subscriber_check():
    user_cnt_now = input("현재 구독자 수를 입력해주세요")
    if user_cnt_now >= 1000 : print("수익 창출이 가능합니다.")
    else : print(f"수익 창출이 불가능합니다!\n부족한 구독자 수는 {1000 - user_cnt_now}명 입니다.")

subscriber_check()