def main():
    while True:
        res = []
        boring = False
        try:
            num_one, num_two = map(int, input().split())
            res.append(num_one)
            while num_one > 1:
                if num_one % num_two == 0:
                    res.append(num_one // num_two)
                else:
                    boring = True
                    print("Boring !")
                    break
                num_one //= num_two
            if boring == False:
                for num in res:
                    print(num, end=" ")
                print()
        except EOFError:
            return


if __name__ == "__main__":
    main()
