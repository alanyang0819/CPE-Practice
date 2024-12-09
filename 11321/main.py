def main():
    N, M = map(int, input().split())
    test, mod = N, M
    while True:
        res = {}
        for _ in range(N):
            num = int(input())
            res[num] = num % M

        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
    print(test, mod)
    for key, _ in sorted(
        res.items(),
        key=lambda x: (x[1], x[0] % 2 == 0, -x[0] if x[0] % 2 == 1 else x[0]),
    ):
        print(key)
    print(f"{N} {M}")


if __name__ == "__main__":
    main()
