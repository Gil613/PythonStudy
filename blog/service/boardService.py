#key : ID, value : [title,text,writer(user id)] (외래키, 참조키)

boardData = {}


def write(writer):
    id = 0
    print("=====글을 작성합니다.=====")
    title = input("글 제목을 입력해주세요.")
    text = input("글 내용을 입력해주세요.")
    boardData[0] = [title, text, writer]
    id += 1
    print(boardData)

