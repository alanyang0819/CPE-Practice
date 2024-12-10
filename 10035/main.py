def main():
    while True:
        num_one, num_two = map(int, input().split())
        if num_one == 0 and num_two == 0:
            break
        carry_operation = 0
        carry_digit = 0

        while num_one > 0 or num_two > 0:
            num_sum = num_one % 10 + num_two % 10 + carry_digit
            if num_sum >= 10:
                carry_operation += 1
            carry_digit = num_sum // 10
            num_one //= 10
            num_two //= 10

        if carry_operation == 0:
            print("No carry operation.")
        elif carry_operation == 1:
            print(f"{carry_operation} carry operation.")
        elif carry_operation >= 2:
            print(f"{carry_operation} carry operations.")


if __name__ == "__main__":
    main()
