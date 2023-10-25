from main import *

import random

# 4 pts
def test_qsort_fixed():
  assert(qsort([5,4,3,2,1], lambda a: a[0])) == [1,2,3,4,5]

def test_qsort_fixed_custom():
  assert(qsort([3,4,2,5,7,6,8,9,1], lambda a: a[0])) == [1,2,3,4,5,6,7,8,9]

# 4 pts
def test_qsort_random():
  assert(qsort([5,4,3,2,1], lambda a: random.choice(a))) == [1,2,3,4,5]
