"""
Calculates and displays all prime numbers between 1-500 inclusive,
Includes three concepts: if then else, a function definition, and
for loops.
"""
def is_prime(num): 
    for n in range (1, num):
        if n ==1 or n == num:
            continue
        if num % n != 0:
            return True
        else:
            return False

for n in range(500):
    if is_prime(n):  
        print(n)
