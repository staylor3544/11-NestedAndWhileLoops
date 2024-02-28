###############################################################################
# DONE: 1. (3 pts)
#
#   For this _TODO_, write function called count() that takes one parameter:
#       number  <-- int
#
#   that simply counts from one until the number is reached (inclusive).
#
#   So, if the function is called like so:
#
#       count(5)
#
#   it would print:
#
#       1
#       2
#       3
#       4
#       5
#
#   Make sure to use a *while* loop in your solution. Also, notice how you will use the accumulator pattern for this problem.
#
#   Also, write a line of code that calls your function with whatever number you would like.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def count(number):
    i = 1
    while i <= number:
        print(i)
        i += 1

count(5)
count(30)
###############################################################################
# DONE: 2. (5 pts)
# For this _TODO_, write a function called adder() that will continually ask the use to enter a number (using user input) like so:
#
#       "Please Enter a Number: "
#
#   and will keep a running total of all the numbers that the user enters.
#
#   If the user enters a zero (0) the function should end and print the sum to the user like so:
#
#       "The sum is <TOTAL HERE>."
#
#   Your solution may use either just ints or in can also accept floats (it's up to you).
#
#   Do NOT worry about what happens when a user enters a value that is not a number. It can simply error out in this case.
#
#   Make sure to use a *while* loop in your solution. Also, notice how you will use the accumulator pattern for this problem.
#
#   Also, make sure to call your function to start things off.
#   
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def adder():
    total = 0
    while True:
        user_input = int(input("Please Enter a Number: "))
        if user_input == 0:
                break
        total += user_input
        print(f"The sum is {total}.")
                  
adder()

def adder1():
    total = 0
    while True:
        user_input = input("Please Enter a Number: ")
        try:
            number = float(user_input)
            total += number
        except ValueError:
            print("Invalid Input! Please enter a valid number.")
            continue

        if number == 0:
            break

    print(f"The sum is {total}.")

adder1()

###############################################################################
# DONE: 3. EXTRA CREDIT (3 pts)
#
#   DO NOT attempt this extra credit until you have completed m3!!!
#   
#   For this extra credit _TODO_, modify your code in _TODO_ #2 to handle the case when the user inputs a non-numeric input.
#
#   The function should maintain its total that it has calculated thus far and should prompt the user to enter a valid number like so:
#
#       "Invalid Input! Please enter a valid number: "
#
#   There are likely many ways you could accomplish this. Feel free to do some digging for potential solutions. Your solution should work no matter what the user types in.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################