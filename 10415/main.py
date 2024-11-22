def main():
    finger = {
        "c": "0111001111",
        "d": "0111001110",
        "e": "0111001100",
        "f": "0111001000",
        "g": "0111000000",
        "a": "0110000000",
        "b": "0100000000",
        "C": "0010000000",
        "D": "1111001110",
        "E": "1111001100",
        "F": "1111001000",
        "G": "1111000000",
        "A": "1110000000",
        "B": "1100000000",
    }

    for i in range(int(input())):
        count = [0] * 10
        sound = input()
        for alpha in sound:
            for i in range(len(finger[alpha])):
                count[i] += int(finger[alpha][i])

        for item in count:
            print(item, end=" ")
        print()


if __name__ == "__main__":
    main()
