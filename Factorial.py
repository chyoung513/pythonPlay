
def fact_r(num):

    if num == 1:
        return 1

    return num * fact_r(num - 1)


def fact_f(num):

    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


