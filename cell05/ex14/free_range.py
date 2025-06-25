#!/usr/bin/env python3
import sys
a = len(sys.argv)
if a != 3:
print("none")
else:
start = int(sys.argv[1])
end = int(sys.argv[2])
arr = [j for j in range(start , end + 1)]
print(arr)
