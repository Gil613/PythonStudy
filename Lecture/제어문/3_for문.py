# for문은 특정 조건에 대해 반복한다.
"""
for 변수 in 리스트 :
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

range_test = range(1,11) #1부터 10까지의 객체

for i in range(1,11) :
    print(f"{i}만큼 반복중 ")