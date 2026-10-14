# Comments start with the pound symbol
# 1. How to create variables for strings, numbers, booleans
name = "Dan Gilleland"
yearsAtNait = 26
employed = True
employer: str = 'Northern Alberta Institute of Technology'

# 2. How to output
#    {name} has worked for {years} at {employer}
print(f"{name} has worked for {yearsAtNait} at {employer}")

# 3. How to input
#    Prompt: What do you currently teach?
teach = input('What do you currently teach? ')
# Assume the data comes in as a single string with commas separating course numbers

# 4. How to create arrays/lists
course_list: list[str] = teach.split(',')
print()
# 5. Loop to display each course
for index, course in enumerate(course_list, start=1):
    print(f'{index}. {course.strip()}')

# 6. Get the user to input a number and I want to validate
#    that it is between 20 and 32 (inclusive)
class_size_str: str = input('Enter the class size: ')
# 
while not class_size_str.strip().isdigit():
    class_size_str = input('Try again - Enter a class size: ')

class_size: int = int(class_size_str)
print(f'{class_size} students per section')