def main():
    while True:
        try:
            N = input()
            M = input()
            res = []
            for str in M:
                if str in N and str not in res:
                    res.append(str)
            for item in sorted(res):
                print(item, end="")
            print()
        except EOFError:
            return


if __name__ == "__main__":
    main()
