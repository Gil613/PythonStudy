# https://school.programmers.co.kr/learn/courses/30/lessons/120824 짝수 홀수 개수
# #num_list = [1,2,3,4,5]
# answer = []
# cnt1 = 0
# cnt2 = 0
# i = 0
# length = len(num_list)

# while i < length :
#     print(i)
#     if num_list[i] % 2 == 0 : 
#         cnt1 += 1
#         i += 1
#     else :
#         cnt2 += 1    
#         i += 1
    
   
    
            
# answer.insert(0, cnt1)
# answer.insert(1, cnt2)
# print(answer)

#https://school.programmers.co.kr/learn/courses/30/lessons/120829 각도기 문제 if문

# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오.


#1부터 10까지 더하기

#for와 range 함수를 사용하여 구구단 만들기

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{j} X {i} = {i*j}", end = "\t")
#     print(" ")


# 유투버로부터 현재 구독자 수를 입력하면 수익창출이 가능한지 불가능한지 알려주는 프로그램 제작을 요청받았다.
# 수익창출은 1,000명 이상일 경우 가능하며, "현재 구독자 수를 입력하세요" 라는 문구와 함께 숫자를 입력했을 경우 "수익 창출이 가능합니다!", 
# "수익 창출이 불가능합니다! 부족한 구독자 수는 00명입니다."  라는 안내 문구가 출력되도록 기획하였다.
'''
def subscriber_check():
    user_cnt_now = int(input("현재 구독자 수를 입력하세요 >>>"))
    if user_cnt_now >= 1000 : print("수익 창출이 가능합니다.")
    else : print(f"수익 창출이 불가능합니다!\n부족한 구독자 수는 {1000 - user_cnt_now}명 입니다.")

subscriber_check()
'''

#학생이 공부시간을 채우지 못할경우 휴대폰을 사용하지 못하게하는
#프로그램을 만들어주자
#조건) 10시간 이상 : 휴대폰 잠금 해제, 5시간 이상 : 휴대폰 사용가능, 나머지 :불가능
'''
def phone_keeper():
    study_time = int(input("공부한 시간을 입력하세요(시간)"))
    
    if study_time >= 10: print("잠금 해제")
    elif study_time >=5: print("30분간 사용 가능")
    else: print("공부시간을 채워주세요")

phone_keeper()
'''

