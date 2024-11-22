def main():
    for _ in range(int(input())):
        family = []
        numbers = list(map(int, input().split()))
        for i in range(numbers[0]):
            family.append(numbers[i + 1])
        family.sort()
        if len(family) % 2 == 1:
            mid = family[(len(family) - 1) // 2]
        else:
            mid = family[(len(family) // 2) - 1] + family[len(family) // 2] // 2

        sum = 0
        for j in range(len(family)):
            sum += abs(family[j] - mid)

        print(sum)


if __name__ == "__main__":
    main()
