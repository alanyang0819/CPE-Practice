def solve(string):
    if len(string) == 1:
        return int(string)
    elif len(string) >= 2:
        sum = 0
        for digit in string:
            sum += int(digit)
        return solve(str(sum))


def main():
    string = input()
    while string != "0":
        print(solve(string))
        string = input()


if __name__ == "__main__":
    main()
