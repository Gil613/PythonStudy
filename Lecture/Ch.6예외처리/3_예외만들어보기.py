#raise 구문 사용법 -> 에러를 강제로 발생시키기 위함
#raise 예외("에러메세지")
# raise Exception
# raise Exception("내가 만든 예외")

# try:
#     num = int(input("음수받기"))
#     if num >= 0:
#         raise Exception("양수는 입력 불가입니다.")
# except Exception as e:
#     print("에러발생", e)


# try:
#     num = int(input("음수받기"))
#     if num >= 0:
#         raise ValueError("양수는 입력 불가입니다.")
# except Exception as e:
#     print("에러발생", e)
#예외 구조


#에러 만들기
# class 예외(Exception):
#     def __init__(self):
#         super()__init__("에러메세지")

class PositiveNumberError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

try:
    num = int(input("음수받기"))
    if num >= 0:
        raise PositiveNumberError
except:
    print("예외발생")