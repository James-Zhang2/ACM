# import math
# import sys

# input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
# mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n = sint()
    cnt2 = [[0] * n for _ in range(n)]
    cnt5 = [[0] * n for _ in range(n)]
    zi = zj = -1
    for i in range(n):
        nums = ints()
        for j, x in enumerate(nums):
            while x and x % 2 == 0:
                cnt2[i][j] += 1
                x //= 2
            while x and x % 5 == 0:
                cnt5[i][j] += 1
                x //= 5
            if i and j:
                cnt2[i][j] += min(cnt2[i - 1][j], cnt2[i][j - 1])
                cnt5[i][j] += min(cnt5[i - 1][j], cnt5[i][j - 1])
            elif i:
                cnt2[i][j] += cnt2[i - 1][j]
                cnt5[i][j] += cnt5[i - 1][j]
            elif j:
                cnt2[i][j] += cnt2[i][j - 1]
                cnt5[i][j] += cnt5[i][j - 1]

            if x == 0: zi, zj = i, j

    if cnt2[-1][-1] <= cnt5[-1][-1]:
        dp = cnt2
    else:
        dp = cnt5

    if dp[-1][-1] and zi != -1:
        ans = "D" * zi + "R" * zj + "D" * (n - 1 - zi) + "R" * (n - 1 - zj)
        print(1)
        print(ans)
        return

    ans = []
    x = y = n - 1
    while x != 0 or y != 0:
        if y == 0:
            x -= 1
            ans.append("D")
        elif x == 0:
            y -= 1
            ans.append("R")
        elif dp[x - 1][y] < dp[x][y - 1]:
            x -= 1
            ans.append("D")
        else:
            y -= 1
            ans.append("R")

    ans.reverse()
    print(dp[-1][-1])
    print("".join(ans))


solve()

# 这里重新定义了 `input` 函数，使其能够读取标准输入并去除末尾的换行符。
# `sint` 函数用于读取一个整数，它通过调用重新定义的 `input` 函数并将读取到的字符串转换为整数。
# `ints` 函数用于读取一行由空格分隔的整数，并将它们转换为整数列表。

# - 首先读取二维数组的边长 `n`。
# - 然后初始化了两个二维数组 `cnt2` 和 `cnt5`，用于分别记录从左上角到每个位置的路径上所有元素分解质因数后2和5的累计个数，初始值都为0。
# - 同时初始化了 `zi` 和 `zj` 为 -1，这两个变量将用于记录值为0的元素的坐标（如果存在的话）。

# - 对于二维数组中的每个元素 `x`：
#     - 首先通过不断除以2和5的方式，计算该元素分解质因数后2和5的个数，并分别累加到 `cnt2` 和 `cnt5` 对应的位置。
#     - 然后根据当前元素的位置（是否在第一行或第一列），通过取上方或左方位置的累计因数个数的最小值，来更新当前位置的累计因数个数。例如，如果当前元素不在第一行和第一列，就取上方和左方位置 `cnt2`（或 `cnt5`）的最小值累加到当前位置的 `cnt2`（或 `cnt5`）中。
#     - 如果当前元素的值为0，就记录下该元素的坐标 `zi` 和 `zj`。


# - 首先比较从左上角到右下角路径上累计的2的个数和5的个数，选择较小的那个作为 `dp`（这里 `dp` 要么是 `cnt2`，要么是 `cnt5`）。
# - 如果 `dp` 最后一个位置的值不为0（即存在一条从左上角到右下角的路径使得累计因数个数不为0），并且之前记录到了值为0的元素坐标（`zi` 和 `zj` 不为 -1），那么就构造一条先向下走到值为0的元素位置，再向右走到右下角的路径 `ans`，并输出相关信息后返回。

# - 如果没有满足前面特殊路径（经过值为0的元素）的情况，就通过动态规划的思想从右下角开始回溯到左上角来确定一条路径。
# - 在回溯过程中，根据上方和左方位置的 `dp` 值大小来决定是向上走（`D`）还是向左走（`R`），将走过的方向记录到 `ans` 列表中。
# - 最后将 `ans` 列表反转得到从左上角到右下角的正确路径顺序，并输出 `dp` 最后一个位置的值（即累计因数个数）以及构造好的路径字符串。

# 总体而言，这段代码通过对二维数组元素的因数分解和动态规划的运用，巧妙地解决了在特定规则下从二维数组左上角到右下角的路径规划问题，同时考虑了数组中存在值为0的元素的特殊情况来优化路径选择。