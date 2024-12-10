def ThreeNPlusOne(num, length=1):
    if num == 1:
        return length
    elif num % 2 == 1:
        # length += 1
        return ThreeNPlusOne(num * 3 + 1, length + 1)
    else:
        # length += 1
        return ThreeNPlusOne(num // 2, length + 1)


def main():
    while True:
        try:
            i, j = map(int, input().split())
            print(f"{i} {j} ", end="")
            max = 0
            if i > j:
                i, j = j, i

            for num in range(i, j + 1):
                result = ThreeNPlusOne(num, length=1)
                if result > max:
                    max = result
            print(max)

        except EOFError:
            break


if __name__ == "__main__":
    main()
