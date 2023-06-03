# Write a function called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example function call:
#
def p_times(string, num):
    # count = 1
    # while count <= num:
    #     print(string)
    #     count += 1
    for n in range(num):
        print(n, string)

p_times('Hello there', 1)
#
# > Hello there
#
p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there
