"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""

from math import factorial as f

print(sum(list(map(int,list(str(f(100)))))))
