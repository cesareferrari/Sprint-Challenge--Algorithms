#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n)

Time complexity of the algorithm is O(n), linear because it increases relative
to n


b)

O(n^2)

Outer loop runs n times
Inner loop runs at least one time for each time the outer loop runs.


c)

O(n)

Linear time


## Exercise II


Linear approach:

We need to find the first floor that breaks the egg, and return the floor below it.

Set a counter = 0

while counter < n (number of floors)

throw egg from floor 1

if egg breaks, return the floor number - 1: we are done

if egg does not break: Increment counter += 1 

do next iteration

Complexity: O(n) linear (egg could break at the last floor)



Binary approach:

1. find the midpoint of the floors (n / 2) steps
2. Throw an egg.
3. if the egg breaks, eliminate all floors above midpoint.

Repeat steps 1 - 3 until egg doesn't break.
Return that floor.

Complexity: O(log n)

