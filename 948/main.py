def main():
    fib = [1, 2]
    while fib[-1] < 100000000:
        fib.append(fib[-1] + fib[-2])

    for _ in range(int(input())):
        num = int(input())
        print(f"{num} = ", end="")

        found = 0
        for f in fib[::-1]:
            if num >= f:
                num -= f
                found = 1
                print(1, end="")

            elif found:
                print(0, end="")
        print(" (fib)")


if __name__ == "__main__":
    main()
