#파일 쓰기
# file = open("./Lecture/Ch.7파일입출력/test.txt","w", encoding="utf8")
# file.write("파일 입출력 연습중입니다.")
# file.close()

# 파일 데이터 추가하기
# file = open("./Lecture/Ch.7파일입출력/test.txt","a", encoding="utf8")
# file.write("\n파일에 문장 추가합니다.")
# file.close()

#파일 읽기
file = open("./Lecture/Ch.7파일입출력/test.txt","r", encoding="utf8")
# data = file.read()
# print(data)
# file.close()


#파일 한 줄씩 읽기
while True:
    data = file.readline()
    print(data)
    if data == "":
        break
file.close()


