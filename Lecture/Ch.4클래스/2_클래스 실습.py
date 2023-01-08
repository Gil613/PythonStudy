# RPG게임을 만드는 중 아이템에 대한 설계도를 토대로 만들어보자.
# 아이템 공통 : 이름, 가격, 무게, 판매하기, 버리기(버리기 가능할때만)
# 장비 아이템 : 착용효과, 착용하기
# 소모품 아이템 : 사용효과, 사용하기

class Item:
    def __init__(self, name, price, weight, sale, is_drop_able):
        self.name = name    
        self.price = price    
        self.weight = weight
        self.sale = sale
        self.is_drop_able = is_drop_able

    def sales(self):
        print(f"{self.sale}원에 판매되었습니다.")

    def drop(self):
        if self.is_drop_able:
            print("버린다.")
        else :
            pass

class WareableItem(Item):
    def __init__(self, name, price, weight, sale, is_drop_able,effect):
        super().__init__(name, price, weight, sale, is_drop_able)
        self.effect = effect

    def wear(self):
        print(f"{self.name}(을)를 착용했습니다 {self.effect}의 효과를 얻었다.")

class UsableItem(Item):
    def __init__(self, name, price, weight, sale, is_drop_able, effect):
        super().__init__(name, price, weight, sale, is_drop_able)
        self.effect = effect

    def use(self):
        print(f"{self.name}을(를) 사용했습니다.")


sword = WareableItem("집행자의 검+5", 100000000, 0.35, 50000000, True, "모든 능력치 5상승")

sword.sales()