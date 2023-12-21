
import datetime
import sys
def find_max_of_three(x, y, z):
max_value = max(x, y, z)
return max_value
def multiply_list(numbers):
result = 1
for num in numbers:
result *= num
return result
def generate_even_numbers(start, end):
even_numbers = [num for num in range(start, end + 1) if num % 2 == 
0]
return even_numbers
def display_datetime_and_python_version():
current_datetime = datetime.datetime.now()
python_version = sys.version
print("1. The maximum value among 42, 17, and 88 is:", 
find_max_of_three(42, 17, 88))
number_list = [2, 3, 5, 7]
print("2. The product of numbers in the list [2, 3, 5, 7] is:", 
multiply_list(number_list))
even_numbers_list = generate_even_numbers(19, 88)
print("3. List of even numbers between 19 and 88:", 
even_numbers_list)
print("4. Current Date and Time:", current_datetime)
print("5. Python Version:", python_version)
# Call the combined function to perform all tasks
display_datetime_and_python_version()
