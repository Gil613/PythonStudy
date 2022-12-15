# 2. 문자

# 작은 따옴표 ''
'작은 따옴표입니다.'

# 큰 따옴표
"큰 따옴표입니다."

# 작은 따옴표 3개 -> 들여쓰기 가능
'''작은 따옴표 3개입니다.
이렇게 여러 문장으로 구성 할 수 있습니다.'''

# 큰 따옴표 3개 -> 들여쓰기 가능
"""큰 따옴표 3개입니다.
이렇게 여러 문장으로 구성 할 수 있습니다."""

#이스케이프 코드
"이스케이프 코드란 여러 줄의 문장을 처리할 때 \n 사용 하는 '문자 조합입니다.' \t 간격조정도 가능하며 출력하는 문자열에 여러가지 옵션을 사용 할 수 있습니다"
"이스케이프 코드는 다양하기에 외울 필요 없고 필요 한 코드를 검색해서 사용하시면 됩니다."

#2.1. 문자열 연산
pre = "String can addition other string " 
suffix = " it is awesome"
pre + suffix #결과 : String can addition other string  it is awesome

string_multiple = "string can multiplication it is awesome " * 2
string_multiple # 결과 : string can multiplication it is awesome string can multiplication it is awesome

#2.2. 문자열 길이 구하기 len()
# len() 함수를 사용해 문자열의 길이를 구할 수 있다. 1부터 시작한다.
ten_letters = "0123456789"
len(ten_letters) # 결과 : 10

#2.3. 문자열 인덱싱
# 인덱싱이란 문자열의 각 문자들의 번호이다. 0부터 시작한다.
ten_letters[0] # 결과 : 0 -> "0123456789"의 0번째는 0이다
ten_letters[-1] #결과 : 9 -> 인덱스 -1 은 문자열의 맨 뒷부분을 가리킨다.

#2.4. 문자열 슬라이싱
# slice의 문자열안에 홍길동이라는 이름만 추출하고 싶을때 사용한다.
slice = "안녕하세요 저의 이름은 홍길동 입니다."
slice[13:16] # 결과 : 홍길동 -> 0부터 시작하는 인덱스의 13번째부터 16번째까지를 가리킨다.

#2.5. 문자열 formatting
#2.5.1. 숫자 대입하기
"I am %d years old " %28 # 결과 : I am 28 years old
#2.5.1. 문자 대입하기
"Today is %s day" %"snow" # 결과 : Today is snow day 
#2.5.2. 두 개 이상의 값 대입하기 .format() 파이썬 
"여기엔 숫자 {0} 여기엔 문자 {1} 여기에 다시 숫자 {2}" .format(10, "문자", 3) # 결과 : 여기엔 숫자 10 여기엔 문자 문자 여기에 다시 숫자 3
#2.5.3 정렬하기 10의 길이를 갖는 문자열로 정렬해준다.
"{0:<10}" .format("왼쪽 정렬")   # 결과 : 왼쪽 정렬     .
"{0:>10}" .format("오른쪽 정렬") # 결과 :     오른쪽 정렬.
"{0:^10}" .format("가운데 정렬") # 결과 :   가운데 정렬  .
"{0:@^30}" .format("공백 대신 @를 채워 가운데 정렬") # 결과 : @@@@@@공백 대신 @를 채워 가운데 정렬@@@@@@
"{0:1<30}" .format("공백 대신 1을 채워 왼쪽 정렬")   # 결과 : 공백 대신 1을 채워 왼쪽 정렬1111111111111
"{0:1>30}" .format("공백 대신 !을 채워 오른쪽 정렬") # 결과 : !!!!!!!!!!!!!공백 대신 !을 채워 왼쪽 정렬

#2.6 문자열 관련 함수
#2.6.1. 문자 세기(count)
a_cnt = "abcadoea"
a_cnt.count("a") # 결과 : 3
#2.6.2. 위치 알기(find)
n_find = "my name is Nina"
n_find.find("n") # 결과 :3 -> n은 0부터 시작해 3번째에 위치한다
print(n_find.find("N")) # 결과 :3 -> n은 0부터 시작해 3번째에 위치한다
n_find.find("z") # 결과 :-1 -> 문자열에 존재하지 않는 문자를 찾을시 -1을 리턴
#2.6.3. 인덱스 알기(index)
a_index = "i am Adam"
a_index.index('a') #결과 : 2  0부터 시작해 첫번째 a가 있는 index를 리턴
a_index.index('A') #결과 : 5  0부터 시작해 첫번째 A가 있는 index를 리턴
#a_index.index('c') #결과 : 오류 존재하지않는 문자이기 때문에 인덱스를 찾을 수 없어 오류가 발생
#2.6.4. 문자열 삽입(join)
",".join('abcdef') # 결과 : a,b,c,d,e,f 문자 사이에,를 삽입한다.

#이 외에 필요할 시 검색
