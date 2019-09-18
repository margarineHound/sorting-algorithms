import math

def karatsuba(num1, num2):

    if (num1 < 10 ) or (num2 < 10):
        return num1*num2

    len1 = int(math.log10(num1)) +1
    len2 = int(math.log10(num2)) +1

    lenn = max(len1, len2)

    lenn_2 = math.ceil(lenn/2)

    a = int(num1 /pow(10, lenn_2))
    b = num1 % pow(10, lenn_2)

    c = int(num2 /pow(10, lenn_2))
    d = num2 % pow(10, lenn_2)

    # print(f'len1 ={len1}, len2 = {len2}, lenn = {lenn}, lenn_2 = {lenn_2}' \
        # +f'\n, a = {a}')

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba((a+b), (c+d))
    mid = abcd - ac - bd

    return ac*pow(10, 2*lenn_2) + mid*pow(10, lenn_2) + bd

def main():
    # num1 = int(input("Enter first number: >> "))
    # num2 = int(input("Enter first number: >> "))
    num1 = 123456789
    num2 = 4562345524324
    result = karatsuba(num1, num2)
    print(f'Result: > ', result)


if __name__ == "__main__":
    main()