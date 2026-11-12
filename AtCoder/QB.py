N, Q = map(int, input().split())

s = [chr(ord('A') + i) for i in range(N)]

for i in range (N):
    for j in range(N-1):
        print(f"{s[j]} {s[j+1]}", flush = True)

        ans = input().strip()


        if ans == '>':
            s[j] , s[j+1] = s[j+1], s[j]
print("! " + "".join(s), flush=True)
