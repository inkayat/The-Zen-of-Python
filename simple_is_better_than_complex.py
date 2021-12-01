"""
  ___-ı |+___________
  |   ı |           |                 o---------|--/ ---|---[X]-|
  |                 |                           |       |       |
  |                 |                 o-----|   |       |___[X]_|
  |                 |     >                 |   |               |
 \                 [X]                o-|   |   |_____/ ____[X]_|
  |                 |                   |   |                   |
  |_________________|                 ----  |                   |
                                       --   |                   |
                                        -   |___________________|

"""


#Bad
import heapq

numbers = [-1, 12, -5, 0, 7, 21, 15, 1]
heapq.heapify(numbers)

sorted_numbers = []

while numbers:
    sorted_numbers.append(heapq.heappop(numbers))

print(sorted_numbers)


#Better
numbers = [-1, 12, -5, 0, 7, 21, 15, 1]
numbers.sort()

print(numbers)


