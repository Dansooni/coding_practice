from collections import deque

n = int(input())
m = int(input())
travel_time_table = []
for _ in range(n + 1):
    travel_time_table.append([-1] * (n + 1))
for _ in range(m):
    u, v, t = map(int, input().split())
    travel_time_table[u][v] = t
s, e = map(int, input().split())

time_cost = [-1] * (e + 1)
time_cost[s] = 0

start_points = deque()
start_points.append(s)

while start_points:
    start_point = start_points.popleft()
    for i in range(start_point + 1, e + 1):
        if travel_time_table[start_point][i] != -1:
            if time_cost[i] == -1:
                time_cost[i] = time_cost[start_point] + travel_time_table[start_point][i]
                if i != e and i not in start_points:
                    start_points.append(i)
            else:
                time_cost[i] = min(time_cost[i], time_cost[start_point] + travel_time_table[start_point][i])
                if i != e and i not in start_points:
                    start_points.append(i)
                
print(time_cost[e])