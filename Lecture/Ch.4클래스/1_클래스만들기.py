#클래스 생성 및 호출해보기

class Cocktail: # 부모클래스
    def __init__(self, sour, sweet, ice, bitter, method):
        self.sour = sour
        self.sweet = sweet
        self.ice = ice
        self.bitter = bitter
        self.method = method
        print("초기화됐음")
    
    def tipsy(self):
        print("알딸딸하다.")

    def get_happy(self):
        print("행복하다")
        
#인스턴스화 => 호출
# old_fashioned = Cocktail(False, True, True, True, "stir")

#상속 사용해보기
class Vinchaud(Cocktail): # 자식클래스
    def dummy_method():
        print("dummy")
# hot_wine_cocktail = Vinchaud(True, True, False, True, "boil")
# hot_wine_cocktail.tipsy()
# hot_wine_cocktail.get_happy()

#오버라이딩, 클래스변수
class Fizz(Cocktail):
    def __init__(self, sour, sweet, ice, bitter, soft_drink, method):
        super().__init__(sour, sweet, ice, bitter, method)
        self.sour = sour
        self.sweet = sweet
        self.ice = ice
        self.bitter = bitter
        self.soft_drink = soft_drink
        self.method = method
        print("오버라이딩!")
     

gin_fizz = Fizz(True, True, True, False, "soda", "shake")

gin_fizz.tipsy()