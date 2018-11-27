import glob
############# 특정 폴더의 파일 확인
files = glob.glob('../output/*.*')       
print(files)

import os.path
############## 폴더와 파일 각각 출력
files = glob.glob('*')      #파일 및 폴더를 갖고 옴

for x in files:
    if os.path.isdir(x):
        print('%s <DIR>' % x)
    else:
        print(x)