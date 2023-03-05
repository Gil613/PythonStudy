from service import loginService

def home():

    print("블로그에 오신걸 환영합니다. \n 숫자를 선택해주세요")
    choose = input("1. 회원가입 , 2. 로그인 => ")
    if choose == '1' :
        print("=====회원가입을 진행합니다=====")
        loginService.signIn()
    elif choose == '2' :
        print("=====로그인을 진행합니다=====")
        loginService.joinIn()
    else:
        print("올바르지 않은 번호입니다. \n 처음으로 돌아갑니다.")
        home()
home()