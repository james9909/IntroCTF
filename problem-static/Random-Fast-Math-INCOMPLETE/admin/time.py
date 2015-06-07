import timeit
import math

print timeit.timeit('__import__("math").sqrt(876543212365)', number=10000)
print math.sqrt(876543212365)
