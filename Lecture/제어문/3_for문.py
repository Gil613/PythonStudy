#시퀀스 자료형을 출력할때 유용하다
# for문은 특정 조건에 대해 반복한다.
"""
for 변수 in 시퀀스자료 :
    실행할 코드
"""

list1 = [1,2,3,4]
for i in list1 :
    i

list2 = [(1,2),(3,4),(5,6)]
for first, last in list2 :
    print(f"({first} , {last})")

# continue는 for문의 처음으로 돌아가게 하는 함수이다
for i in list1 :
    if i > 2 : 
        continue
    print("i는 2보다 크다")

# range는 n 부터 k미만의 숫자를 포함하는 객체를 만들어준다.
#range(끝)
#range(시작,끝)
#range(시작,끝,단계)
range_test = range(1,11) #1부터 10까지의 객체

for i in range(1,11) :
    print(f"{i}만큼 반복중 ")


for a in range(10):
    print(a)


#리스트 컴프리헨션 https://school.programmers.co.kr/learn/courses/30/lessons/120809
#리스트안에 리스트 컴프리헨션을 사용하면 좀 더 편리하고 직관적인 코드를 만들 수 있다.
#[표현식 for 항목 in 시퀀스자료형]
'''
리스트 각 항목에 3을 곱한 결과를 반환하는 예제이다
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
'''
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)


# if문도 사용 가능
result1 = [num * 2 for num in a if num % 2 != 0]

# 여러 줄 사용 가능
result3 = [x * y for x in range(2,10)
                 for y in range(1,10)]