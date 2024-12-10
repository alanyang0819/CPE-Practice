def main():
    res = []
    count = 0
    while True:
        try:
            string = input().split(" ")
            for i, word in enumerate(string):
                if '"' in word and (count + 1) % 2 == 1:
                    string[i] = word.replace('"', "``")
                    count += 1
                elif '"' in word and (count + 1) % 2 == 0:
                    string[i] = word.replace('"', "' '")
                    count += 1
            res.append(" ".join(string))
        except EOFError:
            break

    print("\n".join(res))


if __name__ == "__main__":
    main()
