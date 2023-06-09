# ## 1. **Create Phone Number**

# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example:

# createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"


# ## 2. **RGB To Hex Conversion**

# The RGB function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# **Note**: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# import rgb2hex

# def rgb(r, g, b):
#     return rgb2hex(r, g, b)
def rgb(r,g,b):
    letters = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    output = ''
    tup = r, g, b
    for num in tup:
        if num <= 0:
            output += '00'
        elif num >= 255:
            output += 'FF'
        else:
            if letters.get(num//16):
                output += letters[num//16]
            else:
                output += str(num // 16)
            if letters.get(num%16):
                output += letters[num%16]
            else:
                output += str(num % 16)
    return output

print(rgb(255, 255, 255)) # returns FFFFFF
print(rgb(255, 255, 300)) # returns FFFFFF
print(rgb(0,0,0)) # returns 000000
print(rgb(148, 0, 211)) # returns 9400D3