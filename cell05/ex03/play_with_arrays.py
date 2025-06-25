#!/usr/bin/env python3
array1 = [2,8,9,48,8,22,-12,2]
array2 = {(array1[i] + 2) for i in range(len(array1))}
print(f"Original array: {array1}")
print(f"New Array: {array2}")
