from . import boardService

#유저 데이터
userData = {'test' : '1234'}

def signIn():
    user_id = input("아이디를 입력해주세요 : ")

    if user_id in userData.keys():
        print("중복된 아이디 입니다.")
        signIn() #재귀함수

    user_pwd = input("패스워드를 입력해주세요 : ")
    #유저데이터에 자장
    userData[user_id] = user_pwd
    print("=====회원가입을 완료했습니다=====")
    print("=====로그인을 진행합니다=====")
    joinIn()

def joinIn():
    user_id = input("아이디를 입력해주세요 : ")
    user_pwd = input("패스워드를 입력해주세요 : ")
    if user_id not in userData.keys():
        print("아이디가 존재하지 않습니다.")
        joinIn() #재귀함수
    #비밀번호가 일치하지 않을경우
    elif user_pwd not in userData[user_id]:
        print("비밀번호가 일치하지 않습니다.")
        joinIn()

    print("로그인이 완료되었습니다.")
    print("번호를 입력해주세요.")
    choose = input("1. 글 작성, 2. 게시글 목록 =>")

    if choose == '1':
        boardService.write(user_id)
