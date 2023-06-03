# x = 2
# print(x)
# x = 5
# print(x)

# DO_NOT_CHANGE_THIS = 5
# print(DO_NOT_CHANGE_THIS)
# DO_NOT_CHANGE_THIS = 3
# print(DO_NOT_CHANGE_THIS)

# Same exponent as in JS
# print(2 ** 3)
# # Same division as in JS
# print(14 / 3)
# # console.log(Math.floor(14 / 3)) in JS
# print(14 // 3)
# # Same modulo as in JS
# print(14 % 3)

# command and / will comment out a line or a group of highlighted lines in VS code regardless of the language
'''
Comments here for multi line comments
'''

# print('''text''')

number = 5
string = "Hello world"

# str(number) is a way to convert a number into a string. Unlike JS, every other language thinks adding a number and a string is an error...including Python
# print(str(number) + ' ' + string)
# An f string is the equivelent of a JS template literal (the backticks)
# print(f'{str(number)} is the number and {string} is the string')

# my_words = "This is my sentence".split(" ")
# print(my_words)

# my_letters = list("This is my letters sentence")
# print(my_letters)

# print("hello".index('h'))
# print("hello world".capitalize())

# print("hello".replace('l', "a"))

# print(len('hello world'))

# age = 77

# # It's key to notice the indentation
# if age < 18:
#     years_left = 18 - age
#     print(f'You cannot enter for another {years_left} years')
# elif age < 21:
#     print("You can come in but you can't drink")
# else:
#     print("You're welcome to do anything you want unless I decide you're too much and kick you out")

# print(years_left)

# count = 0
# while count < 5:
#     # print(count)
#     # count += 1
#     if(count != 3):
#         print(count)
#         count += 1
#     # print(count)

# def fizz_buzz(num):
#     # I want to start at 1 and until I hit the number, I want to print fizz, buzz, fizzbuzz or the number
#     # for n in range(num + 1):
#     #     string = ''
#     #     if n % 3 == 0:
#     #         string = "Fizz"
#     #     if n % 5 == 0:
#     #         string = string + "Buzz"
#     #     if string != '':
#     #         print(string)
#     #     else:
#     #         print(n)
#         # if n % 5 == 0 and n % 3 == 0:
#         #     print("FizzBuzz")
#         # elif n % 5 == 0:
#         #     print("Buzz")
#         # elif n % 3 == 0:
#         #     print("Fizz")
#         # else:
#         #     print(n)
#     count = 1
#     while count <= num:
#         if count % 15 == 0:
#             print("FizzBuzz")
#         elif count % 5 == 0:
#             print("Buzz")
#         elif count % 3 == 0:
#             print("Fizz")
#         else:
#             print(count)
#         count += 1


# fizz_buzz(20)
# fizz_buzz(50)

frogs = [
    "Bull", "Kermit", "Slippy", "Hoppy", "Voldemort",
    "Tadpole", "Poison dart frog", "Frodo", "Secret prince"
]

# print(len(frogs))
# print(frogs[0])
# We can use negative indexes in Python!!!! frogs[-2] gives us the second to last item. 
# print(frogs[-2])
frogs.pop(-2)
# print(frogs)
# Append to add one item to a list (an array)
frogs.append("Longlegs")
# extend is used when adding multiple items, which we put into an list, into an existing list
frogs.extend(["Another 1", "More frogs", "final frog"])
# print(frogs)

# If you just need the value, not the index, then you can just name a variable for the value of each index and the array. If you need the index, we use idx (or whatever you want to call it), name_for_the_value and then enumerate the list you're iterating through
# for frog in frogs:
#     print(f'This frog is named {frog}')
for idx, frog in enumerate(frogs):
    frogs[idx] = {'name': frog}
    # print(f'This frog at index {idx} is named {frog}')

# print(frogs)
# for(let i = 0; i < frogs.length; i++) {
#     print(`This frog is named ${frogs[i]}`)
# } is the JS equivelent

for idx, frog in enumerate(frogs):
    # print(frog['name'])
    frogs[idx] = {'name': frog['name'], 'age': idx}
    # for key in frogs[idx]:
        # print(f'The key is {key}')

# Checks if the key is in the object with the in keyword. Returns a boolean
# print('faceware' in frogs[0])
# frogs[0]['faceware'] = 'monacle'
# # print(frogs[0].get('faceware'))
# print(frogs[0])
# print('faceware' in frogs[0])
# print(frogs[0])

# del frogs[0]['faceware']
# print(frogs[0])

instructor = {
    'name': "Eric",
    'course': "SEI"
}
# The .items() creates a list of tuples (lists that cannot ever be modified) and using that we can grab both the key and the value in the for loop
print(instructor.items())
for key, value in instructor.items():
    print(f'{key} = {value}')

