#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) Runtime: **O(n)**

`a = 0` is a single operation equal to **0(1)**. The `while` loop iterates **n^3** times, but the counter(a) is incremented by **n^2**.

b) Runtime: **O(n log(n))**

`sum = 0` is a single operation equal to **0(1)**. The `for` loop iterates n times, but the `while` loop interates **log n** times.

c) Runtime: **O(n)** (linear)

The `if` statement is a single operation equal to **0(1)**. The recursive statement will loop n times.

## Exercise II

To determine the value of floor `f`, I would use a binary search to start on the middle floor, and then drop the egg.

If the egg breaks, I would move down and try again, until the egg doesn't break. If the egg doesn't break, I would move up and try again until the egg breaks.

Time complexity: **O(log n)** (logarithmic)
