#집합의 형태
s1 = set([1,2,3])
s2 = set('hello')
s3 = set(['a','b','c','e'])


#교집합
s2 & s3
s2.intersection(s3)

#합집합
s2 | s3
s2.union(s3)

#차집합
s2 - s3
s3.difference(s2)

#값 추가하기
s1.add(4) #값 단일 추가
s1.update([5,6,7]) # 값 여러 개 추가

#값 제거하기
s1.remove(6)
s1.discard(6)