#함수의 기본 형태
'''
def 함수이름() :
    명령 블록
'''

# 함수 호출하기
'''
함수이름(인자1,인자2...)
'''

# 반환 값이 있는 함수
'''
def 함수이름() :
    명령 블록
    return 반환 값
''' 

# 함수의 사용하는 경우
def printMessage(name, whether) :
    print("안녕하세요? 저는", name,"(이)에요")
    print("현재 날씨는(은) ",whether)

print(printMessage('유길상', '미세먼지나쁨'))

#함수를 사용하지 않는 경우
# print("안녕하세요? 저는 길동(이)에요")
# print("현재 날씨는(은) 흐려요")

# print("안녕하세요? 저는 우성(이)에요")
# print("현재 날씨는(은) 맑아요")

# print("안녕하세요? 저는 현지(이)에요")
# print("현재 날씨는(은) 추워요")
