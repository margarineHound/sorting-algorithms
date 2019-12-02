def roman(n):
    if n> 3999:
        print("number exceeds 3999: Please enter a number between 1-3999\n")
        return
    numRoman = []
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    table = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    i = 0
    while (i < len(num)):
        if int(n/num[i]) == 0:
            i += 1
            continue
        else:
            while (int(n/num[i])) > 0:
                numRoman.append(int(n/num[i])*table[i])
                n %= num[i]

    return ''.join(numRoman)



if __name__ == "__main__":
    print(roman(3888))