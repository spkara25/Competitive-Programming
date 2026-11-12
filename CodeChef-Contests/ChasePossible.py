R, B = map(int, input().split())

rem_balls = 6 * B
if rem_balls < R:
    print("No")
else:
    print("YES")