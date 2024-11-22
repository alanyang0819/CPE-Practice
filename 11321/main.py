"""
def main():
    M, N = map(int, input().split())
    dict = {}
    for i in range(M):
        num = int(input())
        dict[num] = num % N

    for key in sorted(dict.items(), key=lambda x: (x[1], ))
"""
