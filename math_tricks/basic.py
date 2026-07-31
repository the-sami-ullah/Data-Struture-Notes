def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
  
  
# =====================  GCD  ======================   


from math import gcd

lcm = a * b // gcd(a, b)  

# =====================   LCM  ======================   

def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True
  
# =====================  PRIME  ======================   
  
def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    i = 2
    while i * i <= n:
        if prime[i]:
            j = i * i
            while j <= n:
                prime[j] = False
                j += i

        i += 1

    return prime  