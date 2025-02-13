for _ in range(int(input())):
    n = int(input())
    if n & 1:
        if n >= 27:
            print(* [1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 13, 12, 12, 1, 13] + [i // 2 + 22 for i in range(n - 27)])
        else:
            print(-1)
    else:
        print(*[f"{i} {i}"for i in range(1, n // 2 + 1)])
