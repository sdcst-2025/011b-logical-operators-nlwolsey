#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger

You can use an if statement to determine which is larger, or use the
max() function to determine the larger of the two
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
x = int(input("enter a number"))
y = int(input("enter another number"))
if x > y:
    if x % y == 0:
        print(f"{y} is a factor of {x}")
    else:
        print(f'{x} is not a factor of {y}')
elif y > x:
    if y % x == 0:
        print(f"{x} is a factor of {y}")
    else:
        print(f'{x} is not a factor of {y}')
else:
    print(f'{x} is not a factor of {y}')