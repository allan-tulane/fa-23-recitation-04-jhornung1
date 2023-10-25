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
Which still agrees with the asymptotic bounds and runtime complexity.

- **1c.**
So our graph looks like:
|   n |   qsort-fixed-pivot |   qsort-random-pivot |
|-----|---------------------|----------------------|
|  10 |               0.049 |                0.006 |
|  20 |               0.074 |                0.001 |
|  30 |               0.149 |                0.003 |
|  40 |               0.280 |                0.004 |
|  50 |               0.160 |                0.002 |
|  60 |               0.209 |                0.002 |
|  70 |               0.344 |                0.003 |
|  80 |               0.348 |                0.003 |
|  90 |               0.896 |                0.004 |
| 100 |               1.654 |                0.017 |
(once again, qsort-random-pivot is the time for Timsort)
So I don't really know what else to say besides that Timsort is incredibly effective. If we test with much larger values (this took a while to output, as qsort is a lot less effective) we get:
|     n |   qsort-fixed-pivot |   qsort-random-pivot |
|-------|---------------------|----------------------|
|  1000 |              11.436 |                0.021 |
|  2000 |              17.191 |                0.035 |
|  3000 |              22.130 |                0.053 |
|  4000 |              85.738 |                0.064 |
|  5000 |              31.149 |                0.072 |
|  6000 |              52.011 |                0.093 |
|  7000 |             102.407 |                0.102 |
|  8000 |             156.495 |                0.135 |
|  9000 |             189.659 |                0.136 |
| 10000 |             374.209 |                0.134 |
Which still agrees with the previous statement that Timsort is incredibly effective and seems to have a runtime complexity of O(n) or at least really close to that.
