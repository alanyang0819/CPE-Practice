def main():
    while True:
        try:
            nums = list(map(int, input().split()))
            gap = []
            for i in range(1, nums[0]):
                gap.append(abs(nums[i] - nums[i + 1]))

            gap.sort()
            jolly = True

            for j in range(1, nums[0]):
                if gap[j - 1] != j:
                    jolly = False
            if jolly:
                print("Jolly")
            else:
                print("Not jolly")

        except EOFError:
            break


if __name__ == "__main__":
    main()
