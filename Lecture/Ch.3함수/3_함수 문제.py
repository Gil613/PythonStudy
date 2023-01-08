# 로또 예상 번호 추출 프로그램을 만들어보자
# 1. 로또 번호 6개를 생성한다.
# 2. 로또 번호는 1~45까지의 랜덤한 번호다.
# 3. 6개의 숫자 모두 달라야한다.
# 4. getRandomNumber() 함수를 사용해서 구현한다.
import random

def get_random_number():
    temp = []
    cnt = 0
    while True:
        number = random.randint(1,45)
        if cnt >= 6:
            break
        if number not in temp:
            temp.append(number)
            cnt += 1
    result = sorted(temp)
    return result

print(get_random_number())