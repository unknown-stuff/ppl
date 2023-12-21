CODE:
class Animal:
def __init__(self, animal_type, name):
self.animal_type = animal_type
self.name = name
def __str__(self):
return f"{self.animal_type} - {self.name}"
class AnimalShelter:
def __init__(self):
self.dog_queue = []
self.cat_queue = []
self.rabbit_queue = []
def enqueue(self, animal_type, name):
"""
Enqueue a new animal to the shelter.
Args:
animal_type (str): Type of animal ('dog', 'cat', or 
'rabbit').
name (str): Name of the animal.
"""
animal = Animal(animal_type, name)
if animal_type == 'dog':
self.dog_queue.append(animal)
elif animal_type == 'cat':
self.cat_queue.append(animal)
elif animal_type == 'rabbit':
self.rabbit_queue.append(animal)
def dequeue_dog(self):
"""Dequeue and adopt a dog from the shelter."""
if self.dog_queue:
return self.dog_queue.pop(0)
else:
return None
def dequeue_cat(self)
if self.cat_queue:
return self.cat_queue.pop(0)
else:
return None
def dequeue_rabbit(self):
if self.rabbit_queue:
return self.rabbit_queue.pop(0)
else:
return None
def dequeue_any(self):
if self.dog_queue:
return self.dog_queue.pop(0)
elif self.cat_queue:
return self.cat_queue.pop(0)
elif self.rabbit_queue:
return self.rabbit_queue.pop(0)
else:
return None
def display_queue(self):
print("Dogs in the shelter:")
for dog in self.dog_queue:
print(dog)
print("Cats in the shelter:")
for cat in self.cat_queue:
print(cat)
print("Rabbits in the shelter:")
for rabbit in self.rabbit_queue:
print(rabbit)
# Example usage:
shelter = AnimalShelter()
shelter.enqueue('dog', 'Buddy')
shelter.enqueue('cat', 'Whiskers')
shelter.enqueue('rabbit', 'Thumper')
shelter.enqueue('dog', 'Rex')
print("Queue Contents Before Adoption:")
shelter.display_queue()
adopted_animal = shelter.dequeue_any()
if adopted_animal:
print(f"\nAdopted Animal: {adopted_animal}\n")
print("Queue Contents After Adoption:")
shelter.display_queue()
