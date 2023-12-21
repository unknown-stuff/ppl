# Demonstration of loops in Python
# For Loop
print("For Loop:")
for i in range(5):
print(i, end=' ')
print("\n")
# While Loop
print("While Loop:")
count = 0
while count < 5:
print(count, end=' ')
count += 1
print("\n")
# Execution of problem statements
def find_numbers(minimum, maximum):
numbers = []
for i in range(minimum, maximum + 1):
if i % 5 == 0 and i % 9 == 0:
numbers.append(i)
return numbers
def is_prime(n):
if n <= 1:
return False
for i in range(2, n):
if n % i == 0:
return False
return True
def count_numbers(numbers):
prime_count = 0
even_count = 0
odd_count = 0
for num in numbers:
if is_prime(num):
prime_count += 1
if num % 2 == 0:
even_count += 1
else:
odd_count += 1
return prime_count, even_count, odd_count
# Execution of the first problem statement
minimum = 10
maximum = 100
result_numbers = find_numbers(minimum, maximum)
print(f"Numbers divisible by 5 and multiples of 9 between {minimum} and 
{maximum} are: {result_numbers}\n")
# Execution of the second problem statement
input_numbers = [23, 5, 17, 6, 4, 9, 12, 13, 25, 28, 31]
prime_count, even_count, odd_count = count_numbers(input_numbers)
print(f"Number of prime numbers: {prime_count}")
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
