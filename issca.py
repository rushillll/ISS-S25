def is_Narc(n):
    num_Str = str(n)
    num_Digits = len(num_Str)
    
    sum_Of_Powers = sum(int(digit) ** num_Digits for digit in num_Str)
    
    return sum_Of_Powers == n

def print_Narcis_Numbers(start, end):
    for num in range(start, end + 1):
        if is_Narc(num):
            print(num)

print_Narcis_Numbers(1000, 5000)
