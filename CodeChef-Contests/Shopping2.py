t = int(input())


while t > 0:
    N, D = map(int, input().split())
    a1= list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    print()

    min_list = []
    a = D + sum(a1)
    b = D + sum(a2)
    for i in range(N): 
        x = min(a1[i], a2[i])
        min_list.append(x)
    c = 2 * D + sum(min_list)

    print(min(a, b, c))

    t-=1