def outer(func=None):
    def inner(num1, num2):
        print('결과는 {}'.format(func(num1, num2)))
    return inner

@outer
def plus(n1, n2):
    return n1 + n2

plus(50, 60)