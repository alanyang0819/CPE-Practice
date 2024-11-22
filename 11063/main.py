def main():
    case = 1
    while True:
        try:
            sum = []
            length = int(input())
            nums = list(map(int, input().split()))
            for i in range(length):
                for j in range(i + 1, length):
                    sum.append(nums[i] + nums[j])

            if len(sum) != len(set(sum)):
                print(f"Case #{case}: It is not a B2-Sequence.")
            else:
                print(f"Case #{case}: It is a B2-Sequence.")
            case += 1
        except EOFError:
            return


if __name__ == "__main__":
    main()
