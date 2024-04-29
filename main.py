from funcs import test_funcs_summ, test_funcs_sub


def main():
    a = int(input("Введите первое число: \n"))
    b = int(input("Введите второе число: \n"))
    print(test_funcs_summ(a, b))
    print(test_funcs_sub(a, b))


if __name__ == "__main__":
    main()
