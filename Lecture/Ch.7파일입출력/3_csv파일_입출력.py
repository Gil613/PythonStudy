import csv

#파일 쓰기
# data = [
#     ["이름", "반", "번호"],
#     ["재석",1,2],
#     ["홍철",1,5],
#     ["명수",3,6]
# ]

# file = open("student.csv","w", newline="", encoding="utf8")
# writer = csv.writer(file)

# for d in data:
#     writer.writerow(d)

# file.close()

#읽기
with open("student.csv","r", newline="", encoding="utf8") as file:
    reader = csv.reader(file)
    for data in reader:
        print(data)

# file = open("student.csv","r", newline="", encoding="utf8")
# reader = csv.reader(file)

# for data in reader:
#     print(data)

# file.close()

