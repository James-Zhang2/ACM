d, sumtime = map(int, input().split())
time_ranges = [list(map(int, input().split())) for _ in range(d)]

min_sum = sum([range_pair[0] for range_pair in time_ranges])
max_sum = sum([range_pair[1] for range_pair in time_ranges])

if min_sum <= sumtime <= max_sum:
    print("YES")
    remaining_time = sumtime - min_sum
    for i in range(d):
        if remaining_time > time_ranges[i][1] - time_ranges[i][0]:
            remaining_time -= time_ranges[i][1] - time_ranges[i][0]
            time_ranges[i][0] = time_ranges[i][1]
        else:
            time_ranges[i][0] += remaining_time
            remaining_time = 0
    for daily_time in time_ranges:
        print(daily_time[0], end=" ")
else:
    print("NO")
