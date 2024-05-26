def calculate_cycle_length(n):
    original_number = n
    count = 0
    while True:
        tens = n // 10
        ones = n % 10
        digit_sum = tens + ones
        new_number = (ones * 10) + (digit_sum % 10)
        count += 1
        if new_number == original_number:
            break
        n = new_number
    
    return count

n = int(input())

cycle_length = calculate_cycle_length(n)
print(cycle_length)