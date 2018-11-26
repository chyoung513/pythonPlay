
print((lambda num1, num2 : num1 * num2)(2, 2))

plusFunc = lambda num1, num2 : num1 + num2                             #람다식을 변수에 치환도 가능
print(plusFunc(10, 20))

# map
def numDouble(num):
    return num * 2

data = list(range(1, 11))
result = list(map(numDouble, data))
print(result)
# newDouble()대신 lambda를 사용
double = list(map(lambda num : num *2, data))
print(double)

result = (x*2 for x in data)

# filter
def filterNum(num):
    if num > 5:
        return num

data = list(range(2, 9, 2))
result = list(map(filterNum, data))
print(result)

result = list(filter(lambda num : num > 5, data))
print(result)

# reduce
from functools import reduce
reduce(lambda num1, num2 : num1 + num2, [1, 2, 3, 4])

#삼항연산자
a = 5
re = '참' if a > 3 else '거짓'
print(re)

re = (lambda: '거짓', lambda: '참')[a > 3]()
print(re)

re =((a > 3) and ['참'] or ['거짓'])[0]
print(re)