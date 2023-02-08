# f = open('01_basic/test.txt', 'r', encoding = 'cp949')
# # print(type(f))
# text = f.read()
# print(text)
# f.close()


# with open('01_basic/test.txt', 'r', encoding = 'cp949' ) as f:
    
#     while True:
#         text = f.readline()
#         if not text:
#             break
#         print(text)


# with open('01_basic/test_w.txt', 'a', encoding = 'utf8') as f:
#     f.write('첫 줄 입력\n')


import pickle

card = [['홍길동', '서울', '111-1111-1111','hong@gmail.com'],
     ['김나리', '광주', '111-1111-1111', 'kim@gmail.com']]

# f = open('01_basic/pickledata.pickle','wb')
# pickle.dump(card, f) 

# f.close


# with open('01_basic/pickledata.pickle','rb') as f:
#     data = pickle.load(f)
#     print(data)

import json

# with open('01_basic/jsontest.json','w') as f:
#     json.dump(card,f,indent=2)


with open('01_basic/jsontest.json','r') as f:
    data = json.load(f)
    print(type(data))
    print(data)


