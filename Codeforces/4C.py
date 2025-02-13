n = int(input())
seen = set()
count_dict = {}
for _ in range(n):
    a = input()
    if a in seen:
        count_dict[a] += 1
        print(f"{a}{count_dict[a]}")
    else:
        print("OK")
        seen.add(a)
        count_dict[a] = 0