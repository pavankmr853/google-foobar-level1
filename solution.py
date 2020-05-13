import math
def solution(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

primes = ''

for i in range(2,21000,1):
    if len(primes) < 10005:
        if solution(i):
            primes = primes + str(i)
    else:
        break
def solution(n):
    re_id = primes[n:n+5:1]
    return(re_id)
