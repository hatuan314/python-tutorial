print('Hello world')
print('>'*10 + "HOANG ANH TUAN" + '<'*10)

# variables
# name = ''
# old = 20
# print('We check in a patient names John Smith.'
#       'He\'s 20 years old and is a new parent.')

# input
# Example 1
# name = input('What is your name ? ')
# favourite_color = input('What is your favourite color? ')
# print('Hi ' + name)
# print(name + ' likes ' + favourite_color)

# Example 2
# kilo = input('How many kilogram ? ')
# gram = 1000 * int(kilo)
# print(type(kilo))
# print(type(gram))
# print(str(kilo) + 'kg = ' + str(gram) + 'g')

# String
course = 'Python for Beginners'
print(course[0])
print(course[-2])
print(course[0:3])
print(course[2:])
print(course[:5])

name = "Jennifer"
print(name[1:-1])

first = "Hoang"
last = "Tuan"
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
# print(message)
print(msg)
print(len(course))
print(course.upper())
print(course.find('y'))
print(course.find('Beginners'))
print(course.replace('Beginners', 'absolute Beginners'))
print('Python' in course)
print('Jython' in course)