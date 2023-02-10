# 리스트에 저장된 데이터 정렬
data = [
    ['이승협', 'A', 32],
    ['차훈', 'C', 30],
    ['유회승', 'B', 28],
    ['김재현', 'D', 29]
]

# data.sort(reverse=False, key=lambda x:(x[1],-x[2]))
# print(data)

# result = sorted(data, key=lambda x:(x[1], -x[2]))
# print(data)
# print(result)

# 딕셔너리에 저장된 데이터 정렬
data = [
    {'name':'이승협', 'score':'A', 'age':32},
    {'name':'차훈', 'score':'C', 'age':30},
    {'name':'유회승', 'score':'B', 'age':28},
    {'name':'김재현', 'score':'D', 'age':30.2}
]

#data.sort()
result = sorted(data, key=lambda x:x['age'])
print(result)

# 클래스에 저장된 데이터 정렬






