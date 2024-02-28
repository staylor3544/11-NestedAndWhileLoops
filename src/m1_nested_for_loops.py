###############################################################################
# DONE: 1. (3 pts)
#
#   For this _TODO_, write a block of code that uses a nested for loop to print
#   the following output:
#
#   Outer: 1
#   Inner: 1
#   Inner: 2
#   Inner: 3
#   Outer: 2
#   Inner: 1
#   Inner: 2
#   Inner: 3
#
#   Notice how the outer loop will repeat twice and the inner loop will repeat
#   3 times. Do NOT "hard-code" the numbers that should print. You should use the indexes of the
#   for loops to determine what number to print.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
for outer in range(1, 3):
    print("Outer: ", outer)
    for inner in range(1, 4):
        print("Inner: ", inner)

###############################################################################
# DONE: 2. (4 pts)
#
#   For this _TODO_, write a function called many_triangles() that takes two
#   parameters:
#       - num_of_triangles    <-- int
#       - size                <-- int
#
#   where *num_of_triangles* is the number of triangles of stars that get printed and *size* is the size of each triangle.
#
#   So, if the function is called like this:
#   
#       many_triangles(2, 3)
#
#   it would print this:
#
#   *
#   **
#   ***
#   *
#   **
#   ***
#
#   Notice how this time we are creating triangles, we do *NOT* have a blank line as the first line of the triangle.
#
#   Also, write a line of code that calls your function with whatever numbers you would like.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def many_triangles(num_of_triangles, size):
    for _ in range(1, size):
        for i in range(1, num_of_triangles +2):
            print("*" * i )


many_triangles(2,3)
many_triangles(4,5)

    