def main():
    gap = []
    numbers = list(map(int, input().split()))
    for i in range(numbers[0]):
        if i >= 1:
            gap.append(abs(numbers[i + 1] - numbers[i]))
    gap.sort()
    for j in range(1, numbers[0]):
        if gap[j - 1] != j:
            print("Not jolly")
            return 0
    print("jolly")


if __name__ == "__main__":
    main()
