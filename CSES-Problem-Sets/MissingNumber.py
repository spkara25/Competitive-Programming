n = int(input())
nums = list(map(int, input().split()))
ans = 0

esum = n * (n + 1) //2
ans = esum - sum(nums)
print(ans)
