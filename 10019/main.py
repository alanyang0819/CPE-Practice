def main():
    for _ in range(int(input())):
        N = input()

        X1 = int(N, 10)
        b1 = bin(X1).count("1")

        X2 = int(N, 16)
        b2 = bin(X2).count("1")
        print(f"{b1} {b2}")


if __name__ == "__main__":
    main()
