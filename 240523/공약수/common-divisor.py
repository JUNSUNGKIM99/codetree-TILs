import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_common_divisors(numbers):
    # Step 1: Compute the GCD of all numbers
    current_gcd = numbers[0]
    for num in numbers[1:]:
        current_gcd = gcd(current_gcd, num)
    
    # Step 2: Find all divisors of the GCD
    common_divisors = []
    for i in range(1, int(math.sqrt(current_gcd)) + 1):
        if current_gcd % i == 0:
            common_divisors.append(i)
            if i != current_gcd // i:
                common_divisors.append(current_gcd // i)
    
    return sorted(common_divisors)

# Input reading
n = int(input())
numbers = list(map(int, input().split()))

# Finding common divisors
result = find_common_divisors(numbers)

# Printing result
for divisor in result:
    print(divisor)