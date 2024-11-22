def main():
    for _ in range(int(input())):
        sum, gap = map(int, input().split())
        if sum < gap:
            print("impossible")
        elif (sum + gap) % 2 != 0 or (sum - gap) % 2 != 0:
            print("impossible")
        else:
            print(f"{(sum + gap) // 2} {(sum - gap) // 2}")


if __name__ == "__main__":
    main()
