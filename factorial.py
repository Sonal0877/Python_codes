def cal_factorial(number: int) -> int:
    """
    Calculate the factorial of provided number
    :param number: input number
    :return: factorial
    """
    output = 1
    if number == 0:
        return 1
    elif number != 0:
        for num in range(1, number+1):
            output *= num
        return output


for num in range(35):
    factorial = cal_factorial(num)
    print("{} {}".format(num,factorial))


