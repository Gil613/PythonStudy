import csv
#주식의 수익금과 수익률을 출력해주는 프로그램을 작성해보자
#수익금 = (목표가 - 매입가) * 수량
#수익률 = (목표가 / 매입가 - 1) * 100
#mystock.csv 파일로부터 종목, 매입가, 수량, 목표가 정보를 가져온다

#mystock.csv 예시 
# 종목       매입가    수량    목표가
# 삼성전자   60,000     10     70,000
#출력 예시
# 수익금 : 100,000 , 수익률 : 16.66%

def mystock(item, price, ea, goal):
    
    
    data = [
        [item, price, ea, goal]
    ]

    file = open("mystock.csv", "a", newline="", encoding="utf8")
    

    append_file = csv.writer(file)
    for it in data:
        append_file.writerow(it)
    file.close()

    file.read

    per = round((goal/price - 1) * 100, 2)
    print(f"{item}  {(goal - price) * ea}   {per}")

mystock("카카오",150000,8,200000)

#"카카오",150000,8,200000
#"네이버", 60000, 12, 100000