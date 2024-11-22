def main():
    while True:
        num_one, num_two = map(int, input().split())
        if num_one == 0 and num_two == 0:
            break
        carry_count = 0
        carry_digit = 0
        while num_one > 0 and num_two > 0:
            digit = num_one % 10 + num_two % 10 + carry_digit
            if digit >= 10:
                carry_count += 1
            carry_digit = digit / 10
            num_one /= 10
            num_two /= 10
        if carry_count > 1:
            print(f"{carry_count} carry operations.")
        elif carry_count == 1:
            print(f"{carry_count} carry operation.")
        elif carry_count == 0:
            print("No carry operation.")


if __name__ == "__main__":
    main()
