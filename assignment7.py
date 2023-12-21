import tkinter as tk
from tkinter import messagebox

# Function to handle the registration process and store the details in a file
def register_student():
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()
    with open('student_details.txt', 'a') as file:
        file.write(f"{name},{age},{course}\n")
    messagebox.showinfo("Success", "Student registered successfully!")

# Function to read the details from the file
def read_details():
    with open('student_details.txt', 'r') as file:
        details = file.readlines()
    messagebox.showinfo("Details", details)

# Function to delete a student record
def delete_record():
    with open('student_details.txt', 'r') as file:
        lines = file.readlines()
    with open('student_details.txt', 'w') as file:
        for line in lines:
            if delete_entry.get() not in line:
                file.write(line)
    messagebox.showinfo("Success", "Record deleted successfully!")

# Function to show the student details
def show_details():
    new_window = tk.Tk()
    new_window.title("Student Details")
    with open('student_details.txt', 'r') as file:
        details = file.read()
    label = tk.Label(new_window, text=details, font=("Arial", 14))
    label.pack()

# GUI setup
root = tk.Tk()
root.title("Student Registration")
root.geometry("400x300")  # Set initial size of the window

name_label = tk.Label(root, text="Name:", font=("Arial", 12))
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.grid(row=0, column=1)

age_label = tk.Label(root, text="Age:", font=("Arial", 12))
age_label.grid(row=1, column=0)
age_entry = tk.Entry(root, font=("Arial", 12))
age_entry.grid(row=1, column=1)

course_label = tk.Label(root, text="Course:", font=("Arial", 12))
course_label.grid(row=2, column=0)
course_entry = tk.Entry(root, font=("Arial", 12))
course_entry.grid(row=2, column=1)

register_button = tk.Button(root, text="Register", command=register_student, font=("Arial", 12))
register_button.grid(row=3, column=0, columnspan=2, pady=10)

read_button = tk.Button(root, text="Read Details", command=read_details, font=("Arial", 12))
read_button.grid(row=4, column=0, columnspan=2, pady=10)

delete_label = tk.Label(root, text="Delete by Name:", font=("Arial", 12))
delete_label.grid(row=5, column=0)
delete_entry = tk.Entry(root, font=("Arial", 12))
delete_entry.grid(row=5, column=1)

delete_button = tk.Button(root, text="Delete", command=delete_record, font=("Arial", 12))
delete_button.grid(row=6, column=0, columnspan=2, pady=10)

show_button = tk.Button(root, text="Show Details", command=show_details, font=("Arial", 12))
show_button.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
