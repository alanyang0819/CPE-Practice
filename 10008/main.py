def main():
    word_dict = {}
    for _ in range(int(input())):
        strs = input().split()
        for str in strs:
            for alpha in str:
                if alpha.isalpha():
                    if alpha.upper() not in word_dict:
                        word_dict[alpha.upper()] = 1
                    else:
                        word_dict[alpha.upper()] += 1
    for key, value in sorted(word_dict.items(), key=lambda x: (-x[1], x[0])):
        print(key, value)


if __name__ == "__main__":
    main()
