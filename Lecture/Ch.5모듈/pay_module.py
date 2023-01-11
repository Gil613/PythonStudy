#결제 정보 모듈
# 변수
version = 2.0

#함수
def printAuthoor():
    return print("스타트코딩")

#클래스
class Pay:
    def __init__(self, id, date, price):
        self.id = id
        self.date = date
        self.price = price
    def get_pay_info(self):
        return f"{self.id}, {self.date}, {self.price}"


if __name__ == '__main__':
    print("pay_module입니다.")