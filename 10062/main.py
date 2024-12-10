def main():
    res = []
    while True:
        try:
            dict = {}
            str = input()
            for char in str:
                if ord(char) not in dict:
                    dict[ord(char)] = 1
                else:
                    dict[ord(char)] += 1
            res.append(dict)

        except EOFError:
            for object in res:
                for key, value in sorted(object.items(), key=lambda x: (x[1], -x[0])):
                    print(f"{key} {value}")

                if object != res[-1]:
                    print()
            break


if __name__ == "__main__":
    main()
