import glob, os

path = os.path.dirname(__file__)
result = glob.glob(path+'/01*.*')
print(result)



#경로 안(특정 폴더 안)에 파일 파악할 때 / *, ?
#외장함수라 import 씀