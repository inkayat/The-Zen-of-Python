"""
Nesting code makes it more difficult to follow and understand. Nesting two or three levels deep may still be good,
but anything beyond that becomes confusing and unreadable.

Even though you can actually have any level of nested loops or if statements in Python,
anything above three should be a clear signal that it’s maybe a good time to start refactoring your code.
"""

#Bad
x = float(input("Enter a number: "))

if x > 0:
    if x > 1:
        if x > 2:
            if x > 3:
                if x >= 4:
                    if x <= 6:
                        print("x is a number between 4 and 6.")
else:
    print("x is not a number between 4 and 6.")


#Better
x = float(input("Enter a number: "))

if x >= 4 and x <=6:
    print("x is a number between 4 and 6.")
else:
    print("x is not a number between 4 and 6.")

