def main():
    for _ in range(int(input())):
        families = []
        nums = list(map(int, input().split()))
        for i in range(1, len(nums)):
            families.append(nums[i])

        families.sort()

        sum = 0
        if len(families) % 2 == 1:
            mid = families[(len(families) - 1) // 2]

        else:
            mid = (families[len(families) // 2] + families[len(families) // 2 - 1]) // 2

        for family in families:
            sum += abs(family - mid)

        print(sum)


if __name__ == "__main__":
    main()
