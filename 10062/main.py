def main():
    res = []
    while True:
        dict = {}
        try:
            str = list(input())
            for alpha in str:
                if ord(alpha) not in dict:
                    dict[ord(alpha)] = 1
                else:
                    dict[ord(alpha)] += 1
            res.append(dict)
        except EOFError:
            for object in res:
                for key, value in sorted(object.items(), key=lambda x: (x[1], -x[0])):
                    print(key, value)
                if object != res[-1]:
                    print()
            return


if __name__ == "__main__":
    main()
