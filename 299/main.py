def main():
    for _ in range(int(input())):
        _ = int(input())
        nums = list(map(int, input().split()))

        swap_count = 0
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swap_count += 1

        print(f"Optimal train swapping takes {swap_count} swaps.")


if __name__ == "__main__":
    main()
