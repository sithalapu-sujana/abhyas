n = int(input())
arr = list(map(int, input().split()))

prime = []
# 1. Track primes we have already seen to avoid duplicates
seen = set()

for num in arr:
    if num < 2:
        continue

    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    # 2. Only add the number if it's prime AND unique
    if is_prime and num not in seen:
        prime.append(num)
        seen.add(num)

prime.sort()

# 3. Print everything separated by spaces with NO trailing space
print(*prime)
