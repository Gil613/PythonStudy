#원화를 입력, 환율을 입력 -> 달러값을 출력해주는 프로그램

won = int(input("금액을 입력해 주세요"))

odd = int(input("환율을 입력해 주세요"))

try:
    print(int(won) / int(odd))
except ZeroDivisionError as e:
    print("0이상의 숫자를 입력해주세요", e)
except:
    print("숫자만 입력해주세요")
