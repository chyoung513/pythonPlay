
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = len(nums)
output_file = '../output/result.csv'

f = open(output_file, 'a')

for idx in range(count):
    if idx < (count - 1):
        f.write(str(nums[idx]) + ',')
    else:
        f.write(str(nums[idx]) + '\n')

f.close()

############## 저장된 내용 읽어오기
input_file = '../output/result.csv'
f = open(input_file, 'r')
for line in f:
    print(line, end = '')
f.close()

################ with 구문 사용
with open(input_file, 'r') as f:
    for line in f:
        print(line, end = '')