#딕셔너리 형태

d1 = {'name' : 'Gil', 'phone' : '1234', 'birth' : '0810'}
d2 = {'number': [1,2,3,4,5], 'char' : ['a','b','c','d']} #리스트로 변환하여 인덱스 값 출력해보기

#호출하기

d1.get('name') # 결과 : Gil
d1['name']
d2.values()
d2.keys()
d2.items()


#추가하기
d3 = {1 : 'a'}
d3[2] = 'b'
d3['name'] = 'Gil'
d3[3] = [1,2,3]
d3[4,5,6] = [7,8,9]

#삭제하기

del d3[4,5,6]

#key값은 중복 불가

d4 = {1 : 'a'}
d4[1] = 'b'


d5 = {1 : 'a', 1 : 'b'}

d5.clear()

#특정 key가 딕셔너리 안에 있는지 확인
'name' in d2
'email' in d2