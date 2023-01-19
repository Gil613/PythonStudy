import pickle

#파일 write
# data = {
#     "1" : "피클사용하기",
#     "2" : "익숙해지기"
# }
# file = open("./Lecture/Ch.7파일입출력/data.pickle", "wb") # -> wb는 바이너리모드, 컴퓨터가 바로 읽을 수 있는 방식
# pickle.dump(data,file)
# file.close()

#파일 read
# file = open("./Lecture/Ch.7파일입출력/data.pickle", "rb")
# data = pickle.load(file)
# print(data)
# file.close()

#with구문으로 읽어보기
with open("./Lecture/Ch.7파일입출력/data.pickle", "rb") as file:
    data = pickle.load(file)
    print(data)