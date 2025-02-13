a = {}
b = {}
name = [None] * 1017
score = [0] * 1017
n = int(input())

def main():
    for i in range(n):
        name[i], score[i] = input().split()
        score[i] = int(score[i])
        if name[i] in a:
            a[name[i]] += score[i]
        else:
            a[name[i]] = score[i]

    max_score = 0
    for i in range(n):
        if a[name[i]] > max_score:
            max_score = a[name[i]]

    for i in range(n):
        if name[i] not in b:
            b[name[i]] = 0
        b[name[i]] += score[i]

        # 在最终分数是最大的人中，选首先达到最大分数的人
        if (b[name[i]] >= max_score) and (a[name[i]] >= max_score):
            print(name[i])
            break

if __name__ == "__main__":
    main()