CODE:
input_list = ["MIT", "SOE", "MIT", "ADTU", "ADT", "Loni", "Design", 
"Food", "Technology"]
# Access the first element of the list
first_element = input_list[0]
print("First element of the list:", first_element)
# Update a value in the list
input_list[1] = "School of Engineering"
nested_list = [[1, 2, 3], ["a", "b", "c"]]
cloned_list = input_list.copy()
# Concatenate two lists
combined_list = input_list + nested_list[1]
# Count the occurrences of "MIT" and "ADT"
mit_count = input_list.count("MIT")
adt_count = input_list.count("ADT")
# Using lists as a stack (LIFO)
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
popped_value = stack.pop()
# Using lists as a queue (FIFO)
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
dequeued_value = queue.popleft()
# Loop through the input list and print each item
for item in input_list:
print(item)
# Loop through the list with indexes
for index, item in enumerate(input_list):
print(f"Index {index}: {item}")
# Create an iterator from a list
iterator = iter(input_list)
# Square all the numbers in the input list
squared_list = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
if mit_count == 2 and adt_count >= 1:
# Filter the list to include only "MIT" and "ADT"
result_list = list(filter(lambda x: x in ["MIT", "ADT"], 
input_list))
print("List of Strings with exactly two occurrences of 'MIT' and at 
least one occurrence of 'ADT:")
print(result_list)
else:
print("The input list does not meet the criteria.")
