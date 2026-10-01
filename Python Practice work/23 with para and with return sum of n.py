def sum(n):
    sum = 0

    for i in range(1, n + 1):
        sum = sum + i
        print(i)

    return sum


n = int(input("Enter The Number : "))

ans = sum(n)

print("Sum =", ans)