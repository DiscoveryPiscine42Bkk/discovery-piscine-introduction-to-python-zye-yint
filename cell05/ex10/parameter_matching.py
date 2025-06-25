#!/usr/bin/env python3
import sys
user = len(sys.argv)
if user != 2:
print("none")
else:
string = input("What was the parameter? ")
if string == sys.argv[1]:
print("Good job!")
else:
print("Nope, sorry...")
