def solve(num, degree=0, already_nine=False):
    sum = 0
    for digit in num:
        sum += int(digit)
    if sum == 9:
        if already_nine:
            return degree
        already_nine = True
    if sum % 9 != 0:
        return degree

    else:
        degree += 1
        return solve(str(sum), degree, already_nine)


def main():
    num_str = input()
    while num_str != "0":
        degree = solve(num_str, 0)

        if degree == 0:
            print(f"{num_str} is not a multiple of 9")

        else:
            print(f"{num_str} is a multiple of 9 and has 9-degree {degree}")

        num_str = input()


main()
