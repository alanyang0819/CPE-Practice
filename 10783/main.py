def main():
    try:
        for i in range(int(input())):
            num_one = int(input())
            num_two = int(input())
            sum = 0

            for num in range(num_one, num_two + 1):
                if num % 2 == 1:
                    sum += num
            print(f"Case {i+1}: {sum}")
    except EOFError:
        return


if __name__ == "__main__":
    main()
