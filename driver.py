import math
import random
# import matplotlib.pyplot as plt
import timeit
import linear
# import binsearch
import bst
import rbtree

if __name__ == "__main__":
    f = open("small_data.txt", "w")
    for i in range(1000):
        f.write("%d " % random.randint(-1000, 1000))
    start = timeit.default_timer()
    if linear.linear_search():
        stop = timeit.default_timer()
    print(stop - start)

