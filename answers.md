# CMPS 2200 Reciation 5
## Answers

**Name:** Jacob Hornung 


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**

So first I changed the functino being returned in compare sort from random_pivot to ssort, so that I could compare ssort and qsort directly and have a table. With my first run (after I changed the values to be a little bit smaller) I recieved a table that looks like:
|     n |   qsort-fixed-pivot |   qsort-random-pivot |
|-------|---------------------|----------------------|
|    10 |               0.049 |                0.017 |
|    20 |               0.081 |                0.032 |
|    50 |               0.214 |                0.105 |
|   100 |               0.427 |                0.451 |
|   200 |               1.026 |                1.277 |
|   500 |               2.643 |                8.327 |
|  1000 |               8.882 |               66.619 |
|  2000 |              11.682 |              205.959 |
|  5000 |              76.175 |             1613.806 |
| 10000 |             119.097 |             5400.490 |
(qsort-random-pivot is my ssort function)
Qsort-fixed has a linearithmic runtime while ssort has a quadratice runtime. I think these tables show those two runtimes as when we plug these values into a graph generating tool (such as a graphing calculator), we have two lines that look like a linearithmic and a quadratic line. Also, we can give the function even more different values like the graph:
|   n |   qsort-fixed-pivot |   qsort-random-pivot |
|-----|---------------------|----------------------|
|  10 |               0.042 |                0.017 |
|  20 |               0.097 |                0.050 |
|  30 |               0.110 |                0.046 |
|  40 |               0.144 |                0.072 |
|  50 |               0.197 |                0.136 |
|  60 |               0.221 |                0.158 |
|  70 |               0.296 |                0.233 |
|  80 |               0.482 |                0.273 |
|  90 |               0.377 |                0.367 |
| 100 |               0.545 |                0.433 |
Which still agrees with the asymptotic bounds and runtime complexity


- **1c.**
