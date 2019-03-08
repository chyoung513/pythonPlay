def outer(tax):
    def inner(su, dan):
        amount = su * dan * tax
        return amount
    return inner


def main():
    tax_rate = outer(0.1)
    notebook = tax_rate(5, 1500000)
    print('노트북 세금은', notebook)

    keyboard = tax_rate(5, 200000)
    print('키보드 세금은', keyboard)


if __name__ == '__main__':
    main()