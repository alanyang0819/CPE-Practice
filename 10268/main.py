def main():
    while True:
        try:
            para = int(input())
            coeff = list(map(int, input().split()))

            if len(coeff) == 1:
                print(0)

            elif len(coeff) == 2:
                print(coeff[0])

            elif len(coeff) > 2:
                deri = 0
                degree = len(coeff) - 1
                for i in range(degree):
                    deri += coeff[i] * (degree - i) * pow(para, degree - i - 1)
                print(deri)

        except EOFError:
            return


if __name__ == "__main__":
    main()
